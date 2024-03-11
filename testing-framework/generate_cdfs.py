from utilities import *
all_eta = np.append(np.arange(0, 3, 0.25), np.array([np.float_power(10, i) for i in range(-6, -1)]))
all_r = np.arange(0.25, 3, 0.25)
add_cdfs('cdfs_lite', all_r, all_eta, True, 1000)