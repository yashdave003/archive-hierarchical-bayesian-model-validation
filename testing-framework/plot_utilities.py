import seaborn as sns
import matplotlib.pyplot as plt
from utilities import *

GROUP_NAME = 'Layer'

def create_scatter_plot(df, metric=None):
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
        plt.grid(which='both')
        plt.show()

    else:

        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot 1 (Linear eta)
        sns.scatterplot(x=df['r'], y=df['eta'], color='xkcd:shamrock green', alpha=1, ax=ax)
        ax.set_xlabel('r')
        ax.set_ylabel('eta')
        ax.set_title('(r, eta) pairs for which CDFs are computed (Linear eta)')
        plt.grid(which='both')
        plt.show()

    return fig


def create_scatter_plots(df, metric1, metric2):
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
    plt.grid(True)
    ax1.set_xlabel('r')
    ax1.set_ylabel('eta')
    ax1.set_title(f'(r, eta) pairs colored by {metric1}')
    cbar1 = fig.colorbar(scatter1, ax=ax1)
    cbar1.set_label(metric1)
    

    # Plot 2 (Linear eta, colored by metric2)
    scatter2 = ax2.scatter(df['r'], df['eta'], c=df[metric2], cmap='viridis', alpha=0.6)
    plt.grid(True)
    ax2.set_xlabel('r')
    ax2.set_ylabel('eta')
    ax2.set_title(f'(r, eta) pairs colored by {metric2}')
    cbar2 = fig.colorbar(scatter2, ax=ax2)
    cbar2.set_label(metric2)
    

    plt.subplots_adjust(wspace=0.3)
    plt.show()

    return fig

def create_scatter_plots_log_eta(df, metric=None):
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

    return fig

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
    
    contour = ax.contour(r_meshgrid, eta_meshgrid, metric_meshgrid, cmap='viridis')
    cbar = fig.colorbar(heatmap, ax=ax)
    cbar.set_label(metric)
    
    ax.clabel(contour, inline=True, fontsize=10)
    ax.set_xlabel('r')
    ax.set_ylabel('eta')
    ax.set_title('Contour Plot (r, eta) colored by {}'.format(metric))
    
    plt.show()

    return fig

def visualize_cdf(sample, params, distro='gengamma', n_samples=10000, interval=None, provided_loc=None, all_cdfs=None, group=None):
    """
    Visualize the gap between the empirical CDF and the computed CDF.

    Args:
        sample (np.ndarray): Observed data.
        params (tuple): Parameters for the computed CDF.
        distro (str): Distribution to use for the computed CDF ('gengamma', 'gaussian', or 'laplace').
        n_samples (int): Number of samples for the computed CDF.
        interval (tuple): Optional interval for the x-axis limits.
        provided_loc (float): Optional location to compute the deviation at.
        all_cdfs (dict): Dictionary containing computed CDFs.
        group (int or None): Group index (for titling purposes).

    Returns:
        fig (matplotlib.figure.Figure): The figure object containing the plot.
    """
    xs = np.linspace(max(np.min(sample), -5000), min(np.max(sample), 5000), 10000)
    sample = np.sort(sample)
    n = len(sample)

    if distro == 'gengamma':
        r, eta = params
        if all_cdfs and (r, eta) in all_cdfs:
            null_cdf = all_cdfs[(r, eta)]
        else:
            null_cdf = compute_prior_cdf(r, eta, n_samples)
    elif distro == 'gaussian' or distro == 'normal':
        null_cdf = stats.norm(scale=params).cdf
    elif distro == 'laplace':
        null_cdf = stats.laplace(scale=params).cdf
    elif distro == 't':
        null_cdf = stats.t(df=params[0], scale = params[1]).cdf

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_xlim(left=-25, right=25)
    if interval:
        ax.set_xlim(left=interval[0], right=interval[1])

    ax.plot(sample, np.arange(1, n+1)/n, label='Empirical CDF')
    ax.plot(xs, null_cdf(xs), label='Computed CDF')

    result = stats.ks_1samp(sample, null_cdf)
    distance = result.statistic
    location = result.statistic_location
    emp_cdf_at_loc = np.searchsorted(sample, location, side='right') / n
    computed_cdf_at_loc = null_cdf(location)

    ax.vlines(location, emp_cdf_at_loc, computed_cdf_at_loc, linestyles='--',
              label=f'Maximum Deviation: {np.round(distance, 6)}\nat x={np.round(location, 6)}',
              color='xkcd:bright red')

    if provided_loc is not None:
        emp_cdf_at_provided_loc = np.searchsorted(sample, provided_loc, side='right') / n
        computed_cdf_at_provided_loc = null_cdf(provided_loc)
        ax.vlines(provided_loc, emp_cdf_at_provided_loc, computed_cdf_at_provided_loc, linestyles='--',
                  label=f'Deviation: {np.round(np.abs(emp_cdf_at_provided_loc - computed_cdf_at_provided_loc), 6)}\nat x={np.round(provided_loc, 6)}',
                  color='xkcd:shamrock green')

    if distro == 'gengamma':
        r, eta = params
        ax.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
    else:
        ax.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n {distro} (0, {params})')

    ax.legend()
    plt.tight_layout()

    return fig

