from logging import raiseExceptions
from signal import raise_signal
import os
BRANDON = '/Users/brandonmarks/Desktop/Research Materials/hierarchical-bayesian-model-validation/'
YASH = '/Users/yashd/Desktop/hierarchical-bayesian-model-validation/'

ROOT_DIR = BRANDON
os.chdir(ROOT_DIR + 'testing-framework/')

from utilities import *

USE_MATLAB = True

if USE_MATLAB:
    import matlab.engine 
    eng = matlab.engine.connect_matlab()
else:
    eng=None


def simple_add_cdfs(r_range, eta_range, folder_name = '', n_samples = 2000, tail_bound = 0.01, tail_percent = 0.1, use_matlab=False, eng= None, enforce_assert=True, return_assert = False, debug=False):

    if not os.path.isdir("CDFs"):
        raise Exception("This Directory Does Not Contain CDFs")
    
    if folder_name == '':
        folder_name = f'r{round_to_sigfigs(min(r_range))}to{round_to_sigfigs(max(r_range))}_eta{round_to_sigfigs(min(eta_range))}to{round_to_sigfigs(max(eta_range))}'

    FOLDER_PATH = os.path.join("CDFs", folder_name)

    if os.path.isdir(FOLDER_PATH):
        cdfs_completed = combine_pickles(folder_name)
        if debug:
            print("CDFs completed:", len(cdfs_completed))
    else:
        Path(os.path.join(os.getcwd(), FOLDER_PATH)).mkdir()
        cdfs_completed = dict()

    n = len(r_range)*len(eta_range)

    cnt = len(cdfs_completed)
    for r in r_range:
        r_cdf = dict()
        r = round_to_sigfigs(r)
        for eta in eta_range:
            eta = round_to_sigfigs(eta)
            if ((r, eta) in cdfs_completed) and cdfs_completed[(r, eta)]:
                continue
            cnt += 1
            if debug:
                print(f'{(r, eta)}, {cnt} of {n}')
  
            computed_cdf = compute_prior_cdf(r = r, eta = eta, method = 'gamma_cdf', n_samples = n_samples, tail_percent = tail_percent, tail_bound = tail_bound, 
                                             use_matlab=use_matlab, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, debug=debug)
            if computed_cdf is None:
                with open("generate_CDF_log_brandon.csv", 'a') as handle:
                    handle.write(f"{r}, {eta}, {n_samples}, failed assert\n")
                continue
            r_cdf[(r, eta)] = computed_cdf
        if r_cdf:
            sorted_r_cdf = [i[1] for i in sorted(r_cdf)]
            min_eta, max_eta = round_to_sigfigs(eta_range[0], 6), round_to_sigfigs(max(sorted_r_cdf), 6)
            pkl_path = os.path.join(FOLDER_PATH, f'r{r}_eta{min_eta}-{max_eta}.pickle')
            pd.to_pickle(r_cdf, pkl_path)
        else:
            print(f"Skipped {r} entirely")

    if debug:
        print(f'You can find the CDFs here: {os.path.join(os.getcwd(), FOLDER_PATH)}')

# 2. 
all_eta = np.arange(0,10,0.1)
all_r = np.arange(2, 5, 0.01)
n_samples = 1000
tail_percent = 0.1
tail_bound = 0.01

# 1. log_eta eta=10^-1 to 10^-9 with spacing of 10^-2, r = 0.1 to 8, 0.1 (Yash)
# 2a. r=lowest to 0.1, spacing 0.01; eta 0 to 5, 0.1; tail_bound= 0.00001, n_samples=5000
# 2b. r=0.1 to 0.2, spacing 0.01; eta 0 to 5, 0.1; tail_bound= 0.0001, n_samples=5000  
# 3. r=0.2 to 2, spacing 0.01; eta = 0 to 5, 0.1; tail_bound=0.001, n_samples=2000
# 4. r=2 to 5, spacing 0.01, eta = 0 to 10, 0.1, tail_bound=0.01, n_samples=1000
# 5. r=5 to 10, spacing 0.1, eta = 0 to 10, 0.1, tail_bound=0.01, n_samples=1000 (Yash)
# 6. r=10 to 50, spacing 1, eta = 0 to 10, 1, tail_bound=0.01, n_samples=1000 (Yash)

simple_add_cdfs(all_r, all_eta, n_samples = n_samples, folder_name='',
                tail_percent = tail_percent, tail_bound = tail_bound, use_matlab=USE_MATLAB, 
                eng=eng, enforce_assert=False, return_assert=True, debug=True)

if USE_MATLAB:
    eng.quit()
