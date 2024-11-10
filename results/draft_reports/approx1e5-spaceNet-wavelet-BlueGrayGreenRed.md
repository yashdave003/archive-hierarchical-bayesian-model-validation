# Comparative Analysis: SPACENET Dataset (Wavelet) - 2024-11-08
## Dataset Variations
* **Variations compared:** approx1e5, approx1e5, approx1e5, approx1e5
* **Image Type:** Green
* **Representation:** Wavelet

## Comparative Results

### Best parameters comparison:
|   layer |    total_samples |   Gray_best_r |   Red_best_r |   Blue_best_r |   Green_best_r |   Gray_best_eta |   Red_best_eta |   Blue_best_eta |   Green_best_eta |   Gray_kstest_stat_best |   Red_kstest_stat_best |   Blue_kstest_stat_best |   Green_kstest_stat_best |
|--------:|-----------------:|--------------:|-------------:|--------------:|---------------:|----------------:|---------------:|----------------:|-----------------:|------------------------:|-----------------------:|------------------------:|-------------------------:|
|       2 |  27208           |         0.205 |        0.207 |        0.208  |          0.204 |           -0.1  |          -0.08 |           -0.08 |            -0.1  |                0.019506 |               0.018429 |                0.02168  |                 0.019212 |
|       3 | 108832           |         0.086 |        0.087 |        0.087  |          0.087 |           -1.37 |          -1.37 |           -1.37 |            -1.37 |                0.13244  |               0.13153  |                0.13192  |                 0.13308  |
|       4 | 333298           |         0.171 |        0.13  |        0.126  |          0.12  |           -0.92 |          -1.24 |           -1.23 |            -1.24 |                0.07707  |               0.07636  |                0.07505  |                 0.0778   |
|       5 |      1.14954e+06 |         0.162 |        0.19  |        0.192  |          0.161 |           -1.14 |          -1.05 |           -1.04 |            -1.14 |                0.042154 |               0.040245 |                0.039836 |                 0.043118 |
|       6 |      4.25125e+06 |         0.228 |        0.24  |        0.24   |          0.224 |           -0.97 |          -0.93 |           -0.95 |            -0.97 |                0.021304 |               0.018534 |                0.022744 |                 0.020647 |
|       7 |      1.7005e+07  |         0.27  |        0.28  |        0.28   |          0.271 |           -1.03 |          -1.01 |           -1.03 |            -1.02 |                0.013764 |               0.01334  |                0.014094 |                 0.013502 |
|       8 |      6.802e+07   |         0.42  |        0.438 |        0.455  |          0.42  |           -1.01 |          -1    |           -1.01 |            -1    |                0.011656 |               0.013254 |                0.011965 |                 0.012391 |
|       9 |      2.7208e+08  |         1.229 |        1.29  |        9.9999 |          1.29  |           -1    |          -1.03 |           -1.08 |            -1.03 |                0.016586 |               0.024493 |                0.023453 |                 0.025333 |  
           
### Full Grid Search Combo Plots Comparison
<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 2</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer2.jpg" alt="Full Grid Search Layer 2" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer2.jpg" alt="Fine Grid Search Layer 2" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer3.jpg" alt="Full Grid Search Layer 3" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer3.jpg" alt="Fine Grid Search Layer 3" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer3.jpg" alt="Full Grid Search Layer 3" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer3.jpg" alt="Fine Grid Search Layer 3" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer3.jpg" alt="Full Grid Search Layer 3" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer3.jpg" alt="Fine Grid Search Layer 3" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer3.jpg" alt="Full Grid Search Layer 3" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer3.jpg" alt="Fine Grid Search Layer 3" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 4</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer4.jpg" alt="Full Grid Search Layer 4" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer4.jpg" alt="Fine Grid Search Layer 4" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer4.jpg" alt="Full Grid Search Layer 4" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer4.jpg" alt="Fine Grid Search Layer 4" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer4.jpg" alt="Full Grid Search Layer 4" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer4.jpg" alt="Fine Grid Search Layer 4" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer4.jpg" alt="Full Grid Search Layer 4" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer4.jpg" alt="Fine Grid Search Layer 4" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer5.jpg" alt="Full Grid Search Layer 5" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer5.jpg" alt="Fine Grid Search Layer 5" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer6.jpg" alt="Full Grid Search Layer 6" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer6.jpg" alt="Fine Grid Search Layer 6" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer6.jpg" alt="Full Grid Search Layer 6" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer6.jpg" alt="Fine Grid Search Layer 6" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer6.jpg" alt="Full Grid Search Layer 6" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer6.jpg" alt="Fine Grid Search Layer 6" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer6.jpg" alt="Full Grid Search Layer 6" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer6.jpg" alt="Fine Grid Search Layer 6" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 7</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer7.jpg" alt="Full Grid Search Layer 7" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer7.jpg" alt="Fine Grid Search Layer 7" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer7.jpg" alt="Full Grid Search Layer 7" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer7.jpg" alt="Fine Grid Search Layer 7" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer7.jpg" alt="Full Grid Search Layer 7" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer7.jpg" alt="Fine Grid Search Layer 7" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer7.jpg" alt="Full Grid Search Layer 7" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer7.jpg" alt="Fine Grid Search Layer 7" style="width: 80%;">
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
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer8.jpg" alt="Full Grid Search Layer 8" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer8.jpg" alt="Fine Grid Search Layer 8" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>

