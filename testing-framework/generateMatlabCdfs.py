import matlab.engine 
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from scipy import integrate, interpolate  
from scipy.stats import gengamma, laplace, norm, kstwo, ks_1samp
import matplotlib.pyplot as plt
import pickle
import os
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
    if cheby <= 99:
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
    return poly




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
            cdfs[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples,  n_tail = 100, tail_bound = 0.01, scipy_int=False)
        # Store pickle every outer loop iteration
        with open(f'CDFs/{pickle_name}.pickle', 'wb') as handle:
            pickle.dump(cdfs, handle)


def round_to_2_sigfigs(x):
    if x == 0:
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-1))



all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
#all_eta = np.append(np.arange(0.2, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
all_r = np.arange(0.2, 2, 0.1)
num_points = 10000

add_cdfs(f'cdfs_mtlb_{num_points}_{min(all_r)}-{max(all_r)}_{min(all_eta)}-{max(all_eta)}', all_r, all_eta, True, num_points)

eng.quit()
