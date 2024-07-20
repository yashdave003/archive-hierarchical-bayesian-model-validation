import numpy as np
import pandas as pd
import scipy
from scipy import integrate, interpolate, stats
from pathlib import Path
import pickle
import os
import pywt
import pywt.data
from PIL import Image

def sample_prior(r, eta, size=1):
    '''
    Samples from prior distribution of signal x
    r : shape parameter, must be nonzero
    eta : shape parameter, controls roundedness of peak, must be picked such that beta=(1.5+eta)/r > 0
    size : integer specifying number of samples required

    Note: Theta ~ GenGamma is modeled as the variance of the Normal, scale takes in the standard deviation. 
    This matches up with the original paper on "Sparse Reconstructions ..." by Calvetti et. al. 2020
    '''
    beta = (eta + 1.5)/r
    assert beta > 0
    vars = stats.gengamma.rvs(a = beta, c = r, size = size)
    x = np.random.normal(scale = np.sqrt(vars), size=size)
    return x

def compute_prior_pdf(r, eta, n_samples = 10000, tail_bound = 0.05, tail_percent = 0.01, scale = 1, scipy_int=True, eng= None, debug=False):
    
    """
    Computes the prior probability density function (PDF) for given parameters r and eta.

    Inputs:
    - r (float): Shape parameter for the generalized gamma distribution, recommended r >= 0.4
    - eta (float): Parameter related to the beta in the generalized gamma distribution, recommended eta >= 0
    - n_samples (int, optional): Number of samples to generate. Default is 10000
    - tail_bound (float, optional): Bound for the tail of the distribution. Default is 0.05
    - tail_percent (float, optional): Percentage of samples to allocate to the tail. Default is 0.01
    - scale (float, optional): Scale parameter for the distribution. Default is 1
    - scipy_int (bool, optional): If True, uses SciPy for integration. If False, uses 'eng'. Default is True
    - eng (object, optional): MATLAB engine for computation if scipy_int is False. Default is None
    - debug (bool, optional): If True, prints debug information. Default is False

    Outputs:
    - xs (numpy.ndarray): Array of x values
    - pdf (numpy.ndarray): Corresponding PDF values

    Note: The function uses a combination of linear and logarithmic spacing for x values to capture both the central part and the tails of the distribution.
    With 10000 samples and relatively large eta values, computed CDFs are reliable for r >= 0.4. For more robust CDFs, use MATLAB. 
    Though the distribution is defined for some values of eta < 0, this function does not reliably compute CDFs in this region.

    """

    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma(beta + 1/r)/scipy.special.gamma(beta)
    cheby = np.sqrt(var_prior/(tail_bound))
    n_tail = int(n_samples*tail_percent)
    
    # introduced additional bound in case chebyshev is unwieldy
    x_max = min(99, cheby) 
    if cheby < 120:
        n_tail = 0
        if debug:
            print(f"No tail")
    if debug:
        print(f"Chebyshev bound: {cheby}")

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))

    prior_pdf = np.full(xs.shape, np.nan)

    for j, x in enumerate(xs):

        # Note that theta = variance, np.sqrt(theta) = SD
        def gauss_density(theta):
            return (1./(np.sqrt(2*np.pi)*np.sqrt(theta))) * np.exp(-0.5*(x**2/theta))

        def gen_gamma_density(theta):
            return (np.abs(r)/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return gauss_density(theta) * gen_gamma_density(theta)

        if scipy_int:
            prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_pdf[j] = eng.compute_prior(float(r), float(eta), float(x), nargout=1)
    
    return xs, prior_pdf

def pdf_to_cdf(xs, prior_pdf, return_assert=False, enforce_assert=True, debug = False):
    """
    Converts a probability density function (PDF) to a cumulative distribution function (CDF).

    Inputs:
    - xs (numpy.ndarray): Array of x values
    - prior_pdf (numpy.ndarray): Corresponding PDF values
    - enforce_assert (bool, optional): If True, applies assertion checks. Default is True
    - debug (bool, optional): If True, prints debug information. Default is False

    Output:
    - cdf_spline (scipy.interpolate.CubicSpline): CubicSpline interpolation of the CDF

    Note: The function pads the CDF with zeros and ones at the extremes to ensure proper behavior at the tails.
    """

    prior_cdf = np.zeros_like(prior_pdf)
    prior_cdf[0] = 0
    for i in range(1, len(xs)):
        prior_cdf[i] = (interpolate.CubicSpline(x=xs[:i+1], y=prior_pdf[:i+1])).integrate(xs[0], xs[i])+0

    normalizer = prior_cdf[-1]
    first = prior_cdf[1]

    if debug:
        print("First CDF value:", first)
        print("Last CDF value:", normalizer)

    if return_assert:
        if not 0.05 > first > -0.05:
            return None
        if not 1.05 > normalizer > 0.95:
            return None    

    if enforce_assert:
        assert 0.05 > first > -0.05    
        assert 1.05 > normalizer > 0.95
    
    prior_cdf = prior_cdf/normalizer   

    k = int(0.01*len(xs))
    zero_padding = np.zeros(k)
    ones_padding = np.ones(k)

    pad_max = max(10e5, np.round(max(np.abs(xs)) ** 2))
    if debug:
        print(f"0, 1 padding bounds: {pad_max}")

    prior_cdf_padded = np.concatenate([zero_padding, prior_cdf, ones_padding])
    xs_padded = np.concatenate([
        np.linspace(-pad_max, xs[0] - 1e-5, k),
        xs,
        np.linspace(xs[-1] + 1e-5, pad_max, k)
    ])

    cdf_spline = interpolate.CubicSpline(x=xs_padded, y=prior_cdf_padded)

    if enforce_assert:
        assert np.isclose(cdf_spline(-1e10), 0, atol=1e-8)
        assert np.isclose(cdf_spline(1e10), 1, atol=1e-8)

    return cdf_spline


def compute_prior_cdf(r, eta, n_samples=10000, tail_bound=0.05, tail_percent=0.01, scale=1, scipy_int=True, eng=None, enforce_assert=True, return_assert = False, return_pdf=False, debug=False):
    """
    Computes the prior cumulative density function (CDF) for given parameters r and eta. Optionally returns support, pdf, cdf (as a spline) in that order

    Inputs:
    - r (float): Shape parameter for the generalized gamma distribution, recommended r >= 0.4
    - eta (float): Parameter related to the beta in the generalized gamma distribution, recommended eta >= 0
    - n_samples (int, optional): Number of samples to generate. Default is 10000
    - tail_bound (float, optional): Bound for the tail of the distribution. Default is 0.05
    - tail_percent (float, optional): Percentage of samples to allocate to the tail. Default is 0.01
    - scale (float, optional): Scale parameter for the distribution. Default is 1
    - scipy_int (bool, optional): If True, uses SciPy for integration. If False, uses 'eng'. Default is True
    - eng (object, optional): MATLAB engine for computation if scipy_int is False. Default is None
    - enforce_assert (bool, optional): If True, applies assertion checks in pdf_to_cdf. Default is True
    - return_pdf (bool, optional): If True, also returns the PDF. Default is False
    - debug (bool, optional): If True, prints debug information. Default is False

    Note: The function uses a combination of linear and logarithmic spacing for x values to capture both the central part and the tails of the distribution.
    With 10000 samples and relatively large eta values, computed CDFs are reliable for r >= 0.4. For more robust CDFs, use MATLAB. 
    Though the distribution is defined for some values of eta < 0, this function does not reliably compute CDFs in this region. 

    Outputs:
    If return_pdf is False:
    - poly (scipy.interpolate.CubicSpline): CubicSpline interpolation of the CDF

    If return_pdf is True:
    - xs (numpy.ndarray): Array of x values
    - prior_pdf (numpy.ndarray): Corresponding PDF values
    - cdf_spline (scipy.interpolate.CubicSpline): CubicSpline interpolation of the CDF
    """

    xs, prior_pdf = compute_prior_pdf(r = r, eta = eta, n_samples = n_samples, 
                                      tail_bound = tail_bound, tail_percent = tail_percent, 
                                      scale = scale, scipy_int = scipy_int, eng = eng, debug = debug)
    cdf_spline = pdf_to_cdf(xs = xs, prior_pdf = prior_pdf, enforce_assert = enforce_assert, return_assert = return_assert, debug = debug)

    if return_pdf:
        return xs, prior_pdf, cdf_spline
    else:
        return cdf_spline

def round_to_sigfigs(x, num_sigfigs=5):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-(num_sigfigs-1)))

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
            return d, stats.kstwo.sf(d, n), loc_max
        else:
            return d, stats.kstwo.sf(d, n), loc_min
    return d, stats.kstwo.sf(d, n)