<div style="display: flex; flex-direction: column; margin-bottom: 40px;">
  <h3>Layer 9</h3>
  <div style="margin-bottom: 20px;">
    <h4>gray</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\full_grid_search_combo_plot_layer9.jpg" alt="Full Grid Search Layer 9" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\optimized_full_grid_search_combo_plot_layer9.jpg" alt="Fine Grid Search Layer 9" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>red</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\full_grid_search_combo_plot_layer9.jpg" alt="Full Grid Search Layer 9" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\optimized_full_grid_search_combo_plot_layer9.jpg" alt="Fine Grid Search Layer 9" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>blue</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\full_grid_search_combo_plot_layer9.jpg" alt="Full Grid Search Layer 9" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\optimized_full_grid_search_combo_plot_layer9.jpg" alt="Fine Grid Search Layer 9" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
  <div style="margin-bottom: 20px;">
    <h4>green</h4>
    <div style="display: flex; gap: 20px; justify-content: center;">
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\full_grid_search_combo_plot_layer9.jpg" alt="Full Grid Search Layer 9" style="width: 80%;">
        <p>Full Grid Search</p>
      </div>
      <div style="text-align: center;">
        <img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\optimized_full_grid_search_combo_plot_layer9.jpg" alt="Fine Grid Search Layer 9" style="width: 80%;">
        <p>Fine Grid Search</p>
      </div>
    </div>
  </div>
</div>



### Compare CDF PDF Plots
<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_2.jpg" alt="Layer 2 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_3.jpg" alt="Layer 3 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_4.jpg" alt="Layer 4 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_5.jpg" alt="Layer 5 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_6.jpg" alt="Layer 6 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_7.jpg" alt="Layer 7 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_8.jpg" alt="Layer 8 Plot" width="90%"/>
<p>green</p>
</div>
</div>

<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\gray\plots\compare_cdf_pdf_layer_9.jpg" alt="Layer 9 Plot" width="90%"/>
<p>gray</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\red\plots\compare_cdf_pdf_layer_9.jpg" alt="Layer 9 Plot" width="90%"/>
<p>red</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\blue\plots\compare_cdf_pdf_layer_9.jpg" alt="Layer 9 Plot" width="90%"/>
<p>blue</p>
</div>
<div style="text-align: center;">
<img src="..\case-studies\spaceNet\wavelet\approx1e5\green\plots\compare_cdf_pdf_layer_9.jpg" alt="Layer 9 Plot" width="90%"/>
<p>green</p>
</div>
</div>



### Individual Analyses

### gray
#### Optimization progression:
|   layer |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|--------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|       2 |        0.21 |           0   |             0.0209023 |    0.205 |      -0.1  |     0.205 |       -0.1  |           0.0195055 |
|       3 |        0.09 |          -1.3 |             0.13244   |    0.086 |      -1.37 |     0.086 |       -1.37 |           0.13244   |
|       4 |        0.18 |          -0.9 |             0.07707   |    0.171 |      -0.92 |     0.171 |       -0.92 |           0.07707   |
|       5 |        0.17 |          -1.1 |             0.0421566 |    0.162 |      -1.14 |     0.162 |       -1.14 |           0.042154  |
|       6 |        0.22 |          -1   |             0.0236605 |    0.228 |      -0.97 |     0.228 |       -0.97 |           0.0213042 |
|       7 |        0.28 |          -1   |             0.0185749 |    0.27  |      -1.03 |     0.27  |       -1.03 |           0.0137644 |
|       8 |        0.43 |          -1   |             0.0124702 |    0.42  |      -1.01 |     0.42  |       -1.01 |           0.0116561 |
|       9 |        1.23 |          -1   |             0.0166035 |    1.229 |      -1    |     1.229 |       -1    |           0.0165857 |

