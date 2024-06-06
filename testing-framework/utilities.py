import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from scipy import integrate, interpolate  
from scipy.stats import gengamma, laplace, norm, kstwo, ks_1samp
from pathlib import Path
import pickle
import os
import pywt
import pywt.data
from PIL import Image

def sample_prior(r, eta, size=1):
    '''
    Samples from prior distribution of signal x
    r : shape parameter, must be > 0
    eta : shape parameter, controls roundedness of peak
    size : integer specifying number of samples required
    '''
    vars = gengamma.rvs(a = (eta + 1.5)/r, c = r, size = size)
    x = np.random.normal(scale = vars, size=size)
    return x

def round_to_sigfigs(x, num_sigfigs=5):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-(num_sigfigs-1)))

def extract_single_dist(all_dist_df, base_r, base_eta):
    return all_dist_df[(all_dist_df['base_r'] == base_r) & (all_dist_df['base_eta'] == base_eta)].drop(['base_r', 'base_eta'], axis = 1)

def kstest_custom(x, cdf, return_loc = False):
    n = len(x)
    x = np.sort(x)
    cdfvals = cdf(x)
    dplus, dminus = (np.arange(1.0, n + 1) / n - cdfvals), (cdfvals - np.arange(0.0, n)/n)
    plus_amax, minus_amax = dplus.argmax(), dminus.argmax()
    loc_max, loc_min = x[plus_amax], x[minus_amax]
    d = max(dplus[plus_amax], dminus[minus_amax])
    if return_loc:
        if d == plus_amax:
            return d, kstwo.sf(d, n), loc_max
        else:
            return d, kstwo.sf(d, n), loc_min
    return d, kstwo.sf(d, n)

def create_obs_x(data_dict, layer, only_diag = False):
    df = data_dict[layer]
    if not only_diag:
        df = df[(df['Orientation'] == 'H') | (df['Orientation'] == 'V')]
    else:
        df = df[df['Orientation'] == 'D']
    return np.sort(np.hstack(df['Data']))

def make_layer_df(x, cdfs_df):
    df = cdfs_df.copy()
    kstest_stat_pval = cdfs_df.apply(lambda row : kstest_custom(x, row.iloc[3]), axis = 1)
    df['kstest_stat'] = kstest_stat_pval.str[0]
    df['kstest_pval'] = kstest_stat_pval.str[1] 

    return df

def find_best_metric(obs_x, df, metric='kstest_stat'):
    df = df.copy()
    kstest_stat_pval = df.apply(lambda row : kstest_custom(obs_x, row.iloc[3]), axis = 1)
    df['kstest_stat'] = kstest_stat_pval.str[0]
    df['kstest_pval'] = kstest_stat_pval.str[1]
    df_metric = df.set_index(['r', 'eta'])[[metric]]
    if metric == 'kstest_stat':
        idx = df_metric.idxmin()
    elif metric == 'kstest_pval':
        idx = df_metric.idxmax()
    else:
        df_metric[metric] = df.apply(metric)
        idx = df_metric[[metric]].idxmin()
    r = idx.iloc[0][0]
    eta = idx.iloc[0][1]
    stat = df.set_index(['r', 'eta']).loc[idx, 'kstest_stat'].iloc[0]
    pval = df.set_index(['r', 'eta']).loc[idx, 'kstest_pval'].iloc[0]
    return np.array([r, eta, stat, pval])

def val_df_fixed_num(x, num_samples, df):
    val_df = pd.DataFrame(columns = ['r', 'eta', 'kstest_stat', 'kstest_pval'])
    all_subsets = np.array_split(x, x.size/num_samples)
    for i, x_s in enumerate(all_subsets):
        val_df.loc[i, :] = find_best_metric(x_s, df)
    val_df['num_samples'] = num_samples * np.ones(val_df.shape[0])
    return val_df