def create_obs_x(data_dict, layer, only_diag = False):
    df = data_dict[layer]
    if not only_diag:
        df = df[(df['Orientation'] == 'H') | (df['Orientation'] == 'V')]
    else:
        df = df[df['Orientation'] == 'D']
    return np.sort(np.hstack(df['Data']))

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

def compute_ksstat_tail(sample, cdf, sorted_sample = True, tail_cutoff = 2):
    '''
    Computes the KS-Test Statistic, assumes that the sample is already sorted
    '''
    if not sorted_sample:
        sample = np.sort(sample)

    tail_idxs = np.argwhere(np.abs(sample) > tail_cutoff)
    tails = sample[tail_idxs]

    if isinstance(cdf, tuple):
        r = cdf[0]
        eta = cdf[1]
        cdf = compute_prior_cdf(r, eta, 10000)
    
    n = len(sample)
    cdfvals = cdf(sample)
    dplus, dminus = (np.arange(1.0, n + 1) / n - cdfvals), (cdfvals - np.arange(0.0, n)/n)
    dplus_t, dminus_t = dplus[tail_idxs], dminus[tail_idxs]
    return np.max(np.append(dplus_t, dminus_t))

def compute_ksratio(sample, cdf, sorted_sample = True, tail_cutoff = 0):
    '''
    Computes the ratio of empirical and computed cdfs, assumes that the sample is already sorted
    '''
    if not sorted_sample:
        sample = np.sort(sample)
    tail_idxs = np.argwhere((np.abs(sample) > tail_cutoff))
    tails = sample[tail_idxs]

    if isinstance(cdf, tuple):
        r = cdf[0]
        eta = cdf[1]
        cdf = compute_prior_cdf(r, eta, 10000)
    
    n = len(sample)
    tail_vals = cdf(tails)
    d = (np.arange(1.0, n + 1) / n)
    tail_ratios = np.nan_to_num(d[tail_idxs] / tail_vals)
    # empirical / computed
    return (round_to_sigfigs(np.min(tail_ratios)), round_to_sigfigs(np.max(tail_ratios)))