def visualize_cdf_pdf(sample, params, distro = 'gengamma', log_scale = True, n_samples=10000, interval = None, provided_loc = None, all_cdfs=None, group=None, bw = 0.05, bw_log = 0.05):
    """
    Visualize the gap between the empirical CDF/PDF and the Computed CDF/PDF.

    Args:
        sample (np.ndarray): Observed data.
        r (float): r value.
        eta (float): eta value.
        n_samples (int): Number of samples for the computed CDF/PDF.
        all_cdfs (dict): Dictionary containing computed CDFs.
        group (int or None): Group index (for titling purposes).

    Returns:
        distance (float): The Kolmogorov-Smirnov statistic.
        location (float): The location of the maximum deviation between the empirical and computed CDFs.
    """
    xs = np.linspace(max(-10000, np.min(sample)), min(np.max(sample), 10000), 20000)
    sample = np.sort(sample)
    n = len(sample)
    
    if distro == 'gengamma':
        r, eta = params
        if all_cdfs and (r, eta) in all_cdfs:
            null_cdf = all_cdfs[(r, eta)]
            xs_pdf, computed_pdf = compute_prior_pdf(r, eta, tail_bound=0.01)
        else:
            xs_pdf, computed_pdf, null_cdf = compute_prior_cdf(r=r, eta=eta, n_samples=n_samples, enforce_assert=False, debug=True, return_pdf=True)
        
    elif distro == 'gaussian' or distro == 'normal':
        null_cdf = stats.norm(scale=params).cdf
        xs_pdf = np.linspace(-30, 30, 10000)
        computed_pdf = stats.norm(scale=params).pdf(xs)
    elif distro == 'laplace':
        null_cdf = stats.laplace(scale=params).cdf
        xs_pdf = np.linspace(-30, 30, 10000)
        computed_pdf = stats.laplace(scale=params).pdf(xs)

    if log_scale:

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 6))

        # Empirical CDF vs Computed CDF
        ax1.set_xlim(left = -25, right = 25)
        if interval:
            ax1.set_xlim(left = interval[0], right = interval[1])
        ax1.plot(sample, np.arange(1, n+1)/n, label='Empirical CDF')
        ax1.plot(xs, null_cdf(xs), label='Computed CDF')
        result = stats.ks_1samp(sample, null_cdf)
        distance = result.statistic
        location = result.statistic_location
        emp_cdf_at_loc = np.searchsorted(sample, location, side='right') / n
        computed_cdf_at_loc = null_cdf(location)

        ax1.vlines(location, emp_cdf_at_loc, computed_cdf_at_loc, linestyles='--', label=f'Maximum Deviation: {np.round(distance, 6)}\nat x={np.round(location, 6)}', color='xkcd:bright red')
        if provided_loc:
            emp_cdf_at_provided_loc = np.searchsorted(sample, provided_loc, side='right') / n
            computed_cdf_at_provided_loc = null_cdf(provided_loc)
            ax1.vlines(provided_loc, emp_cdf_at_provided_loc, computed_cdf_at_provided_loc, linestyles='--', label=f'Deviation: {np.round(emp_cdf_at_provided_loc - computed_cdf_at_provided_loc, 6)}\nat x={np.round(provided_loc, 6)}', color='xkcd:shamrock green')
        if distro == 'gengamma':
            ax1.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
            ax2.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical PDF vs Computed PDF \n (r={r}, eta={eta})')
            ax3.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Log Scale:\n Empirical PDF vs Computed PDF (r={r}, eta={eta})')
        else:
            ax1.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n {distro} (0, {params})')
            ax2.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical PDF vs Computed PDF \n {distro} (0, {params})')
            ax3.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Log Scale:\n Empirical PDF vs Computed PDF {distro} (0, {params})')

        # Empirical PDF vs Computed PDF
        ax2.set_xlim(left = -25, right = 25)
        if interval:
            ax2.set_xlim(left = interval[0], right = interval[1])
        
        sns.kdeplot(sample, bw_method = bw, ax=ax2, label=f'Empirical PDF (KDE, bw={bw})')
        ax2.plot(xs_pdf, computed_pdf, label='Computed PDF')
        
        # Log Scale
        ax3.set_xlim(left = -25, right = 25)
        if interval:
            ax3.set_xlim(left = interval[0], right = interval[1])
        ax3.set_ylim(bottom = 10**-4, top=10)
        sns.kdeplot(ax = ax3, x = sample, bw_method = bw, log_scale=[False, True], label = f"Empirical PDF (KDE, bw={bw_log})")
        ax3.plot(xs_pdf, computed_pdf, label = "Computed PDF")

        ax1.legend()
        ax2.legend()
        ax3.legend()

        plt.tight_layout()
        plt.show()

    else:

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Empirical CDF vs Computed CDF
        ax1.set_xlim(left = -25, right = 25)
        ax1.plot(sample, np.arange(1, n+1)/n, label='Empirical CDF')
        ax1.plot(xs, null_cdf(xs), label='Computed CDF')
        result = stats.ks_1samp(sample, null_cdf)
        distance = result.statistic
        location = result.statistic_location
        emp_cdf_at_loc = np.searchsorted(sample, location, side='right') / n
        computed_cdf_at_loc = null_cdf(location)
        ax1.vlines(location, emp_cdf_at_loc, computed_cdf_at_loc, linestyles='--', label=f'Maximum Deviation: {np.round(distance, 6)}\nat x={np.round(location, 6)}', color='xkcd:bright red')
        if distro =='gengamma':
            ax1.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n (r={r}, eta={eta}) with p-value:{np.round(result.pvalue, 8)}')
            ax2.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical PDF vs Computed PDF \n (r={r}, eta={eta})')
        else:
            ax1.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical CDF vs Computed CDF \n {distro} (0, {params})')
            ax2.set_title(f'{f"{GROUP_NAME} {group}" if group else ""} Empirical PDF vs Computed PDF \n {distro} (0, {params})')
        ax1.legend()

        # Empirical PDF vs Computed PDF
        ax2.set_xlim(left = -25, right = 25)
        sns.kdeplot(sample, bw_method = bw, ax=ax2, label=f'Empirical PDF (KDE, bw={bw})')
        ax2.plot(xs_pdf, computed_pdf, label='Computed PDF')
        ax2.legend()
    
    return fig



