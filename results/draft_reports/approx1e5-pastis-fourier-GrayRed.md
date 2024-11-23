# Comparative Analysis: PASTIS Dataset (Fourier) - 2024-11-22
## Dataset Variations
* **Variations compared:** approx1e5, approx1e5
* **Image Type:** Red
* **Representation:** Fourier

## Comparative Results

### Best parameters comparison:
|   band |    total_samples |   Gray_best_r |   Red_best_r |   Gray_best_eta |   Red_best_eta |   Gray_kstest_stat_best |   Red_kstest_stat_best |
|-------:|-----------------:|--------------:|-------------:|----------------:|---------------:|------------------------:|-----------------------:|
|      2 |  31800           |         0.29  |        0.279 |            7.49 |           5.9  |                0.004331 |               0.004324 |
|      5 |  41340           |         0.29  |        0.3   |            6.09 |           7.01 |                0.002839 |               0.003425 |
|      8 |  66780           |         0.31  |        0.299 |            6.9  |           5.51 |                0.00329  |               0.003287 |
|     11 | 104940           |         0.311 |        0.32  |            5.67 |           6.29 |                0.002328 |               0.002582 |
|     14 | 162180           |         0.339 |        0.331 |            6.9  |           5.87 |                0.002819 |               0.00258  |
|     17 | 257580           |         0.339 |        0.33  |            5.41 |           4.54 |                0.001387 |               0.000891 |
|     20 | 381600           |         0.35  |        0.341 |            4.7  |           3.99 |                0.000914 |               0.001658 |
|     23 | 610560           |         0.369 |        0.369 |            4.26 |           4.21 |                0.001547 |               0.001126 |
|     26 | 973080           |         0.39  |        0.391 |            3.42 |           3.62 |                0.000988 |               0.000893 |
|     29 |      1.37694e+06 |         0.428 |        0.428 |            2.53 |           3.13 |                0.001861 |               0.001402 |
|     32 | 419760           |         0.624 |        0.547 |            2.58 |           2.65 |                0.001684 |               0.001655 |  
           
### Full Grid Search Combo Plots Comparison
<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 2</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
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
  <h3>Layer 5</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
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
  <h3>Layer 8</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
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

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 11</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 14</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 17</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 20</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 23</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 26</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer26.jpg" alt="Full Grid Search Layer 26" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer26.jpg" alt="Fine Grid Search Layer 26" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer26.jpg" alt="Full Grid Search Layer 26" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer26.jpg" alt="Fine Grid Search Layer 26" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 29</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer29.jpg" alt="Full Grid Search Layer 29" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer29.jpg" alt="Fine Grid Search Layer 29" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer29.jpg" alt="Full Grid Search Layer 29" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer29.jpg" alt="Fine Grid Search Layer 29" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 32</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer32.jpg" alt="Full Grid Search Layer 32" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer32.jpg" alt="Fine Grid Search Layer 32" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer32.jpg" alt="Full Grid Search Layer 32" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\pastis\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer32.jpg" alt="Fine Grid Search Layer 32" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>



### Compare CDF PDF Plots
<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_26.jpg" alt="Layer 26 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_26.jpg" alt="Layer 26 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_29.jpg" alt="Layer 29 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_29.jpg" alt="Layer 29 Plot" width="90%"/>
<p>red</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_32.jpg" alt="Layer 32 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\pastis\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_32.jpg" alt="Layer 32 Plot" width="90%"/>
<p>red</p>
</div>
</div>



### Individual Analyses

### gray
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.29 |           7.5 |             0.0046599 |    0.29  |       7.49 |     0.29  |        7.49 |           0.0043305 |
|      5 |        0.29 |           6.1 |             0.0032413 |    0.29  |       6.09 |     0.29  |        6.09 |           0.0028394 |
|      8 |        0.31 |           6.9 |             0.0032905 |    0.31  |       6.9  |     0.31  |        6.9  |           0.0032905 |
|     11 |        0.31 |           5.6 |             0.0033366 |    0.311 |       5.67 |     0.311 |        5.67 |           0.0023282 |
|     14 |        0.34 |           7   |             0.0028282 |    0.339 |       6.9  |     0.339 |        6.9  |           0.0028195 |
|     17 |        0.34 |           5.5 |             0.0014879 |    0.339 |       5.41 |     0.339 |        5.41 |           0.0013872 |
|     20 |        0.35 |           4.7 |             0.0009142 |    0.35  |       4.7  |     0.35  |        4.7  |           0.0009142 |
|     23 |        0.37 |           4.3 |             0.0021685 |    0.369 |       4.26 |     0.369 |        4.26 |           0.0015469 |
|     26 |        0.39 |           3.4 |             0.0017241 |    0.39  |       3.42 |     0.39  |        3.42 |           0.0009875 |
|     29 |        0.43 |           2.6 |             0.0020862 |    0.428 |       2.53 |     0.428 |        2.53 |           0.0018612 |
|     32 |        0.62 |           2.5 |             0.0019597 |    0.624 |       2.58 |     0.624 |        2.58 |           0.0016837 |

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
