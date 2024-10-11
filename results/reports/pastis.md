
# PASTIS Dataset - 2024-10-11

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

<table>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Layer 2 Plot"></td>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer3.jpg" alt="Layer 3 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer4.jpg" alt="Layer 4 Plot"></td>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Layer 5 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer6.jpg" alt="Layer 6 Plot"></td>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer7.jpg" alt="Layer 7 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Layer 8 Plot"></td>
    <td></td>
  </tr>
</table>


### Compare CDF PDF Plots

<table>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot"></td>
  </tr>
  <tr>
    <td><img src="wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_9.jpg" alt="Layer 9 Plot"></td>
  </tr>
</table>


## Results

Here are the best parameters from the proposed prior distribution

|    |    total_samples |   best_r |   best_eta |   kstest_stat_best |
|---:|-----------------:|---------:|-----------:|-------------------:|
|  0 |   3180           |    0.42  |       5.68 |         0.0175418  |
|  1 |  12720           |    0.509 |       7.22 |         0.00426327 |
|  2 |  50880           |    0.436 |       1.31 |         0.00531527 |
|  3 | 203520           |    0.462 |       0.13 |         0.00390606 |
|  4 | 814080           |    0.52  |      -0.58 |         0.00311    |
|  5 |      3.25632e+06 |    0.91  |      -0.92 |         0.00843243 |
|  6 |      1.30253e+07 |    0.7   |      -1.26 |         0.0355432  |

Here are the KS statistics along with the cutoff for a p-value of 0.05.

|    |    total_samples |   kstest_stat_initial |   kstest_stat_cutoff_0.05 |   kstest_stat_eta0 |   kstest_stat_best |   kstest_stat_gaussian |   kstest_stat_laplace |   kstest_stat_t |
|---:|-----------------:|----------------------:|--------------------------:|-------------------:|-------------------:|-----------------------:|----------------------:|----------------:|
|  0 |   3180           |            0.018069   |               0.0240303   |         0.0603464  |         0.0175418  |              0.0195034 |            0.0363916  |       0.0363047 |
|  1 |  12720           |            0.0046148  |               0.0120285   |         0.0370116  |         0.00426327 |              0.010128  |            0.0226653  |       0.0264103 |
|  2 |  50880           |            0.00627036 |               0.00601756  |         0.0233191  |         0.00531527 |              0.0204744 |            0.0144979  |       0.0184891 |
|  3 | 203520           |            0.00523582 |               0.0030096   |         0.00565307 |         0.00390606 |              0.030178  |            0.00234437 |       0.0105699 |
|  4 | 814080           |            0.00752167 |               0.00150501  |         0.0205071  |         0.00311    |              0.0423748 |            0.0144807  |       0.0179405 |
|  5 |      3.25632e+06 |            0.0114808  |               0.000752555 |         0.0822836  |         0.00843243 |              0.0529285 |            0.0252819  |       0.0264405 |
|  6 |      1.30253e+07 |            0.02814    |               0.00037629  |         0.227351   |         0.0355432  |              0.0563576 |            0.0291519  |       0.02814   |

## Major Take-aways

[Add major conclusions and insights]
