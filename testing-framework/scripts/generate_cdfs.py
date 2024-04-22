# cdfs lite
from utilities import *
# all_eta = np.append(np.arange(0, 3, 0.25), np.array([np.float_power(10, i) for i in range(-6, -1)]))
# all_r = np.arange(0.25, 3, 0.25)
# # updated_1000000 ranges
all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
all_r = np.arange(3, 9, 0.4)
num_points = 100000
add_cdfs(f'updated_{num_points}_{min(all_r)}-{max(all_r)}', all_r, all_eta, True, num_points)