def twoSampleComparisonPlots(samp1, samp2, bw =0.2, samp1name = "Sample 1", samp2name = "Sample 2"):
    n_1 = len(samp1)
    n_2 = len(samp2)
    ksres = stats.ks_2samp(samp1, samp2)
    ks_loc, ks_stat = ksres.statistic_location, ksres.statistic
    fig, axes = plt.subplots(1, 3, figsize=(24, 6))
    #axes[0].set_xlim(left = -.25*bound, right = .25*bound)
    #axes[1].set_xlim(left = -.25*bound, right = .25*bound)
    axes[1].set_ylim(bottom = 10**-6, top= 10)
    #axes[2].set_xlim(left = -.25*bound, right = .25*bound)
    sns.kdeplot(ax = axes[0], x = samp1, bw_method=bw, label = samp1name)
    sns.kdeplot(ax = axes[0], x = samp2,bw_method = bw, label = samp2name)
    sns.kdeplot(ax = axes[1], x = samp1, bw_method = bw, log_scale=[False, True], label = samp1name)
    sns.kdeplot(ax = axes[1], x = samp2, bw_method = bw, log_scale=[False, True], label = samp2name)
    axes[2].plot(np.sort(samp1), np.arange(1, n_1+1)/n_1, label=samp1name)
    axes[2].plot(np.sort(samp2), np.arange(1, n_2+1)/n_2, label=samp2name)
    emp_cdf_at_loc = np.searchsorted(np.sort(samp1), ks_loc, side='right') / n_1
    emp_cdf_at_loc2 = np.searchsorted(np.sort(samp2), ks_loc, side='right') / n_2
    axes[2].vlines(ks_loc, emp_cdf_at_loc, emp_cdf_at_loc2, linestyles='--', label=f'Maximum Deviation: {np.round(ks_stat, 6)}\nat x={np.round(ks_loc, 6)}', color='xkcd:bright red')
    
    axes[0].set_title("Non Log Scale Pdf")
    axes[1].set_title("Log Scale Pdf")
    axes[2].set_title(f"CDF with p-value:{np.round(ksres.pvalue, 8)}")
    axes[0].legend()
    axes[1].legend()
    axes[2].legend()                                                                
    return fig


def multiSampleComparisonPlots(samps,  samp_names, bw =0.2):
    fig, axes = plt.subplots(1, 3, figsize=(24, 6))
    for i in range(len(samps)):
        n_1 = len(samps[i])
        #axes[0].set_xlim(left = -.25*bound, right = .25*bound)
        #axes[1].set_xlim(left = -.25*bound, right = .25*bound)
        axes[1].set_ylim(bottom = 10**-6, top= 10)
        #axes[2].set_xlim(left = -.25*bound, right = .25*bound)
        sns.kdeplot(ax = axes[0], x = samps[i], bw_method=bw, label = samp_names[i])
        sns.kdeplot(ax = axes[1], x = samps[i], bw_method = bw, log_scale=[False, True], label = samp_names[i])
        axes[2].plot(np.sort(samps[i]), np.arange(1, n_1+1)/n_1, label=samp_names[i])

        
        axes[0].set_title("Non Log Scale Pdf")
        axes[1].set_title("Log Scale Pdf")
        axes[2].set_title(f"CDF")
        axes[0].legend()
        axes[1].legend()
        axes[2].legend()                                                                
    return fig