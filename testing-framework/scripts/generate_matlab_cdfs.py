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

def pdf_to_cdf(xs, prior_pdf, enforce_assert=True, debug = False):
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


def compute_prior_cdf(r, eta, n_samples=10000, tail_bound=0.05, tail_percent=0.01, scale=1, scipy_int=True, eng=None, enforce_assert=True, return_pdf=False, debug=False):
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

    xs, prior_pdf = compute_prior_pdf(r, eta, n_samples, tail_bound, tail_percent, scale, scipy_int, eng, debug)
    cdf_spline = pdf_to_cdf(xs, prior_pdf, enforce_assert, debug)

    if return_pdf:
        return xs, prior_pdf, cdf_spline
    else:
        return cdf_spline


def round_to_sigfigs(x, num_sigfigs=2):
    if x == np.zeros_like(x):
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-(num_sigfigs-1)))

def load_pkl(path):
    if os.path.isfile(path):
        with open(path, 'rb') as handle:
            obj = pickle.load(handle)
        return object
    else:
        raise Exception("File does not exist, check the path again")
    
def dump_dict_pkl(obj, path, overwrite = False):
    if not overwrite:
        if os.path.isfile(path):
            with open(path, 'rb') as handle:
                existing_object = pickle.load(handle)
            obj = obj | existing_object
            with open(path, 'wb') as handle:
                pickle.dump(obj, handle)
            print("merged")
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle)
    else:
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle)

def add_cdfs(r_range, eta_range, n_samples, scipy_int=True, folder_name='', debug = False, eng=None):
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
            r_cdf[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples,  tail_percent = 0.01, tail_bound = 0.01, scipy_int=scipy_int, eng=eng)

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
  
os.chdir(os.path.join(os.getcwd(), "testing-framework"))

all_eta = np.arange(0.1, 4.1, 0.1) 
all_r = np.arange(0.2, 1, 0.05)
num_points = 10000
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='mtlb_', debug=True)

if USE_MATLAB:
    eng.quit()