def gridsearch(sample, all_cdfs, top_k = 1, debug = False):
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
        if debug:
            print(f"Computing {i} of {num_cdfs}")
    
    min_k = 2*np.ones(top_k).astype(int)
    if debug:
        print(f"Finding Minimum after computing {num_cdfs} CDFs")
    if top_k > 1:
        ksstats_copy = ksstats.copy()
        for i in np.arange(top_k):
            min_k[i] = np.argmin(ksstats_copy)
            ksstats_copy[min_k[i]] = 2
        return ksstats, [cdf_keys[j] for j in min_k], ksstats[min_k]
    else:
        return ksstats, cdf_keys[np.argmin(ksstats)], np.min(ksstats) 


def add_cdfs(r_range, eta_range, n_samples, scipy_int=True, folder_name='', debug = False, eng=None, enforce_assert=True, return_assert = False):
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
        folder_name = f'{min(r_range)}-{max(r_range)}{min(eta_range)}-{max(eta_range)}_{n_samples}'

    FOLDER_PATH = os.path.join("CDFs", folder_name)
    cdfs_completed = set()
    if os.path.isdir(FOLDER_PATH):
        print(FOLDER_PATH)    
        for pkl in os.listdir(FOLDER_PATH):
            with open(os.path.join(FOLDER_PATH, pkl), 'rb') as handle:
                next_cdf = pickle.load(handle)
            cdfs_completed.update(next_cdf.keys())
    else:
        Path(os.path.join(os.getcwd(), FOLDER_PATH)).mkdir()
    if debug:
        print("CDFs completed:", len(cdfs_completed))
    n = len(r_range)*len(eta_range)

    if len(cdfs_completed) == n:
        if debug:
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
            if debug:
                print(f'{(r, eta)}, {cnt} of {n}')
            computed_cdf = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples, tail_percent = 0.01, tail_bound = 0.01, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert)
            if computed_cdf is None:
                
                with open("faultyCDFs_brandon.csv", 'a') as handle:
                    handle.write(f"{r},{eta},{n_samples}\n")
                with open("faultyCDF_log.txt", 'a') as handle:
                    handle.write(f"Failed assert for r={r}, eta={eta}, n_samples={n_samples}")
                    handle.write(f"Skipping {eta} (exclusive) to {max(eta_range)} for r={r}")
                print(f"Failed assert for r={r}, eta={eta}, n_samples={n_samples}")
                print(f"Skipping {eta} (exclusive) to {max(eta_range)} for r={r}")
                break
            r_cdf[(r, eta)] = computed_cdf

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

    if debug:
        print(f'You can find the CDFs here: {os.path.join(os.getcwd(), FOLDER_PATH)}')

