import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from scipy import integrate, interpolate  
from scipy.stats import gengamma, laplace, norm, kstwo, ks_1samp
import matplotlib.pyplot as plt
import pickle
import os

#os.chdir('C:\\Users\\yashd\\Desktop\\hierarchical-bayesian-model-validation\\testing-framework')

def compute_prior_pdf(r, eta, n_samples = 10000, tail_bound = 0.05, n_tail = 5, scale = 1):

    '''
    Returns support and pdf for prior distribution
    r : shape parameter controlling rate of exponentional decay
    eta : controls roundedness of peak, and hence sparsity
    scale : scale parameter
    n_samples : number of points used to numerically approximate CDF
    tail_bound : Uses Chebyshev's Inequality to bound the region of the CDF that is outside the coverage of xs
    n_tail : Sets the number of points tha lie outside the coverage of xs to approximate tails if need be

    Usage:
    new_pdf = compute_prior_cdf(r = 0.1, eta = 0.001)
    new_pdf(0.5343) returns CDF
    Can also accept arrays
    '''
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 1/2)/r)/scipy.special.gamma(beta)
    x_max = min(100, np.round(var_prior/tail_bound)) # introduced additional bound in case chebyshev is unwieldy
    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(np.linspace(-(x_max+100), -(x_max+20), n_tail), xs)
    xs = np.append(xs, np.linspace(x_max + 20, x_max + 100, n_tail))
    prior_pdf = np.full(xs.shape, np.nan)

    # Loop over xs
    for j, x in enumerate(xs):

        # Define integrands
        def gauss_density(theta):
            return (1./(np.sqrt(2*np.pi)*theta)) * np.exp(-0.5*(x/theta)**2)

        def gen_gamma_density(theta):
            return (r/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return gauss_density(theta) * gen_gamma_density(theta)

        # Integrate 
        prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
    return xs, prior_pdf

def compute_prior_cdf(r, eta, n_samples = 1000, tail_bound = 0.05, n_tail = 5, scale = 1):

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
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 1/2)/r)/scipy.special.gamma(beta)
    x_max = min(100, np.round(var_prior/tail_bound)) # introduced additional bound in case chebyshev is unwieldy
    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(np.linspace(-(x_max+100), -(x_max+20), n_tail), xs)
    xs = np.append(xs, np.linspace(x_max + 20, x_max + 100, n_tail))
    prior_pdf = np.full(xs.shape, np.nan)

    # Loop over xs
    for j, x in enumerate(xs):

        # Define integrands
        def gauss_density(theta):
            return (1./(np.sqrt(2*np.pi)*theta)) * np.exp(-0.5*(x/theta)**2)

        def gen_gamma_density(theta):
            return (r/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return gauss_density(theta) * gen_gamma_density(theta)

        # Integrate 
        prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]

    prior_cdf = np.zeros_like(prior_pdf)
    for i in range(len(xs) - 1):
        prior_cdf[i] = np.trapz(prior_pdf[:i+1], xs[:i+1]) 
    prior_cdf = np.append(prior_cdf[:-1], 1)

    poly = interpolate.CubicSpline(x = xs, y = prior_cdf)
    return poly

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

def sample_laplace(size=1):
    '''
    Samples from laplace distribution
    size : integer specifying number of samples required
    '''
    return laplace.rvs(size = size)

def cartesian_product(*arrays):
    " Credits: https://stackoverflow.com/a/11146645"
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def round_to_2_sigfigs(x):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-1))

def add_cdfs(pickle_name, r_range, eta_range, check_redundant = False, n_samples = 10000):
    '''
    pickle_name: Name of pickle file that stores dictionary of cdfs, does not include the '.pickle'
    r_range: range of r values, assumes use of np.arange
    eta_range: range of eta values, assumes use of np.arange 
    check_redundant: if True, checks if key already exists in dictionary 
    n_samples: number of samples used when computing prior_cdf
    '''
    if os.path.isfile(f'CDFs/{pickle_name}.pickle'):
        with open(f'CDFs/{pickle_name}.pickle', 'rb') as handle:
            cdfs = pickle.load(handle)
    else:
        cdfs = dict()
    n = len(r_range)*len(eta_range)
    i = 0
    for r in r_range:
        for eta in eta_range:
            
            (r, eta) = (round_to_2_sigfigs(r), round_to_2_sigfigs(eta))
            if check_redundant:
                if ((r, eta) in cdfs):
                    continue
            print(f'{(r, eta)}, {i} of {n}')
            i += 1
            cdfs[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples)

        # Store pickle every outer loop iteration
        with open(f'CDFs/{pickle_name}.pickle', 'wb') as handle:
            pickle.dump(cdfs, handle) 

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
            return loc_max
        else:
            return loc_min
    return d, kstwo.sf(d, n)

def create_obs_x(data_dict, layer, only_diag = False):
    df = data_dict[layer]
    if not only_diag:
        df = df[(df['Orientation'] == 'H') | (df['Orientation'] == 'V')]
    else:
        df = df[df['Orientation'] == 'D']
    return np.hstack(df['Data'])

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


        