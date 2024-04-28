
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from scipy import integrate, interpolate  
from scipy.stats import gengamma, laplace, norm, kstwo, ks_1samp
import matplotlib.pyplot as plt
import pickle
from pathlib import Path
import os

USE_MATLAB = False

if USE_MATLAB:
    import matlab.engine 
    eng = matlab.engine.connect_matlab()


def compute_prior_cdf(r, eta, n_samples = 1000, tail_bound = 0.05, n_tail = 5, scale = 1, scipy_int=True):

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
    
    x_max = min(99, cheby) # introduced additional bound in case chebyshev is unwieldy
    if cheby < 120:
        n_tail = 0
        print("No Tail")
    

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))
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
        if scipy_int:
            prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_pdf[j] = eng.testIntegrals(float(r), float(eta), float(x), nargout=1)

    prior_cdf = np.zeros_like(prior_pdf)
    for i in range(len(xs) - 1):
        prior_cdf[i] = np.trapz(prior_pdf[:i+1], xs[:i+1])
    prior_cdf = np.append(prior_cdf[:-1], 1)
    poly = interpolate.CubicSpline(x = xs, y = prior_cdf)

    # TODO: normalize based on last value in CDF

    # TODO: add assert statements to act as unit tests
    # assert area is 1 using pdf
    # assert last point is 1

    return poly

def round_to_sigfigs(x, num_sigfigs=2):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-(num_sigfigs-1)))

def add_cdfs(r_range, eta_range, n_samples = 10000, scipy_int=True, folder_name=''):
    '''
    folder_name: Name of directory that contains pickles of dictionaries of cdfs
    r_range: range of r values, assumes use of np.arange
    eta_range: range of eta values, assumes use of np.arange
    check_redundant: if True, checks if key already exists in dictionary
    n_samples: number of samples used when computing prior_cdf
    '''
    FOLDER_PATH = f'testing-framework\\CDFs\\{folder_name}{n_samples}\\'
    cdfs_completed = set()
    if os.path.isdir(FOLDER_PATH):
        
        for pkl in os.listdir(FOLDER_PATH):
            with open(f'{FOLDER_PATH}{pkl}', 'rb') as handle:
                next_cdf = pickle.load(handle)
            cdfs_completed.update(next_cdf.keys())
    else:
        Path(os.path.join(os.getcwd(), FOLDER_PATH)).mkdir()

    n = len(r_range)*len(eta_range)
    i = 0
    for r in r_range:
        r_cdf = dict()
        r = round_to_sigfigs(r, 3)
        for eta in eta_range:
            eta = round_to_sigfigs(eta, 3)
            if ((r, eta) in cdfs_completed):
                continue
            print(f'{(r, eta)}, {i} of {n}')
            i += 1
            r_cdf[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples,  n_tail = int(0.01*n_samples), tail_bound = 0.01, scipy_int=scipy_int)

        # Store pickle every outer loop iteration as its own file
        # CDFs/<optional_folder_name><number of samples>/<r>_<min(eta)>-<max(eta)>.pickle
        min_eta, max_eta = round_to_sigfigs(min(eta_range), 3), round_to_sigfigs(max(eta_range), 3)
        with open(f'{FOLDER_PATH}/{r}_{min_eta}-{max_eta}.pickle', 'wb') as handle:
            pickle.dump(r_cdf, handle)

# TODO:
# First, Test to see file directory set up is correct with num_points = 100
# Expected outcome: a new folder within CDFs is created with name 'test_not_mtlb_1000_0.2-0.8' 
# CDFs/<optional_folder_name><number of samples>/<r>_<min(eta)>-<max(eta)>.pickle containing two pickles (grouped by r)
# Run it a second time, and since the CDFs are already computed, it should not take any time to run
all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
all_r = np.arange(0.6, 5, 0.1)
num_points = 100
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='')

# Then, change USE_MATLAB to True and run below:
all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
all_r = np.arange(0.1, 0.7, 0.1)
num_points = 100000
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='mtlb')

if USE_MATLAB:
    eng.quit()