def load_pkl(path):
    if os.path.isfile(path):
        with open(path, 'rb') as handle:
            obj = pickle.load(handle)
        return obj
    else:
        raise Exception("File does not exist, check the path again")
    
def dump_dict_pkl(obj, path, overwrite = False, debug=False):
    if overwrite:
        if debug:
            print("Overwriting existing file if it exists")
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle)
    elif os.path.isfile(path):
        if debug:
            print("Appending to Existing File")
        with open(path, 'rb') as handle:
            existing_object = pickle.load(handle)
        obj = obj | existing_object
    else:
        if debug:
            print("Writing to new file")
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

    curr_pval = stats.kstwo(n).sf(ksstat)
    while not np.isclose(curr_pval, cutoff, atol=0.01):

        if (round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2)) in cache:
            return cache[(round_to_sigfigs(ksstat, 2), round_to_sigfigs(n, 2))]
        if curr_pval < cutoff:
            n = int(n / 2)
            curr_pval = stats.kstwo(n).sf(ksstat)
        elif curr_pval > cutoff:
            n = int(n * 1.5)
            curr_pval = stats.kstwo(n).sf(ksstat)
    if cache:
        cache[(round_to_sigfigs(ksstat, 2), n)] = n
        dump_dict_pkl(cache, 'pickles/find_n_cache.pickle')
    return n

