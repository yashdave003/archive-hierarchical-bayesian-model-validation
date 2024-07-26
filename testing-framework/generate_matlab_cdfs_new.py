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

# Part 1: 0.14-0.17, num_points = 120000 (and increments of 20000 if need be); folder_name=f'mtlb_014to017_r' (Brandon)
all_eta = np.arange(0.1, 4.1, 0.2) 
all_r = np.arange(0.2, 0.13, -0.01)

# Part 2, 0.14-0.17, num_points = 120000 (and increments of 20000 if need be); folder_name=f'mtlb_014to017_r' (Brandon)
all_eta = np.arange(0, 4.1, 0.2) 
all_r = np.arange(0.2, 0.13, -0.01)

# Part 3: Expanding eta to include a broader space, num_points = 10000; folder_name=f'mtlb_4to8_eta' (Yash)
all_eta = np.arange(4, 8.1, 1) 
all_r = np.append(np.arange(0.2, 4, 0.1), np.arange(4, 8, 1))

# Part 4: Expanding eta to include a broader space, num_points = 10000; folder_name=f'mtlb_8to20_eta' (Yash)
all_eta = np.arange(8, 20.1, 2) 
all_r = np.append(np.arange(0.2, 4, 0.1), np.arange(4, 8, 1))

num_points = 120000
# remember to change folder_name and num_points before running)
add_cdfs(r_range = all_r, eta_range = all_eta, 
         n_samples = num_points, scipy_int=(not USE_MATLAB), 
         folder_name=f'mtlb_{num_points}', debug=True, eng=eng,
         return_assert=True, enforce_assert=False)

if USE_MATLAB:
    eng.quit()
