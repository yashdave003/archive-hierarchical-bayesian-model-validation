import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from scipy import integrate, interpolate  
from scipy.stats import gengamma, laplace, norm, kstwo, ks_1samp
import matplotlib.pyplot as plt
import pickle
import os

def compute_prior_pdf(r, eta, n_samples = 10000, tail_bound = 0.05, n_tail = 5, scale = 1):

    '''
    Returns support and pdf for prior distribution
    r : shape parameter controlling rate of exponentional decay
    eta : controls roundedness of peak, and hence sparsity
    scale : scale parameter
    n_samples : number of points used to numerically approximate CDF
    tail_bound : Uses Chebyshev's Inequality to bound the region of the CDF that is outside the coverage of xs
    n_tail : Sets the number of points tha lie outside the coverage of xs to approximate tails if need be

    Usage:
    new_pdf = compute_prior_cdf(r = 0.1, eta = 0.001)
    new_pdf(0.5343) returns CDF
    Can also accept arrays
    '''
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 1/2)/r)/scipy.special.gamma(beta)
    x_max = min(100, np.round(var_prior/tail_bound)) # introduced additional bound in case chebyshev is unwieldy
    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(np.linspace(-(x_max+100), -(x_max+20), n_tail), xs)
    xs = np.append(xs, np.linspace(x_max + 20, x_max + 100, n_tail))
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
        prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
    return xs, prior_pdf

def compute_prior_cdf(r, eta, n_samples = 1000, tail_bound = 0.05, n_tail = 5, scale = 1):

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
    var_prior = scale * scipy.special.gamma((eta + 1.5 + 1/2)/r)/scipy.special.gamma(beta)
    x_max = min(100, np.round(var_prior/tail_bound)) # introduced additional bound in case chebyshev is unwieldy
    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(np.linspace(-(x_max+100), -(x_max+20), n_tail), xs)
    xs = np.append(xs, np.linspace(x_max + 20, x_max + 100, n_tail))
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
        prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]

    prior_cdf = np.zeros_like(prior_pdf)
    for i in range(len(xs) - 1):
        prior_cdf[i] = np.trapz(prior_pdf[:i+1], xs[:i+1]) 
    prior_cdf = np.append(prior_cdf[:-1], 1)

    poly = interpolate.CubicSpline(x = xs, y = prior_cdf)
    return poly

def sample_prior(r, eta, size=1):
    '''
    Samples from prior distribution of signal x
    r : shape parameter, must be > 0
    eta : shape parameter, controls roundedness of peak
    size : integer specifying number of samples required
    '''
    vars = gengamma.rvs(a = (eta + 1.5)/r, c = r, size = size)
    x = np.random.normal(scale = vars, size=size)
    return x

def sample_laplace(size=1):
    '''
    Samples from laplace distribution
    size : integer specifying number of samples required
    '''
    return laplace.rvs(size = size)

def cartesian_product(*arrays):
    " Credits: https://stackoverflow.com/a/11146645"
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def round_to_2_sigfigs(x):
    if x == 0:
        return 0
    return np.round(x, -int(np.floor(np.log10(abs(x)))-1))

def add_cdfs(pickle_name, r_range, eta_range, check_redundant = False, n_samples = 10000):
    '''
    pickle_name: Name of pickle file that stores dictionary of cdfs, does not include the '.pickle'
    r_range: range of r values, assumes use of np.arange
    eta_range: range of eta values, assumes use of np.arange 
    check_redundant: if True, checks if key already exists in dictionary 
    n_samples: number of samples used when computing prior_cdf
    '''
    if os.path.isfile(pickle_name+'.pickle'):
        with open(f'{pickle_name}.pickle', 'rb') as handle:
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
            cdfs[(r, eta)] = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples)

        # Store pickle every outer loop iteration
        with open(f'{pickle_name}.pickle', 'wb') as handle:
            pickle.dump(cdfs, handle, protocol=pickle.HIGHEST_PROTOCOL) 

def plot_cdf(cdf):
    if type(cdf) == np.ndarray:
        plt.plot(np.arange(0, len(cdf))/len(cdf), cdf)
    else:
        if cdf(-0.1) > 0:
            xs = np.linspace(-100, 100, 10000)
        elif cdf(2) == 1:
            xs = np.linspace(0, 2, 1000)
        else:
            xs = np.linspace(0, 100, 10000)
        plt.plot(xs, cdf(xs))
    plt.title('CDF')
    plt.xlabel('x')
    plt.ylabel('P(x<=k)')

def extract_single_dist(all_dist_df, base_r, base_eta):
    return all_dist_df[(all_dist_df['base_r'] == base_r) & (all_dist_df['base_eta'] == base_eta)].drop(['base_r', 'base_eta'], axis = 1)

def kstest_custom(x, cdf, return_loc = False):
    n = len(x)
    x = np.sort(x)
    cdfvals = cdf(x)
    dplus, dminus = (np.arange(1.0, n + 1) / n - cdfvals), (cdfvals - np.arange(0.0, n)/n)
    plus_amax, minus_amax = dplus.argmax(), dminus.argmax()
    loc_max, loc_min = x[plus_amax], x[minus_amax]
    d = max(dplus[plus_amax], dminus[minus_amax])
    if return_loc:
        if d == plus_amax:
            return loc_max
        else:
            return loc_min
    return d, kstwo.sf(d, n)

