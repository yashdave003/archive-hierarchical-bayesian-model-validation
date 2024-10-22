
# PASTIS Dataset (Wavelet) - 2024-10-22

## Dataset Description

* **Original source:** [Add source information here]
* **Sizes:** [Add size information here]
* **Image Type:** Gray
* **Date range covered:** [Add date range here]
* **Number of Images (and channels):** [Add number of images here]
* **Representation:** Wavelet

## Why did we choose it?

[Add reasons for choosing this dataset]

## Cleaning - what did we do?

[Add cleaning process details]

## Hypotheses

[Add hypotheses, basis/representation used, and assumptions about signal subsets]

## Tests and Questions

### Full Grid Search Combo Plots

<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Layer 2 Plot" width="45%"/>
<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer3.jpg" alt="Layer 3 Plot" width="45%"/>

<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer4.jpg" alt="Layer 4 Plot" width="45%"/>
<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Layer 5 Plot" width="45%"/>

<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer6.jpg" alt="Layer 6 Plot" width="45%"/>
<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer7.jpg" alt="Layer 7 Plot" width="45%"/>

<img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Layer 8 Plot" width="45%"/>



### Compare CDF PDF Plots

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>

<img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>



## Results

Here are the best parameters from the proposed prior distribution:

|   layer |    total_samples |   best_r |   best_eta |   kstest_stat_initial |   kstest_stat_best |   kstest_stat_cutoff_0.05 |   n_pval_0.05 |
|--------:|-----------------:|---------:|-----------:|----------------------:|-------------------:|--------------------------:|--------------:|
|       2 |   3180           |  0.4209  |    5.738   |            0.018069   |         0.0174559  |               0.0240303   |          6034 |
|       3 |  12720           |  0.4921  |    6.186   |            0.0046148  |         0.00387299 |               0.0120285   |        122248 |
|       4 |  50880           |  0.4353  |    1.298   |            0.00627036 |         0.00527459 |               0.00601756  |         64395 |
|       5 | 203520           |  0.46001 |    0.11583 |            0.00523582 |         0.00374205 |               0.0030096   |        128790 |
|       6 | 814080           |  0.52    |   -0.58    |            0.00434924 |         0.00311    |               0.00150501  |        193185 |
|       7 |      3.25632e+06 |  0.91    |   -0.92    |            0.0104128  |         0.00843243 |               0.000752555 |         25440 |
|       8 |      1.30253e+07 |  0.7     |   -1.26    |            0.0515196  |         0.0355432  |               0.00037629  |          1507 |

Here are the KS statistics along with the cutoff for a p-value of 0.05:

|   layer |    total_samples |   kstest_stat_initial |   kstest_stat_cutoff_0.05 |   kstest_stat_eta0 |   kstest_stat_best |   kstest_stat_iter1 |   kstest_stat_iter2 |   kstest_stat_iter3 |   kstest_stat_gaussian |   kstest_stat_laplace |   kstest_stat_t |   kstest_stat_gengamma_tail2 |   kstest_stat_gengamma_tail10 |
|--------:|-----------------:|----------------------:|--------------------------:|-------------------:|-------------------:|--------------------:|--------------------:|--------------------:|-----------------------:|----------------------:|----------------:|-----------------------------:|------------------------------:|
|       2 |   3180           |            0.018069   |               0.0240303   |         0.0603464  |         0.0174559  |          0.0174559  |          0.0174559  |        nan          |              0.0195034 |            0.0363916  |       0.0363047 |                   0.018069   |                   0.018069    |
|       3 |  12720           |            0.0046148  |               0.0120285   |         0.0370116  |         0.00387299 |          0.00387774 |          0.00387299 |        nan          |              0.010128  |            0.0226653  |       0.0264103 |                   0.0046148  |                   0.00382446  |
|       4 |  50880           |            0.00627036 |               0.00601756  |         0.0233191  |         0.00527459 |          0.00527459 |          0.00527459 |        nan          |              0.0204744 |            0.0144979  |       0.0184891 |                   0.00581164 |                   0.00548717  |
|       5 | 203520           |            0.00523582 |               0.0030096   |         0.00565307 |         0.00374205 |          0.00381335 |          0.0037484  |          0.00374205 |              0.030178  |            0.00234437 |       0.0105699 |                   0.0033221  |                   0.0013737   |
|       6 | 814080           |            0.00434924 |               0.00150501  |         0.0205071  |         0.00311    |          0.00311    |          0.00311    |          0.00311    |              0.0423748 |            0.0144807  |       0.0179405 |                   0.00253789 |                   0.000983783 |
|       7 |      3.25632e+06 |            0.0104128  |               0.000752555 |         0.0822836  |         0.00843243 |          0.00843243 |          0.00843243 |          0.00843243 |              0.0529285 |            0.0252819  |       0.0264405 |                   0.00844614 |                   2.98904e-05 |
|       8 |      1.30253e+07 |            0.0515196  |               0.00037629  |         0.227351   |         0.0355432  |          0.0355432  |          0.0355432  |          0.0355432  |              0.0563576 |            0.0291519  |       0.02814   |                   0.00250438 |                   1e-05       |