def convert_to_wavelet_basis(folder_dir,  normalized = True, basis="db1"):
    file_list = [os.path.join(folder_dir, filename) for filename in os.listdir(folder_dir)]
    file_names = os.listdir(folder_dir)

    df_dict = dict()
    image = Image.open(file_list[0]).convert('L')
    first_image = pywt.wavedec2(image, basis)
    layer_len = len(first_image)
    print(str(layer_len) + " layers being used")
    for i in range(layer_len):
        df = pd.DataFrame(columns=["Image ID", "Orientation", "Data"])
        df_dict[i+1] = df

    for k in range(len(file_list)):
        image = Image.open(file_list[k]).convert('L')
        image = np.array(image)
        if normalized:
            std= np.std(image)
            mean = np.mean(image)
            image = (image- mean)/std 
            
        name = file_names[k].split(".")[0]
        transformed = pywt.wavedec2(image, basis)
        df_dict[1].loc[len(df_dict[1].index)] = [name, "L1", np.array(transformed[0][0]).flatten()]
        direction_names = ['H', 'V', 'D']

        for i in range(1, layer_len): 
            for j in range(len(transformed[i])):
                arr = np.array(transformed[i][j])
                df_dict[i+1].loc[len(df_dict[i+1].index)] = [name, direction_names[j], arr.flatten()]

    return df_dict

def dict_to_pickle(converted_directory, converted, name):
    filename = name
    filename = os.path.join(converted_directory, filename)
    with open(filename+".pickle", 'wb') as handle:
        pickle.dump(converted, handle)

