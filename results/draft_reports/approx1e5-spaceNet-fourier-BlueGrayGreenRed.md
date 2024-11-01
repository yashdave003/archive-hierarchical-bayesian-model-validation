# Comparative Analysis: SPACENET Dataset (Fourier) - 2024-11-01
## Dataset Variations
* **Variations compared:** approx1e5, approx1e5, approx1e5, approx1e5
* **Image Type:** Green
* **Representation:** Fourier

## Comparative Results

### Best parameters comparison:
|   band |    total_samples |   Gray_best_r |   Red_best_r |   Blue_best_r |   Green_best_r |   Gray_best_eta |   Red_best_eta |   Blue_best_eta |   Green_best_eta |   Gray_kstest_stat_best |   Red_kstest_stat_best |   Blue_kstest_stat_best |   Green_kstest_stat_best |
|-------:|-----------------:|--------------:|-------------:|--------------:|---------------:|----------------:|---------------:|----------------:|-----------------:|------------------------:|-----------------------:|------------------------:|-------------------------:|
|      2 |  47614           |         0.159 |        0.16  |         0.16  |          0.16  |            1.51 |           1.55 |            1.53 |             1.63 |                0.012798 |               0.012062 |                0.012635 |                 0.012692 |
|      5 | 102030           |         0.159 |        0.159 |         0.161 |          0.16  |            1.04 |           1    |            1.09 |             1.15 |                0.013544 |               0.012899 |                0.013009 |                 0.013048 |
|      8 | 326496           |         0.17  |        0.169 |         0.159 |          0.158 |            1.14 |           1.04 |            0.54 |             0.6  |                0.012261 |               0.010795 |                0.010749 |                 0.010866 |
|     11 | 904666           |         0.168 |        0.17  |         0.179 |          0.179 |            0.53 |           0.6  |            0.91 |             1.04 |                0.010326 |               0.008976 |                0.011668 |                 0.01198  |
|     14 |      2.7276e+06  |         0.18  |        0.18  |         0.178 |          0.179 |            0.55 |           0.55 |            0.41 |             0.53 |                0.009279 |               0.008708 |                0.00868  |                 0.009083 |
|     17 |      8.29844e+06 |         0.19  |        0.192 |         0.199 |          0.2   |            0.42 |           0.48 |            0.62 |             0.76 |                0.005315 |               0.005652 |                0.006765 |                 0.007034 |
|     20 |      2.51402e+07 |         0.227 |        0.228 |         0.228 |          0.219 |            0.9  |           0.91 |            0.8  |             0.65 |                0.003653 |               0.002292 |                0.001818 |                 0.002705 |
|     23 |      6.57345e+07 |         0.257 |        0.259 |         0.267 |          0.251 |            1.22 |           1.27 |            1.4  |             1.05 |                0.003347 |               0.002109 |                0.003228 |                 0.003287 |  
           
### Full Grid Search Combo Plots Comparison
<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 2</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer11.jpg" alt="Full Grid Search Layer 11" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer11.jpg" alt="Fine Grid Search Layer 11" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer14.jpg" alt="Full Grid Search Layer 14" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer14.jpg" alt="Fine Grid Search Layer 14" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer17.jpg" alt="Full Grid Search Layer 17" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer17.jpg" alt="Fine Grid Search Layer 17" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer20.jpg" alt="Full Grid Search Layer 20" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer20.jpg" alt="Fine Grid Search Layer 20" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\full_grid_search_combo_plot_layer23.jpg" alt="Full Grid Search Layer 23" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer23.jpg" alt="Fine Grid Search Layer 23" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>



### Compare CDF PDF Plots
<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_11.jpg" alt="Layer 11 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_14.jpg" alt="Layer 14 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_17.jpg" alt="Layer 17 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_20.jpg" alt="Layer 20 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\gray\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\red\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\blue\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\fourier\approx1e5\green\plots\compare_cdf_pdf_layer_23.jpg" alt="Layer 23 Plot" width="90%"/>
<p>green</p>
</div>
</div>



### Individual Analyses