Here are the comparisons with other common priors (Gaussian, Laplace, Student t):

|   layer |   kstest_stat_initial |   best_r_eta0 |   best_r |   best_eta |   kstest_stat_best |   param_gaussian |   kstest_stat_gaussian |   param_laplace |   kstest_stat_laplace |   param_t |   kstest_stat_t |
|--------:|----------------------:|--------------:|---------:|-----------:|-------------------:|-----------------:|-----------------------:|----------------:|----------------------:|----------:|----------------:|
|       2 |            0.018069   |          0.26 |  0.4209  |    5.738   |         0.0174559  |        27.7823   |              0.0195034 |       25.4391   |            0.0363916  | 20.7528   |       0.0363047 |
|       3 |            0.0046148  |          0.29 |  0.4921  |    6.186   |         0.00387299 |        16.0314   |              0.010128  |       14.0129   |            0.0226653  | 11.2771   |       0.0264103 |
|       4 |            0.00627036 |          0.34 |  0.4353  |    1.298   |         0.00527459 |         8.00107  |              0.0204744 |        7.10498  |            0.0144979  |  5.71965  |       0.0184891 |
|       5 |            0.00523582 |          0.44 |  0.46001 |    0.11583 |         0.00374205 |         3.5902   |              0.030178  |        3.13887  |            0.00234437 |  2.57409  |       0.0105699 |
|       6 |            0.00434924 |          0.74 |  0.52    |   -0.58    |         0.00311    |         1.42619  |              0.0423748 |        1.2468   |            0.0144807  |  1.01054  |       0.0179405 |
|       7 |            0.0104128  |          6.1  |  0.91    |   -0.92    |         0.00843243 |         0.539656 |              0.0529285 |        0.47276  |            0.0252819  |  0.378321 |       0.0264405 |
|       8 |            0.0515196  |          6    |  0.7     |   -1.26    |         0.0355432  |         0.196027 |              0.0563576 |        0.172569 |            0.0291519  |  0.137349 |       0.02814   |

All the columns you can access:

['obs_var', 'var_lower', 'var_upper', 'obs_kurt', 'kurt_lower', 'kurt_upper', 'total_samples', 'initial_r', 'initial_eta', 'kstest_stat_initial', 'kstest_stat_cutoff_0.05', 'kstest_stat_eta0', 'best_r_eta0', 'best_r', 'best_eta', 'kstest_stat_best', 'iter1_r', 'iter1_eta', 'kstest_stat_iter1', 'iter2_r', 'iter2_eta', 'kstest_stat_iter2', 'iter3_r', 'iter3_eta', 'kstest_stat_iter3', 'n_pval_0.05', 'param_gaussian', 'kstest_stat_gaussian', 'kstest_pval_gaussian', 'param_laplace', 'kstest_stat_laplace', 'kstest_pval_laplace', 'param_t', 'kstest_stat_t', 'kstest_pval_t', 'kstest_pval_gengamma', 'kstest_ratio_gengamma_tail0', 'kstest_ratio_gengamma_tail10', 'kstest_ratio_gaussian_tail0', 'kstest_ratio_gaussian_tail10', 'kstest_ratio_laplace_tail0', 'kstest_ratio_laplace_tail10', 'kstest_ratio_t_tail0', 'kstest_ratio_t_tail10', 'kstest_stat_gengamma_tail2', 'kstest_stat_gengamma_tail10']

## Major Take-aways

[Add major conclusions and insights]