def compute_prior_cdf(r, eta, n_samples = 10000, tail_bound = 0.05, tail_percent = 0.01, scale = 1, scipy_int=True, support = False):

    '''
    Returns PPoly-type function that approximates the prior CDF of the signal x
    r : shape parameter controlling rate of exponentional decay
    eta : controls roundedness of peak, and hence sparsity
    scale : scale parameter
    n_samples : number of points used to numerically approximate CDF
    tail_bound : Uses Chebyshev's Inequality to bound the region of the CDF that is outside the coverage of xs
    n_tail : Sets the number of points tha lie outside the coverage of xs to approximate tails if need be

    Usage:
    new_cdf = compute_prior_cdf(r = 0.1, eta = 0.001)
    new_cdf(0.5343) returns CDF
    Can also accept arrays
    '''
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 2)/r)/scipy.special.gamma(beta)
    cheby = np.sqrt(np.round(var_prior/(tail_bound)))
    n_tail = int(n_samples*tail_percent)
    
    x_max = min(99, cheby) # introduced additional bound in case chebyshev is unwieldy
    if cheby < 120:
        n_tail = 0
        print("No Tail")
    
    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))
    prior_pdf = np.full(xs.shape, np.nan)

    for j, x in enumerate(xs):

        def gauss_density(theta):
            return (1./(np.sqrt(2*np.pi)*theta)) * np.exp(-0.5*(x/theta)**2)

        def gen_gamma_density(theta):
            return (r/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return gauss_density(theta) * gen_gamma_density(theta)

        if scipy_int:
            prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_pdf[j] = eng.compute_prior(float(r), float(eta), float(x), nargout=1)

    prior_cdf = np.zeros_like(prior_pdf)
    prior_cdf[0] = 0
    for i in range(1, len(xs)):
        prior_cdf[i] = (interpolate.CubicSpline(x = xs[:i+1], y = prior_pdf[:i+1])).integrate(xs[0], xs[i])+0

        # Alternative with Simpson's: prior_cdf[i] = integrate.simps(prior_pdf[:i+1], xs[:i+1])
    normalizer = prior_cdf[-1]
    first = prior_cdf[1]
    assert 1.05 > normalizer > 0.95
    assert 0.05 > first > -0.05
    prior_cdf = prior_cdf/normalizer   

    k = int(0.01*n_samples)
    zero_padding = np.zeros(k)
    ones_padding = np.ones(k)

    pad_max = max(10e5, np.round(cheby ** 2))
    prior_cdf = np.append(zero_padding, prior_cdf)
    xs_pad = np.append(np.linspace(-pad_max, xs[0] - 1e-5, k), xs)

    prior_cdf = np.append(prior_cdf, ones_padding)
    xs_pad = np.append(xs_pad, np.linspace(xs[-1] + 1e-5, pad_max, k))

    poly = interpolate.CubicSpline(x = xs_pad, y = prior_cdf)

    assert np.isclose(poly(-1e10), 0, atol = 1e-8)
    assert np.isclose(poly(1e10), 1, atol = 1e-8)

    if support:
        return xs, poly
    else:
        return poly

def compute_prior_pdf(r, eta, n_samples = 10000, tail_bound = 0.05, tail_percent = 0.01, scale = 1, scipy_int=True, support = True):

    '''
    Returns PPoly-type function that approximates the prior PDF of the signal x
    r : shape parameter controlling rate of exponentional decay
    eta : controls roundedness of peak, and hence sparsity
    scale : scale parameter
    n_samples : number of points used to numerically approximate CDF
    tail_bound : Uses Chebyshev's Inequality to bound the region of the CDF that is outside the coverage of xs
    n_tail : Sets the number of points tha lie outside the coverage of xs to approximate tails if need be

    Usage:
    new_cdf = compute_prior_cdf(r = 0.1, eta = 0.001)
    new_cdf(0.5343) returns CDF
    Can also accept arrays
    '''
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 2)/r)/scipy.special.gamma(beta)
    cheby = np.sqrt(np.round(var_prior/(tail_bound)))
    
    n_tail = int(n_samples*tail_percent)
    
    x_max = min(99, cheby) # introduced additional bound in case chebyshev is unwieldy
    if cheby < 120:
        n_tail = 0
        print("No Tail")
    

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))
    prior_pdf = np.full(xs.shape, np.nan)

    for j, x in enumerate(xs):

        def gauss_density(theta):
            return (1./(np.sqrt(2*np.pi)*theta)) * np.exp(-0.5*(x/theta)**2)

        def gen_gamma_density(theta):
            return (r/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return gauss_density(theta) * gen_gamma_density(theta)

        if scipy_int:
            prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_pdf[j] = eng.compute_prior(float(r), float(eta), float(x), nargout=1)

    if support:
        return xs, prior_pdf
    else:
        return prior_pdf
    

def combine_pickles(dir_name):
    CDFs_DIR = os.path.join(os.getcwd(), "CDFs")

    pickles = os.listdir(os.path.join(CDFs_DIR, dir_name))
    cdfs = dict()
    for pkl in pickles:
        
        pkl_path = os.path.join(CDFs_DIR, f'{dir_name}/{pkl}')
        with open(pkl_path, 'rb') as handle:
            new_cdf = pickle.load(handle)
        if type(new_cdf) == dict:
            cdfs = cdfs | new_cdf

    return cdfs

def compute_ksstat(sample, cdf, sorted_sample = True):
    '''
    Computes the KS-Test Statistic, assumes that the sample is already sorted
    '''
    if not sorted_sample:
        sample = np.sort(sample)

    if isinstance(cdf, tuple):
        r = cdf[0]
        eta = cdf[1]
        cdf = compute_prior_cdf(r, eta, 10000)
    
    n = len(sample)
    cdfvals = cdf(sample)
    dplus, dminus = (np.arange(1.0, n + 1) / n - cdfvals), (cdfvals - np.arange(0.0, n)/n)
    return np.max(np.append(dplus, dminus))

def gridsearch(sample, all_cdfs, top_k = 1):
    '''
    Takes in a sample and list of CDFs, 
    Returns the KS-Test Statistic computed with respect to each CDF, the top-k minimizing parameters and the corresponding distances
    '''
    cdf_keys = sorted(all_cdfs)
    cdf_splines = [all_cdfs[key] for key in cdf_keys]
    num_cdfs = len(cdf_keys)
    ksstats = np.zeros(num_cdfs)
    
    for i in range(num_cdfs):
        ksstats[i] = compute_ksstat(sample, cdf_splines[i])
    
    min_k = np.ones(top_k).astype(int)

    if top_k > 1:
        ksstats_copy = ksstats.copy()
        for i in np.arange(top_k):
            min_k[i] = np.argmin(ksstats_copy)
            ksstats_copy[min_k[i]] = 1
        return ksstats, [cdf_keys[j] for j in min_k], ksstats[min_k]
    else:
        return ksstats, cdf_keys[np.argmin(ksstats)], np.min(ksstats) 


def add_cdfs(r_range, eta_range, n_samples, scipy_int=True, folder_name=''):
    '''
    folder_name: Name of directory that contains pickles of dictionaries of cdfs
    r_range: range of r values, assumes use of np.arange
    eta_range: range of eta values, assumes use of np.arange
    check_redundant: if True, checks if key already exists in dictionary
    n_samples: number of samples used when computing prior_cdf
    '''
    
    if not os.path.isdir("CDFs"):
        raise Exception("This Directory Does Not Contain CDFs")
    
    if folder_name == '':
        folder_name = f'{min(r_range)}-{max(r_range)}{min(eta_range)}-{max(eta_range)}_'

    FOLDER_PATH = os.path.join("CDFs", folder_name+str(n_samples))
    cdfs_completed = set()
    if os.path.isdir(FOLDER_PATH):
        print(FOLDER_PATH)    
        for pkl in os.listdir(FOLDER_PATH):
            with open(os.path.join(FOLDER_PATH, pkl), 'rb') as handle:
                next_cdf = pickle.load(handle)
            cdfs_completed.update(next_cdf.keys())
    else:
        Path(os.path.join(os.getcwd(), FOLDER_PATH)).mkdir()
    print("CDFs completed:", len(cdfs_completed))
    n = len(r_range)*len(eta_range)

    if len(cdfs_completed) == n:
        print("Already computed")
        return
    
    cnt = 0
    grouped_r_cdf = dict()
    flag = False

    for r in r_range:
        r_cdf = dict()
        r = round_to_sigfigs(r, 6)
        for eta in eta_range:
            eta = round_to_sigfigs(eta, 6)
            if ((r, eta) in cdfs_completed):
                continue
            cnt += 1
            print(f'{(r, eta)}, {cnt} of {n}')
            r_cdf[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples,  tail_percent = 0.01, tail_bound = 0.01, scipy_int=scipy_int, support=False)

        # Store pickle every outer loop iteration as its own file
        # CDFs/<optional_folder_name><number of samples>/<r>_<min(eta)>-<max(eta)>.pickle
        min_eta, max_eta = round_to_sigfigs(eta_range[0], 6), round_to_sigfigs(eta_range[-1], 6)
        
        if len(eta_range) > 1:
            pkl_path = os.path.join(FOLDER_PATH,f'{r}_{min_eta}-{max_eta}.pickle')
            dump_dict_pkl(r_cdf, pkl_path, overwrite=False)
        else:
            grouped_r_cdf = grouped_r_cdf | r_cdf
            flag = True
    if flag:
        pkl_path = os.path.join(FOLDER_PATH, f'{round_to_sigfigs(r_range[0], 6)}-{round_to_sigfigs(r_range[-1], 6)}_{min_eta}.pickle')
        dump_dict_pkl(grouped_r_cdf, pkl_path, overwrite=False)

    print(f'You can find the CDFs here: {os.path.join(os.getcwd(), FOLDER_PATH)}')

def load_pkl(path):
    if os.path.isfile(path):
        with open(path, 'rb') as handle:
            obj = pickle.load(handle)
        return object
    else:
        raise Exception("File does not exist, check the path again")
    
def dump_dict_pkl(obj, path, overwrite = False):
    if overwrite:
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle)
    else:
        if os.path.isfile(path):
            with open(path, 'rb') as handle:
                existing_object = pickle.load(handle)
            obj = obj | existing_object
        else:
            with open(path, 'wb') as handle:
                pickle.dump(obj, handle)

