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

# # Yash has DONE with scipy
# all_eta = np.arange(0, 4.1, 0.1) 
# all_r = np.arange(1.5, 8, 0.1)

# Brandon TO DO with matlab
all_eta = np.arange(0, 4.1, 0.1) 
all_r = np.arange(0.99, 1.5, 0.01)

# # Yash wants to do with scipy
# all_eta = np.arange(0, 4.1, 0.1) 
# all_r = np.arange(1.5, 3, 0.01)

num_points = 10000
add_cdfs(r_range = all_r, eta_range = all_eta, 
         n_samples = num_points, scipy_int=(not USE_MATLAB), 
         folder_name='mtlb_', debug=True, eng=eng,
         return_assert=True, enforce_assert=False)

if USE_MATLAB:
    eng.quit()