### gray
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.16 |           1.6 |             0.0134767 |    0.159 |       1.51 |     0.159 |        1.51 |           0.012798  |
|      5 |        0.16 |           1.1 |             0.0137607 |    0.159 |       1.04 |     0.159 |        1.04 |           0.0135444 |
|      8 |        0.17 |           1.2 |             0.0135236 |    0.17  |       1.14 |     0.17  |        1.14 |           0.0122607 |
|     11 |        0.17 |           0.6 |             0.0123291 |    0.168 |       0.53 |     0.168 |        0.53 |           0.0103259 |
|     14 |        0.18 |           0.6 |             0.0113105 |    0.18  |       0.55 |     0.18  |        0.55 |           0.0092794 |
|     17 |        0.19 |           0.4 |             0.0090515 |    0.19  |       0.42 |     0.19  |        0.42 |           0.0053148 |
|     20 |        0.23 |           1   |             0.0047507 |    0.227 |       0.9  |     0.227 |        0.9  |           0.0036526 |
|     23 |        0.26 |           1.3 |             0.005128  |    0.257 |       1.22 |     0.257 |        1.22 |           0.0033469 |

### red
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.16 |           1.6 |             0.0139004 |    0.16  |       1.55 |     0.16  |        1.55 |           0.0120623 |
|      5 |        0.16 |           1.1 |             0.0146592 |    0.159 |       1    |     0.159 |        1    |           0.0128993 |
|      8 |        0.17 |           1.1 |             0.0112189 |    0.169 |       1.04 |     0.169 |        1.04 |           0.0107948 |
|     11 |        0.17 |           0.6 |             0.0089761 |    0.17  |       0.6  |     0.17  |        0.6  |           0.0089761 |
|     14 |        0.18 |           0.6 |             0.010865  |    0.18  |       0.55 |     0.18  |        0.55 |           0.0087076 |
|     17 |        0.19 |           0.4 |             0.0089293 |    0.192 |       0.48 |     0.192 |        0.48 |           0.0056518 |
|     20 |        0.23 |           1   |             0.003891  |    0.228 |       0.91 |     0.228 |        0.91 |           0.0022924 |
|     23 |        0.26 |           1.3 |             0.0022315 |    0.259 |       1.27 |     0.259 |        1.27 |           0.0021093 |

### blue
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.16 |           1.6 |             0.015444  |    0.16  |       1.53 |     0.16  |        1.53 |           0.0126345 |
|      5 |        0.16 |           1.1 |             0.0145874 |    0.161 |       1.09 |     0.161 |        1.09 |           0.0130095 |
|      8 |        0.16 |           0.6 |             0.0114054 |    0.159 |       0.54 |     0.159 |        0.54 |           0.0107491 |
|     11 |        0.18 |           1   |             0.0130805 |    0.179 |       0.91 |     0.179 |        0.91 |           0.0116684 |
|     14 |        0.18 |           0.5 |             0.0100246 |    0.178 |       0.41 |     0.178 |        0.41 |           0.0086797 |
|     17 |        0.2  |           0.7 |             0.0097256 |    0.199 |       0.62 |     0.199 |        0.62 |           0.0067653 |
|     20 |        0.23 |           0.9 |             0.0068757 |    0.228 |       0.8  |     0.228 |        0.8  |           0.0018183 |
|     23 |        0.27 |           1.5 |             0.0044928 |    0.267 |       1.4  |     0.267 |        1.4  |           0.0032283 |

### green
#### Optimization progression:
|   band |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|-------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|      2 |        0.16 |           1.7 |             0.0149368 |    0.16  |       1.63 |     0.16  |        1.63 |           0.0126924 |
|      5 |        0.16 |           1.2 |             0.0143578 |    0.16  |       1.15 |     0.16  |        1.15 |           0.0130481 |
|      8 |        0.16 |           0.7 |             0.0114418 |    0.158 |       0.6  |     0.158 |        0.6  |           0.0108658 |
|     11 |        0.18 |           1.1 |             0.0123813 |    0.179 |       1.04 |     0.179 |        1.04 |           0.0119797 |
|     14 |        0.18 |           0.6 |             0.0106575 |    0.179 |       0.53 |     0.179 |        0.53 |           0.0090828 |
|     17 |        0.2  |           0.8 |             0.0092807 |    0.2   |       0.76 |     0.2   |        0.76 |           0.0070335 |
|     20 |        0.22 |           0.7 |             0.0056062 |    0.219 |       0.65 |     0.219 |        0.65 |           0.0027046 |
|     23 |        0.25 |           1   |             0.004461  |    0.251 |       1.05 |     0.251 |        1.05 |           0.0032874 |