def find_n_fixed_pval_stat(ksstat: float, n: int, cutoff=0.05, cache = True):
    """
    Finds the sample size 'n' required to achieve a target p-value 'cutoff' for a given Kolmogorov-Smirnov (KS) statistic 'ksstat'.

    Args:
        ksstat (float): The Kolmogorov-Smirnov statistic value.
        n (int): The initial sample size to start the search.
        cutoff (float, optional): The target p-value to achieve. Defaults to 0.05.

    Returns:
        int: The sample size 'n' required to achieve the target p-value 'cutoff' for the given 'ksstat'.

    Note:
        This function assumes the availability of the 'kstwo' function from a specific library (e.g., scipy.stats) 
        to calculate the survival function (sf) of the Kolmogorov-Smirnov distribution.
    """

    if cache:
        cache = pd.read_pickle('pickles/find_n_cache.pickle')
        if (round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2)) in cache:
            return cache[(round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2))]

    curr_pval = kstwo(n).sf(ksstat)
    while not np.isclose(curr_pval, cutoff, atol=0.01):

        if (round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2)) in cache:
            return cache[(round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2))]
        if curr_pval < cutoff:
            n = int(n / 2)
            curr_pval = kstwo(n).sf(ksstat)
        elif curr_pval > cutoff:
            n = int(n * 1.5)
            curr_pval = kstwo(n).sf(ksstat)
    if cache:
        cache[(round_to_sigfigs(ksstat, 2), n)] = n
        dump_dict_pkl(cache, 'pickles/find_n_cache.pickle')
    return n

