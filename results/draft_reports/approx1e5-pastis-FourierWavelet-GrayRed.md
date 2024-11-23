# Comparative Analysis: PASTIS Dataset (Fourier) - 2024-11-22
## Dataset Variations
* **Variations compared:** approx1e5, approx1e5
* **Image Type:** Red
* **Representation:** Fourier

## Comparative Results

### Best parameters comparison:
|    |    total_samples |   Gray_best_r |   Red_best_r |   Gray_best_eta |   Red_best_eta |   Gray_kstest_stat_best |   Red_kstest_stat_best |
|---:|-----------------:|--------------:|-------------:|----------------:|---------------:|------------------------:|-----------------------:|
|  2 |   3180           |         0.34  |        0.279 |           2.42  |           5.9  |                0.016925 |               0.004324 |
|  3 |  12720           |         0.353 |      nan     |           1.56  |         nan    |                0.005072 |             nan        |
|  4 |  50880           |         0.361 |      nan     |           0.53  |         nan    |                0.004837 |             nan        |
|  5 | 203520           |         0.4   |        0.3   |          -0.061 |           7.01 |                0.001806 |               0.003425 |
|  6 | 814080           |         0.458 |      nan     |          -0.57  |         nan    |                0.004687 |             nan        |
|  7 |      3.25632e+06 |         0.72  |      nan     |          -0.852 |         nan    |                0.008731 |             nan        |
|  8 |      1.30253e+07 |         1.9   |        0.299 |          -1.169 |           5.51 |                0.033499 |               0.003287 |
| 11 |    nan           |       nan     |        0.32  |         nan     |           6.29 |              nan        |               0.002582 |
| 14 |    nan           |       nan     |        0.331 |         nan     |           5.87 |              nan        |               0.00258  |
| 17 |    nan           |       nan     |        0.33  |         nan     |           4.54 |              nan        |               0.000891 |
| 20 |    nan           |       nan     |        0.341 |         nan     |           3.99 |              nan        |               0.001658 |
| 23 |    nan           |       nan     |        0.369 |         nan     |           4.21 |              nan        |               0.001126 |
| 26 |    nan           |       nan     |        0.391 |         nan     |           3.62 |              nan        |               0.000893 |
| 29 |    nan           |       nan     |        0.428 |         nan     |           3.13 |              nan        |               0.001402 |
| 32 |    nan           |       nan     |        0.547 |         nan     |           2.65 |              nan        |               0.001655 |  
           
### Full Grid Search Combo Plots Comparison
<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 2</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 3</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer3.jpg" alt="Full Grid Search Layer 3" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer3.jpg" alt="Fine Grid Search Layer 3" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 4</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer4.jpg" alt="Full Grid Search Layer 4" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer4.jpg" alt="Fine Grid Search Layer 4" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 5</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 6</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer6.jpg" alt="Full Grid Search Layer 6" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer6.jpg" alt="Fine Grid Search Layer 6" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 7</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer7.jpg" alt="Full Grid Search Layer 7" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer7.jpg" alt="Fine Grid Search Layer 7" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 8</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>



### Compare CDF PDF Plots
<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>
<p>gray</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>
<p>gray</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>
<p>gray</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>
<p>gray</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>red</p>
</div>
</div>



### Individual Analyses

### gray
#### Optimization progression:
|   layer |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|--------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|       2 |        0.34 |          2.4  |             0.017569  |    0.34  |      2.42  |     0.34  |       2.42  |           0.0169247 |
|       3 |        0.35 |          1.5  |             0.0061952 |    0.353 |      1.56  |     0.353 |       1.56  |           0.0050719 |
|       4 |        0.36 |          0.5  |             0.0063676 |    0.361 |      0.53  |     0.361 |       0.53  |           0.0048372 |
|       5 |        0.4  |         -0.06 |             0.0018459 |    0.4   |     -0.061 |     0.4   |      -0.061 |           0.0018058 |
|       6 |        0.45 |         -0.6  |             0.0061402 |    0.458 |     -0.57  |     0.458 |      -0.57  |           0.0046868 |
|       7 |        0.7  |         -0.86 |             0.0092933 |    0.72  |     -0.852 |     0.72  |      -0.852 |           0.0087311 |
|       8 |        2    |         -1.17 |             0.0335157 |    1.9   |     -1.169 |     1.9   |      -1.169 |           0.0334987 |

### red
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.28 |           6   |             0.0045452 |    0.279 |       5.9  |     0.279 |        5.9  |           0.0043243 |
|      5 |        0.3  |           7   |             0.0034432 |    0.3   |       7.01 |     0.3   |        7.01 |           0.0034254 |
|      8 |        0.3  |           5.6 |             0.0033045 |    0.299 |       5.51 |     0.299 |        5.51 |           0.0032875 |
|     11 |        0.32 |           6.3 |             0.0029474 |    0.32  |       6.29 |     0.32  |        6.29 |           0.0025817 |
|     14 |        0.33 |           5.8 |             0.0027656 |    0.331 |       5.87 |     0.331 |        5.87 |           0.0025805 |
|     17 |        0.33 |           4.5 |             0.0026296 |    0.33  |       4.54 |     0.33  |        4.54 |           0.0008908 |
|     20 |        0.34 |           3.9 |             0.0028776 |    0.341 |       3.99 |     0.341 |        3.99 |           0.0016577 |
|     23 |        0.37 |           4.3 |             0.0027998 |    0.369 |       4.21 |     0.369 |        4.21 |           0.0011262 |
|     26 |        0.39 |           3.6 |             0.0019934 |    0.391 |       3.62 |     0.391 |        3.62 |           0.0008933 |
|     29 |        0.43 |           3.2 |             0.0015142 |    0.428 |       3.13 |     0.428 |        3.13 |           0.0014017 |
|     32 |        0.55 |           2.7 |             0.0020081 |    0.547 |       2.65 |     0.547 |        2.65 |           0.0016553 |