### red
#### Optimization progression:
|   layer |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|--------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|       2 |        0.21 |           0   |             0.0209908 |    0.207 |      -0.08 |     0.207 |       -0.08 |           0.0184292 |
|       3 |        0.09 |          -1.3 |             0.13153   |    0.087 |      -1.37 |     0.087 |       -1.37 |           0.13153   |
|       4 |        0.14 |          -1.2 |             0.0763669 |    0.13  |      -1.24 |     0.13  |       -1.24 |           0.07636   |
|       5 |        0.2  |          -1   |             0.0402471 |    0.19  |      -1.05 |     0.19  |       -1.05 |           0.0402451 |
|       6 |        0.25 |          -0.9 |             0.0209932 |    0.24  |      -0.93 |     0.24  |       -0.93 |           0.0185339 |
|       7 |        0.28 |          -1   |             0.016885  |    0.28  |      -1.01 |     0.28  |       -1.01 |           0.0133396 |
|       8 |        0.43 |          -1   |             0.0132542 |    0.438 |      -1    |     0.438 |       -1    |           0.0132541 |
|       9 |        1.3  |          -1   |             0.0244945 |    1.29  |      -1.03 |     1.29  |       -1.03 |           0.024493  |

### blue
#### Optimization progression:
|   layer |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|--------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|       2 |        0.21 |           0   |             0.0248394 |   0.208  |      -0.08 |    0.208  |       -0.08 |           0.0216796 |
|       3 |        0.09 |          -1.3 |             0.13192   |   0.087  |      -1.37 |    0.087  |       -1.37 |           0.13192   |
|       4 |        0.13 |          -1.2 |             0.07505   |   0.126  |      -1.23 |    0.126  |       -1.23 |           0.07505   |
|       5 |        0.2  |          -1   |             0.0398371 |   0.192  |      -1.04 |    0.192  |       -1.04 |           0.0398356 |
|       6 |        0.25 |          -0.9 |             0.0292834 |   0.24   |      -0.95 |    0.24   |       -0.95 |           0.0227437 |
|       7 |        0.29 |          -1   |             0.0194895 |   0.28   |      -1.03 |    0.28   |       -1.03 |           0.0140941 |
|       8 |        0.46 |          -1   |             0.0145899 |   0.455  |      -1.01 |    0.455  |       -1.01 |           0.0119646 |
|       9 |       10    |          -1.1 |             0.0283354 |   9.9999 |      -1.08 |    9.9999 |       -1.08 |           0.0234527 |

### green
#### Optimization progression:
|   layer |   initial_r |   initial_eta |   kstest_stat_initial |   best_r |   best_eta |   iter1_r |   iter1_eta |   kstest_stat_iter1 |
|--------:|------------:|--------------:|----------------------:|---------:|-----------:|----------:|------------:|--------------------:|
|       2 |        0.21 |           0   |             0.0210254 |    0.204 |      -0.1  |     0.204 |       -0.1  |           0.0192117 |
|       3 |        0.09 |          -1.3 |             0.13308   |    0.087 |      -1.37 |     0.087 |       -1.37 |           0.13308   |
|       4 |        0.13 |          -1.2 |             0.0778    |    0.12  |      -1.24 |     0.12  |       -1.24 |           0.0778    |
|       5 |        0.17 |          -1.1 |             0.0431227 |    0.161 |      -1.14 |     0.161 |       -1.14 |           0.0431176 |
|       6 |        0.22 |          -1   |             0.0277339 |    0.224 |      -0.97 |     0.224 |       -0.97 |           0.0206473 |
|       7 |        0.28 |          -1   |             0.0159148 |    0.271 |      -1.02 |     0.271 |       -1.02 |           0.0135019 |
|       8 |        0.42 |          -1   |             0.0123914 |    0.42  |      -1    |     0.42  |       -1    |           0.0123914 |
|       9 |        1.3  |          -1   |             0.0253345 |    1.29  |      -1.03 |     1.29  |       -1.03 |           0.025333  |
