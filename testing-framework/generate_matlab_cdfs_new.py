from logging import raiseExceptions
from signal import raise_signal
import os
BRANDON = '/Users/brandonmarks/Desktop/Research Materials/hierarchical-bayesian-model-validation/'
YASH = '/Users/yashd/Desktop/hierarchical-bayesian-model-validation/'

ROOT_DIR = YASH
os.chdir(ROOT_DIR + 'testing-framework/')

from utilities import *

USE_MATLAB = False

if USE_MATLAB:
    import matlab.engine 
    eng = matlab.engine.connect_matlab()
else:
    eng=None

# DONE WITH MATLAB in mtlb_10000
# all_eta = np.arange(0.1, 4.1, 0.1) 
# all_r = np.arange(1, 1.5, 0.05)

# Yash is doing
# all_eta = np.arange(0, 4.1, 0.2) 
# all_r = np.arange(1.6, 4, 0.1)

# Brandon to do
all_eta = np.arange(0, 4.1, 0.2) 
all_r = np.arange(4, 8, 0.1)

num_points = 10000
add_cdfs(r_range = all_r, eta_range = all_eta, n_samples = num_points, scipy_int=(not USE_MATLAB), folder_name='scipy_', debug=True, eng=eng)

if USE_MATLAB:
    eng.quit()