def coord_descent_gengamma(sample, initial_param, r_depth, eta_depth, layer, completed_r_depth = 1, completed_eta_depth = 1):
    '''
    Perform coordinate descent optimization to find the best parameters (r, eta) for a generalized gamma distribution
    that minimizes the Kolmogorov-Smirnov (KS) statistic for the given `sample`.
    
    Args:
       sample (numpy.ndarray): The sample data for which the KS statistic is computed.
       initial_param (tuple): The initial guess for the parameters (r, eta).
       r_depth (int): The number of decimal places to search for the optimal value of 'r'.
       eta_depth (int): The number of decimal places to search for the optimal value of 'eta'.
       layer (int): The layer index for naming the intermediate pickles.
       completed_r_depth (int, optional): The number of decimal places already completed for 'r'. Defaults to 1.
       completed_eta_depth (int, optional): The number of decimal places already completed for 'eta'. Defaults to 1.
       
    Returns:
       tuple: The optimal values of (r, eta) that minimize the KS statistic for the given `sample`.

    Example:
    `coord_descent_gengamma(obs_x_dict[4], (0.8, 3), 3, 2, 4)` will search through
    r = range(0.70, 0.90, 0.01), eta = 3. Suppose best value is 0.80 (2 decimals)
    r = range(0.780, 0.800, 0.001), eta = 3. Suppose best value is r=0.803 (3 decimals)
    Then
    r = 0.803, eta = range(2.9, 3.1, 0.01). Suppose best value is eta=3.01 (2 decimals)

    returns 0.803, 3.01
    '''
    r_0, eta_0 = initial_param

    for d in np.arange(completed_r_depth, r_depth):
            
        r_range = np.arange(r_0 - 10.0**(-d), r_0 + 10.0**(-d), 10.0**(-d-1)) 
        eta_range = [eta_0]
        add_cdfs(r_range, eta_range, 10000, True, f'layer{layer}_')
        layer_cdfs = combine_pickles(f'layer{layer}_10000')
        ksstats, best_param, min_stat = gridsearch(sample, layer_cdfs)
        r_0 = round_to_sigfigs(best_param[0], d+1)


    for d in np.arange(completed_eta_depth, eta_depth):
            
        r_range = [r_0]
        eta_range = np.arange(max(eta_0 - 10.0**(-d), 0), eta_0 + 10.0**(-d), 10.0**(-d-1)) 
        add_cdfs(r_range, eta_range, 10000, True, f'layer{layer}_')
        layer_cdfs = combine_pickles(f'layer{layer}_10000')
        ksstats, best_param, min_stat = gridsearch(sample, layer_cdfs)
        eta_0 = round_to_sigfigs(best_param[1], d+1)

    return (r_0, eta_0)