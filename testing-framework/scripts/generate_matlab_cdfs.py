from logging import raiseExceptions
from signal import raise_signal
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
from numba import njit, prange

USE_MATLAB = False

if USE_MATLAB:
    import matlab.engine 
    eng = matlab.engine.connect_matlab()

print("RUN FROM hierarchical-bayesian-model-validation/testing-framework directory")

def compute_prior_cdf(r, eta, n_samples = 1000, tail_bound = 0.05, tail_percent = 0.01, scale = 1, scipy_int=True, support = False):

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

    print(poly(-1e10), poly(1e10))

    if support:
        return xs, poly
    else:
        return poly

def round_to_sigfigs(x, num_sigfigs=2):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-(num_sigfigs-1)))

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

    # Note the FOLDER_PATH
    #FOLDER_PATH = f'testing-framework\\CDFs\\{folder_name}{n_samples}\\'
    FOLDER_PATH = os.path.join("CDFs", folder_name+str(n_samples))
    cdfs_completed = set()
    if os.path.isdir(FOLDER_PATH):
        print(FOLDER_PATH)    
        for pkl in os.listdir(FOLDER_PATH):
            #with open(f'{FOLDER_PATH}{pkl}', 'rb') as handle:
            with open(os.path.join(FOLDER_PATH, pkl), 'rb') as handle:
                next_cdf = pickle.load(handle)
            cdfs_completed.update(next_cdf.keys())
    else:
        Path(os.path.join(os.getcwd(), FOLDER_PATH)).mkdir()
    print("CDFs completed:", len(cdfs_completed))
    n = len(r_range)*len(eta_range)


    cnt = 0
    grouped_r_cdf = dict()
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
        min_eta, max_eta = round_to_sigfigs(min(eta_range), 6), round_to_sigfigs(max(eta_range), 6)
        if len(eta_range) > 1:
            with open(os.path.join(FOLDER_PATH,f'{r}_{min_eta}-{max_eta}.pickle'), 'wb') as handle:
                pickle.dump(r_cdf, handle)
        else:
            grouped_r_cdf = grouped_r_cdf | r_cdf
    with open(os.path.join(FOLDER_PATH,f'{round_to_sigfigs(r_range[0], 6)}-{round_to_sigfigs(r_range[-1], 6)}_{min_eta}.pickle'), 'wb') as handle:
            pickle.dump(grouped_r_cdf, handle)

        # elif cnt % 10 == 9 or cnt == len(r_range): # Store every 10 CDFs computed
        #     grouped_r_cdf = grouped_r_cdf | r_cdf
        #     with open(os.path.join(FOLDER_PATH,f'{round_to_sigfigs(r_range[cnt-9], 6)}-{round_to_sigfigs(r_range[cnt], 6)}_{min_eta}.pickle'), 'wb') as handle:
        #         pickle.dump(grouped_r_cdf, handle)

    print(f'You can find the CDFs here: {os.path.join(os.getcwd(), FOLDER_PATH)}')

# TODO:
# # First, Test to see file directory set up is correct with num_points = 100
# # Expected outcome: a new folder within CDFs is created with name 'test_not_mtlb_100_0.2-0.8' 
# # CDFs/<optional_folder_name><number of samples>/<r>_<min(eta)>-<max(eta)>.pickle containing two pickles (grouped by r)
# # Run it a second time, and since the CDFs are already computed, it should not take any time to run

# # First TEST
# all_eta = np.append(np.arange(0, 4, 0.1), np.array([np.float_power(10, i) for i in range(-9, -1)]))
# all_r = np.arange(0.6, 0.7, 0.1)
# num_points = 1000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='test_')

# # # Then, change USE_MATLAB to True at the top of the notebook and run below:

os.chdir(os.path.join(os.getcwd(), "testing-framework"))

all_eta = np.append(np.arange(0.1, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
# all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-3, -1)]))
all_r = np.arange(0.7, 2, 0.1)
num_points = 10000
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='scipy_')

############################################################

# LAYER 2
# all_r = np.arange(0.6020, 0.6030, 0.0001)
# all_eta = np.arange(3.20, 3.21, 0.01)
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer2_')

# LAYER 3
# all_r = np.arange(0.7040, 0.7060, 0.0001)
# all_eta = np.array([3.63]) #np.arange(3.63, 3.64, 0.01)
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer3_')

# # LAYER 4
# all_r = np.arange(0.780, 0.800, 0.001)
# all_eta = [0.24] # np.arange(2.9, 3.1, 0.01)
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer4_')

# LAYER 5
all_r = np.arange(0.9030, 0.9050, 0.0001)
all_eta =  [1.62] #np.arange(1.55, 1.65, 0.01)
num_points = 10000
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer5_')

# # LAYER 6
# all_r = np.arange(1.020, 1.040, 0.001)
# all_eta = [0.33] # np.arange(0.33, 0.34, 0.01)
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer6_')

# # LAYER 7
# all_r = np.arange(4.6280, 4.630, 0.0001)
# all_eta = [0] # np.append(np.logspace(-6, -1, 1, base = 10), np.arange(0, 4, 0.1))
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer7_')

# # LAYER 8
# all_r = np.arange(5.690, 5.710, 0.001)
# all_eta = [0] # np.append(np.logspace(-6, -1, 1, base = 10), np.arange(0, 4, 0.1))
# num_points = 10000
# add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='layer8_')

if USE_MATLAB:
    eng.quit()