def coord_descent_gengamma(sample, initial_param, r_depth, eta_depth, group, completed_r_depth = 1, completed_eta_depth = 1, debug = True, DATA_NAME = None, eng=None, scipy_int = True):
    '''
    Perform coordinate descent optimization to find the best parameters (r, eta) for a generalized gamma distribution
    that minimizes the Kolmogorov-Smirnov (KS) statistic for the given `sample`.
    
    Args:
       sample (numpy.ndarray): The sample data for which the KS statistic is computed.
       initial_param (tuple): The initial guess for the parameters (r, eta).
       r_depth (int): The number of decimal places to search for the optimal value of 'r'.
       eta_depth (int): The number of decimal places to search for the optimal value of 'eta'.
       group (int): The layer index for naming the intermediate pickles.
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
    n_samples = 10000

    for d in np.arange(completed_r_depth, r_depth):
        if debug:
            print(f"Optimizing r, current depth {d} of {r_depth}, r = {r_0}")
        r_range = np.arange(r_0 - 10.0**(-d), r_0 + 10.0**(-d), 10.0**(-d-1)) 
        eta_range = [eta_0]
        add_cdfs(r_range=r_range, eta_range=eta_range, n_samples=n_samples, folder_name=f'{DATA_NAME}_group{group}_{n_samples}', eng=eng, scipy_int=scipy_int)
        layer_cdfs = combine_pickles(f'{DATA_NAME}_group{group}_{n_samples}')
        ksstats, best_param, min_stat = gridsearch(sample, layer_cdfs)
        r_0 = round_to_sigfigs(best_param[0], d+1)

    for d in np.arange(completed_eta_depth, eta_depth):
        if debug:
            print(f"Optimizing eta, current depth {d} of {eta_depth}, eta = {eta_0}")
        r_range = [r_0]
        eta_range = np.arange(max(eta_0 - 10.0**(-d), 0), eta_0 + 10.0**(-d), 10.0**(-d-1)) 
        add_cdfs(r_range=r_range,eta_range=eta_range, n_samples=n_samples, folder_name=f'{DATA_NAME}_group{group}_{n_samples}', eng=eng, scipy_int=scipy_int)
        layer_cdfs = combine_pickles(f'{DATA_NAME}_group{group}_{n_samples}')
        ksstats, best_param, min_stat = gridsearch(sample, layer_cdfs)
        eta_0 = round_to_sigfigs(best_param[1], d+1)

    return (r_0, eta_0)

def coord_descent_scipy(sample, initial_param):
    r_0, eta_0 = initial_param
    find_r_1 = scipy.optimize.minimize_scalar(generate_func(sample, 'gengamma_r', eta_0), method = 'bounded', bounds = (max(0.5, r_0-0.1), r_0+0.1))
    r_1 = find_r_1['x']
    find_eta_1 = scipy.optimize.minimize_scalar(generate_func(sample, 'gengamma_eta', r_1), method = 'bounded', bounds = (max(0, eta_0-0.1), eta_0+0.1))
    eta_1 = find_eta_1['x']
    find_r_2 = scipy.optimize.minimize_scalar(generate_func(sample, 'gengamma_r', eta_1), method = 'bounded', bounds = (max(0.5, r_1-0.1), r_1+0.1))
    r_2 = find_r_2['x']

    return (r_2, eta_1)

def generate_func(sample, distro, *args):
    if distro == 'gaussian' or distro == 'normal':
        def var_func(var):
            cdf = scipy.stats.norm(scale = var).cdf
            return compute_ksstat(sample, cdf)
        return var_func
    elif distro == 'laplace':
        def var_func(var):
            cdf = scipy.stats.laplace(scale = var).cdf
            return compute_ksstat(sample, cdf)
        return var_func
    elif distro == 't':
        def var_func(var):
            cdf = scipy.stats.t(df = 2, scale = var).cdf
            return compute_ksstat(sample, cdf)
        return var_func
    elif distro == 'gengamma_r':
        eta = args[0]
        def r_func(r):
            cache = pd.read_pickle('CDFs/optimize_cache.pickle')
            if (r, eta) in cache:
                cdf = cache[(r, eta)]
                return compute_ksstat(sample, cdf)
            else:
                cdf = compute_prior_cdf(r, eta, 10000)
            cache[(r, eta)] = cdf
            pd.to_pickle(cache, "CDFs/optimize_cache.pickle")
            return compute_ksstat(sample, cdf)
        return r_func
    elif distro == 'gengamma_eta':
        r = args[0]
        def eta_func(eta):
            cache = pd.read_pickle('CDFs/optimize_cache.pickle')
            if (r, eta) in cache:
                cdf = cache[(r, eta)]
                return compute_ksstat(sample, cdf)
            else:
                cdf = compute_prior_cdf(r, eta, 10000)
            cache[(r, eta)] = cdf
            pd.to_pickle(cache, "CDFs/optimize_cache.pickle")
            return compute_ksstat(sample, cdf)
        return eta_func
    print("Please enter a valid argument for `distro` : 'gaussian', 'laplace', 'gengamma_r', 'gengamma_eta', 't'")