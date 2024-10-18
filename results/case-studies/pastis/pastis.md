
# PASTIS Dataset - 2024-10-18

## Dataset Description

* **Original source:** [Add source information here]
* **Sizes:** [Add size information here]
* **Image Type:** Gray
* **Date range covered:** [Add date range here]
* **Number of Images (and channels):** [Add number of images here]

## Why did we choose it?

[Add reasons for choosing this dataset]

## Cleaning - what did we do?

[Add cleaning process details]

## Hypotheses

[Add hypotheses, basis/representation used, and assumptions about signal subsets]

## Tests and Questions

### Full Grid Search Combo Plots

![Layer 2 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg)
![Layer 3 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer3.jpg)

![Layer 4 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer4.jpg)
![Layer 5 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg)

![Layer 6 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer6.jpg)
![Layer 7 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer7.jpg)

![Layer 8 Plot](wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg)



### Compare CDF PDF Plots

![Layer 2 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg)

![Layer 3 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_3.jpg)

![Layer 4 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_4.jpg)

![Layer 5 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg)

![Layer 6 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_6.jpg)

![Layer 7 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_7.jpg)

![Layer 8 Plot](wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg)



## Results

Here are the best parameters from the proposed prior distribution:

|   layer |    total_samples |   best_r |   best_eta |   kstest_stat_best |
|--------:|-----------------:|---------:|-----------:|-------------------:|
|       2 |   3180           |    0.42  |       5.68 |         0.0175418  |
|       3 |  12720           |    0.509 |       7.22 |         0.00426327 |
|       4 |  50880           |    0.436 |       1.31 |         0.00531527 |
|       5 | 203520           |    0.462 |       0.13 |         0.00390606 |
|       6 | 814080           |    0.52  |      -0.58 |         0.00311    |
|       7 |      3.25632e+06 |    0.91  |      -0.92 |         0.00843243 |
|       8 |      1.30253e+07 |    0.7   |      -1.26 |         0.0355432  |

Here are the KS statistics along with the cutoff for a p-value of 0.05:

|   layer |    total_samples |   kstest_stat_initial |   kstest_stat_cutoff_0.05 |   kstest_stat_eta0 |   kstest_stat_best |   kstest_stat_gaussian |   kstest_stat_laplace |   kstest_stat_t |   kstest_stat_gengamma_tail2 |   kstest_stat_gengamma_tail10 |
|--------:|-----------------:|----------------------:|--------------------------:|-------------------:|-------------------:|-----------------------:|----------------------:|----------------:|-----------------------------:|------------------------------:|
|       2 |   3180           |            0.018069   |               0.0240303   |         0.0603464  |         0.0175418  |              0.0195034 |            0.0363916  |       0.0363047 |                   0.018069   |                   0.018069    |
|       3 |  12720           |            0.0046148  |               0.0120285   |         0.0370116  |         0.00426327 |              0.010128  |            0.0226653  |       0.0264103 |                   0.0046148  |                   0.00382446  |
|       4 |  50880           |            0.00627036 |               0.00601756  |         0.0233191  |         0.00531527 |              0.0204744 |            0.0144979  |       0.0184891 |                   0.00581164 |                   0.00548717  |
|       5 | 203520           |            0.00523582 |               0.0030096   |         0.00565307 |         0.00390606 |              0.030178  |            0.00234437 |       0.0105699 |                   0.0033221  |                   0.0013737   |
|       6 | 814080           |            0.00434924 |               0.00150501  |         0.0205071  |         0.00311    |              0.0423748 |            0.0144807  |       0.0179405 |                   0.00253789 |                   0.000983783 |
|       7 |      3.25632e+06 |            0.0104128  |               0.000752555 |         0.0822836  |         0.00843243 |              0.0529285 |            0.0252819  |       0.0264405 |                   0.00844614 |                   2.98904e-05 |
|       8 |      1.30253e+07 |            0.0515196  |               0.00037629  |         0.227351   |         0.0355432  |              0.0563576 |            0.0291519  |       0.02814   |                   0.00250438 |                   1e-05       |

## Major Take-aways

[Add major conclusions and insights]
