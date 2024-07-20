from logging import raiseExceptions
from signal import raise_signal
import os
BRANDON = '/Users/brandonmarks/Desktop/Research Materials/hierarchical-bayesian-model-validation/'
YASH = '/Users/yashd/Desktop/hierarchical-bayesian-model-validation/'

ROOT_DIR = Brandon
os.chdir(ROOT_DIR + 'testing-framework/')

from utilities import *

USE_MATLAB = True

if USE_MATLAB:
    import matlab.engine 
    eng = matlab.engine.connect_matlab()
else:
    eng=None

# Yash is trying to do with MATLAB, n_samples=100000
# all_eta = np.arange(0, 4.1, 0.2) 
# all_r = np.arange(0.19, 0.1, -0.01)

# Brandon to do with MATLAB
all_eta = np.arange(0.1, 4.1, 0) 
all_r = np.arange(0.2, 0.1, -0.01)

num_points = 100000
# Note that I've changed add_cdfs so that n_samples is not automatically appended at the end inside the function
add_cdfs(r_range = all_r, eta_range = all_eta, 
         n_samples = num_points, scipy_int=(not USE_MATLAB), 
         folder_name=f'mtlb_{num_points}', debug=True, eng=eng,
         return_assert=True, enforce_assert=False)

if USE_MATLAB:
    eng.quit()