def create_scatter_plots(df, metric):
    """
    Create two scatter plots side by side, where the color of each point represents the value from the specified metric column.
    
    Arguments:
    df -- A pandas DataFrame containing the columns 'r', 'eta', and the specified metric column.
    metric -- The name of the column in the DataFrame to use for color mapping.
    """
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot 1 (Linear eta)
    scatter1 = ax1.scatter(df['r'], df['eta'], c=df[metric], cmap='viridis', alpha=0.8)
    ax1.set_xlabel('r')
    ax1.set_ylabel('eta')
    ax1.set_title('(r, eta) pairs colored by {}'.format(metric))

    cbar1 = fig.colorbar(scatter1, ax=ax1)
    cbar1.set_label(metric)
    
    # Plot 2 (Geometric eta)
    mask = df['eta'].isin(10**np.arange(-9.0, 0))
    scatter2 = ax2.scatter(df[mask]['r'], np.log10(df[mask]['eta']), c=df[mask][metric], cmap='viridis', alpha=0.8)
    ax2.set_xlabel('r')
    ax2.set_ylabel('eta')
    ax2.set_title('(r, eta) pairs colored by {} (Geometric eta)'.format(metric))

    cbar2 = fig.colorbar(scatter2, ax=ax2)
    cbar2.set_label(metric)

    plt.subplots_adjust(wspace=0.3)
    plt.show()

def rename_cols(df):
    return df.replace({'Orientation' : {'Horizontal detail' : 'H', 'Vertical detail' : 'V', 'Diagonal detail' : 'D'}})

def make_layer_df(data_dict, layer, all_cdfs, all_cdfs_df, only_diag = False):
    # Assumes all_cdfs_df and all_cdfs dict exist
    layer = rename_cols(data_dict[layer])
    if only_diag:
        ornt = ['D']
    else:
        ornt = ['H', 'V']
    x = np.array([np.concatenate(layer[layer["Orientation"] == direction]["Flattened Data"].values.flatten()) for direction in ornt]).flatten()
    obs_x = np.sort(x)
    print(f"Number of samples: {x.shape[0]}")
    df = all_cdfs_df.copy()
    kstest_stat_pval = all_cdfs_df.apply(lambda row : kstest_custom(obs_x, all_cdfs[(row.iloc[1], row.iloc[2])]), axis = 1)
    df['kstest_stat'] = kstest_stat_pval.str[0]
    df['kstest_pval'] = kstest_stat_pval.str[1]
    return df, obs_x

def visualize_cdfs(obs_x, r, eta, all_cdfs):
    """
    Visualize the gap between the empirical CDF and the true CDF.
    
    Args:
        obs_x (np.ndarray): Observed data.
        r (float): r value.
        eta (float): eta value.
        all_cdfs (dict): Dictionary containing true CDFs.
        
    Returns:
        distance (float): The Kolmogorov-Smirnov statistic.
        location (float): The location of the maximum deviation between the empirical and true CDFs.
    """
    xs = np.linspace(np.min(obs_x), np.max(obs_x), 10000)
    obs_x = np.sort(obs_x)
    n = len(obs_x)
   
    null_cdf = all_cdfs[(r, eta)]

    plt.plot(obs_x, np.arange(1, n+1)/n, label='Empirical CDF')
    plt.plot(xs, null_cdf(xs), label='True CDF')
    result = ks_1samp(obs_x, null_cdf)
    distance = result.statistic
    location = result.statistic_location
    emp_cdf_at_loc = np.searchsorted(obs_x, location, side='right') / n
    true_cdf_at_loc = null_cdf(location)
    plt.vlines(location, emp_cdf_at_loc, true_cdf_at_loc, linestyles='--', label=f'Maximum Deviation: {np.round(distance, 2)}')
    
    plt.title(f'Empirical CDF vs True CDF (r={r}, eta={eta}) \n with p-value:{np.round(result.pvalue, 5)}')
    plt.legend()
    plt.show()
    
    return distance, location

def create_contour_plot(df, metric, log_eta = False):
    """
    Create a contour plot with a semi-transparent heatmap in the background, where the color represents the values from the specified metric column.
    
    Arguments:
    df -- A pandas DataFrame containing the columns 'r', 'eta', and the specified metric column.
    metric -- The name of the column in the DataFrame to use for color mapping.
    """
    
    # Create a meshgrid from r and eta
    r_meshgrid, eta_meshgrid = np.meshgrid(df['r'].unique(), df['eta'].unique())
    
    metric_meshgrid = np.zeros_like(r_meshgrid)
    for i, r in enumerate(df['r'].unique()):
        for j, eta in enumerate(df['eta'].unique()):
            mask = (df['r'] == r) & (df['eta'] == eta)
            if mask.any():
                metric_meshgrid[j, i] = df.loc[mask, metric].values[0]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    heatmap = ax.imshow(metric_meshgrid, extent=[df['r'].min(), df['r'].max(), df['eta'].min(), df['eta'].max()], origin='lower', cmap='viridis', alpha=0.5)
    
    contour = ax.contour(r_meshgrid, eta_meshgrid, metric_meshgrid, cmap='viridis')
    cbar = fig.colorbar(heatmap, ax=ax)
    cbar.set_label(metric)
    
    ax.clabel(contour, inline=True, fontsize=10)
    ax.set_xlabel('r')
    ax.set_ylabel('eta')
    ax.set_title('Contour Plot (r, eta) colored by {}'.format(metric))
    
    plt.show()


        