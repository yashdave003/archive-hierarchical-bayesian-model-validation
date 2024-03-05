from utilities import *
all_eta = np.append(np.arange(0, 4, 0.2), np.array([np.float_power(10, i) for i in range(-9, -1)]))
all_r = np.arange(0.7, 3, 0.1)
add_cdfs('updated_100000', all_r, all_eta, True, 100000)