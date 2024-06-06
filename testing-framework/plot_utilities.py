import numpy as np
import seaborn as sns
from scipy.stats import ks_1samp
import matplotlib.pyplot as plt
from utilities import *

def create_scatter_plot(df, metric=None, save_plot : bool = False):
    """
    Create a scatter plot, where the color of each point represents the value from the specified metric column.
    If metric=None, plot all the (r, eta) values in df.

    Arguments:
    df : A pandas DataFrame containing the columns 'r', 'eta', and the specified metric column.
    metric : The name of the column in the DataFrame to use for color mapping.
    """
    if metric:

        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot 1 (Linear eta)
        scatter = ax.scatter(df['r'], df['eta'], c=df[metric], cmap='viridis', alpha=1)
        ax.set_xlabel('r')
        ax.set_ylabel('eta')
        ax.set_title(f'(r, eta) pairs colored by {metric}')
        cbar = fig.colorbar(scatter, ax=ax)
        cbar.set_label(metric)
        #plt.grid(True)
        plt.show()

        if save_plot:
            fig.savefig(f'panoptic/plots/panoptic/plots/(r,eta){metric}_plot.png', dpi = 300, bbox_inches = 'tight')

    else:

        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot 1 (Linear eta)
        sns.scatterplot(x=df['r'], y=df['eta'], color='xkcd:shamrock green', alpha=1, ax=ax)
        ax.set_xlabel('r')
        ax.set_ylabel('eta')
        ax.set_title('(r, eta) pairs for which CDFs are computed (Linear eta)')
        #plt.grid(True)
        plt.show()

        if save_plot:
            fig.savefig(f'panoptic/plots/(r,eta)_plot.png', dpi = 300, bbox_inches = 'tight')


def create_scatter_plots(df, metric1 : str, metric2 : str, save_plot : bool = False):
    """
    Create two scatter plots side by side, where the color of each point in the first plot represents the value from the first specified metric column, and the color of each point in the second plot represents the value from the second specified metric column.

    Arguments:
    df : A pandas DataFrame containing the columns 'r', 'eta', and the specified metric columns.
    metric1 : The name of the column in the DataFrame to use for color mapping in the first plot.
    metric2 : The name of the column in the DataFrame to use for color mapping in the second plot.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot 1 (Linear eta, colored by metric1)
    scatter1 = ax1.scatter(df['r'], df['eta'], c=df[metric1], cmap='viridis', alpha=0.6)
    ax1.set_xlabel('r')
    ax1.set_ylabel('eta')
    ax1.set_title(f'(r, eta) pairs colored by {metric1}')
    cbar1 = fig.colorbar(scatter1, ax=ax1)
    cbar1.set_label(metric1)

    # Plot 2 (Linear eta, colored by metric2)
    scatter2 = ax2.scatter(df['r'], df['eta'], c=df[metric2], cmap='viridis', alpha=0.6)
    ax2.set_xlabel('r')
    ax2.set_ylabel('eta')
    ax2.set_title(f'(r, eta) pairs colored by {metric2}')
    cbar2 = fig.colorbar(scatter2, ax=ax2)
    cbar2.set_label(metric2)

    plt.subplots_adjust(wspace=0.3)
    plt.show()

    if save_plot:
        fig.savefig(f'panoptic/plots/panoptic/plots/(r,eta){metric1}_and_{metric2}_plot.png', dpi = 300, bbox_inches = 'tight')

def create_scatter_plots_log_eta(df, metric=None, save_plot : bool = False):
    """
    Create two scatter plots side by side, where the color of each point represents the value from the specified metric column.
    
    Arguments:
    df -- A pandas DataFrame containing the columns 'r', 'eta', and the specified metric column.
    metric -- The name of the column in the DataFrame to use for color mapping.
    """
    if metric:
    
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

        if save_plot:
            fig.savefig(f'panoptic/plots/(r,eta)_plot_with_log_eta.png', dpi = 300, bbox_inches = 'tight')
    
    else:
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Plot 1 (Linear eta)
        sns.scatterplot(x=df['r'], y=df['eta'], color='xkcd:shamrock green', alpha=0.4, ax=ax1)
        ax1.set_xlabel('r')
        ax1.set_ylabel('eta')
        ax1.set_title('(r, eta) pairs for which CDFs are computed (Linear eta)')

        # Plot 2 (Geometric eta)
        mask = df['eta'].isin(10**np.arange(-9.0, 0))
        sns.scatterplot(x=df['r'], y=np.log10(df[mask]['eta']), color='xkcd:shamrock green', alpha=0.4, ax=ax2)
        ax2.set_xlabel('r')
        ax2.set_ylabel(f'log10 eta')
        ax2.set_title('(r, eta) pairs for which CDFs are computed (Geometric eta)')

        plt.subplots_adjust(wspace=0.3)
        plt.show()

def create_contour_plot(df, metric):
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
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    heatmap = ax.imshow(metric_meshgrid, extent=[df['r'].min(), df['r'].max(), df['eta'].min(), df['eta'].max()], origin='lower', cmap='viridis', alpha=0.5)
    
    #contour = ax.contour(r_meshgrid, eta_meshgrid, metric_meshgrid, cmap='viridis')
    cbar = fig.colorbar(heatmap, ax=ax)
    cbar.set_label(metric)
    
    #ax.clabel(contour, inline=True, fontsize=10)
    ax.set_xlabel('r')
    ax.set_ylabel('eta')
    ax.set_title('Contour Plot (r, eta) colored by {}'.format(metric))
    
    plt.show()

def visualize_cdf(obs_x, r, eta, n_samples = 1000, all_cdfs = None, layer = None):
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
    if all_cdfs and (r, eta) in all_cdfs:
        null_cdf = all_cdfs[(r, eta)]
    else:
        null_cdf = compute_prior_cdf(r = r, eta = eta, n_samples = n_samples)
    plt.plot(obs_x, np.arange(1, n+1)/n, label='Empirical CDF')
    plt.plot(xs, null_cdf(xs), label='True CDF')
    result = ks_1samp(obs_x, null_cdf)
    distance = result.statistic
    location = result.statistic_location
    emp_cdf_at_loc = np.searchsorted(obs_x, location, side='right') / n
    true_cdf_at_loc = null_cdf(location)
    plt.vlines(location, emp_cdf_at_loc, true_cdf_at_loc, linestyles='--', label=f'Maximum Deviation: {np.round(distance, 6)} \n at x={np.round(location, 3)}', color = 'xkcd:bright red')
    if layer:
        plt.title(f'Layer {layer} Empirical CDF vs True CDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
    else:
        plt.title(f'Empirical CDF vs True CDF (r={r}, eta={eta}) \n with p-value:{np.round(result.pvalue, 8)}')
    plt.legend()
    plt.show()

    return distance, location

def visualize_pdf(obs_x, r, eta, layer=None):
    xs, pdf = compute_prior_pdf(r, eta)
    plt.plot(xs, pdf, label = 'True CDF')
    sns.kdeplot(sample, label = 'Empirical CDF (KDE)')
    if layer:
        plt.title(f'Layer {layer} Empirical PDF vs True PDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
    else:
        plt.title(f'Empirical PDF vs True PDF (r={r}, eta={eta}) \n with p-value:{np.round(result.pvalue, 8)}')
    plt.legend()

def visualize_cdf_pdf(obs_x, params, distro = 'gengamma', n_samples=10000, all_cdfs=None, layer=None):
    """
    Visualize the gap between the empirical CDF/PDF and the true CDF/PDF.

    Args:
        obs_x (np.ndarray): Observed data.
        r (float): r value.
        eta (float): eta value.
        n_samples (int): Number of samples for the true CDF/PDF.
        all_cdfs (dict): Dictionary containing true CDFs.
        layer (int or None): Layer index (for titling purposes).

    Returns:
        distance (float): The Kolmogorov-Smirnov statistic.
        location (float): The location of the maximum deviation between the empirical and true CDFs.
    """
    xs = np.linspace(np.min(obs_x), np.max(obs_x), 10000)
    obs_x = np.sort(obs_x)
    n = len(obs_x)
    
    if distro == 'gengamma':
        r = params[0]
        eta = params[1]
        if all_cdfs and (r, eta) in all_cdfs:
            null_cdf = all_cdfs[(r, eta)]
        else:
            null_cdf = compute_prior_cdf(r=r, eta=eta, n_samples=n_samples)
    elif distro == 'gaussian' or distro == 'normal':
        null_cdf = stats.norm(scale=params).cdf
    elif distro == 'laplace':
        null_cdf = stats.laplace(scale=params).cdf

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Empirical CDF vs True CDF
    ax1.plot(obs_x, np.arange(1, n+1)/n, label='Empirical CDF')
    ax1.plot(xs, null_cdf(xs), label='True CDF')
    result = ks_1samp(obs_x, null_cdf)
    distance = result.statistic
    location = result.statistic_location
    emp_cdf_at_loc = np.searchsorted(obs_x, location, side='right') / n
    true_cdf_at_loc = null_cdf(location)
    ax1.vlines(location, emp_cdf_at_loc, true_cdf_at_loc, linestyles='--', label=f'Maximum Deviation: {np.round(distance, 6)}\nat x={np.round(location, 6)}', color='xkcd:bright red')
    if layer:
        ax1.set_title(f'Layer {layer} Empirical CDF vs True CDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
    else:
        ax1.set_title(f'Empirical CDF vs True CDF (r={r}, eta={eta}) \n with p-value:{np.round(result.pvalue, 8)}')
    ax1.legend()

    # Empirical PDF vs True PDF
    xs_pdf, true_pdf = compute_prior_pdf(r, eta)
    sns.kdeplot(obs_x, ax=ax2, label='Empirical PDF (KDE)')
    ax2.plot(xs_pdf, true_pdf, label='True PDF')
    if layer:
        ax2.set_title(f'Layer {layer} Empirical PDF vs True PDF \n (r={r}, eta={eta})')
    else:
        ax2.set_title(f'Empirical PDF vs True PDF (r={r}, eta={eta})')
    ax2.legend()

    plt.tight_layout()
    plt.show()

    return distance, location