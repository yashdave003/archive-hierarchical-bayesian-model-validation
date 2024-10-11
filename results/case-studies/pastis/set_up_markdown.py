import os
import pandas as pd
from pathlib import Path
import git
import math

def get_plot(filename):
    return os.path.join(str(plots_path.relative_to(case_study_path)), filename)

def create_image_grid(plot_name, layers, cols=2, plot_type="grid"):
    rows = math.ceil(len(layers) / cols)
    grid = "<table>\n"
    for i in range(rows):
        grid += "  <tr>\n"
        for j in range(cols):
            idx = i * cols + j
            if idx < len(layers):
                layer = layers[idx]
                if plot_type == "grid":
                    filename = f"{plot_name}_layer{layer}.jpg"
                elif plot_type == "compare":
                    filename = f"compare_cdf_pdf_layer_{layer}.jpg"
                grid += f"    <td><img src=\"{get_plot(filename)}\" alt=\"Layer {layer} Plot\"></td>\n"
            else:
                grid += "    <td></td>\n"
        grid += "  </tr>\n"
    grid += "</table>\n"
    return grid

def generate_markdown_report(base_path, output_file):
    global case_study_path, plots_path
    case_study_path = Path(os.path.join(base_path, "results", "case-studies", "pastis"))
    wavelet_path = Path(os.path.join(case_study_path, "wavelet", "approx1e5", "gray"))
    cdf_path = Path(os.path.join(wavelet_path, "CDFs"))
    csv_path = Path(os.path.join(wavelet_path, "CSVs"))
    plots_path = Path(os.path.join(wavelet_path, "plots"))

    master_df = pd.read_csv(os.path.join(csv_path, "master_df.csv"))

    markdown_content = f"""
# PASTIS Dataset - {pd.Timestamp.now().strftime('%Y-%m-%d')}

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

{create_image_grid("full_grid_search_combo_plot", range(2, 9), cols=2)}

### Compare CDF PDF Plots

{create_image_grid("compare_cdf_pdf", range(2, 10), cols=1, plot_type="compare")}

## Results

Here are the best parameters from the proposed prior distribution

{master_df[['total_samples', 'best_r', 'best_eta', 'kstest_stat_best']].to_markdown()}

Here are the KS statistics along with the cutoff for a p-value of 0.05.

{master_df.filter(regex='total_samples|kstest_stat.*').to_markdown()}

## Major Take-aways

[Add major conclusions and insights]
"""

    with open(output_file, 'w') as f:
        f.write(markdown_content)

    print(f"Markdown report generated: {output_file}")

# Usage
base_path = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
output_file = os.path.join("results", "case-studies", "pastis", "pastis.md")
generate_markdown_report(base_path, output_file)

output_file = os.path.join("results", "reports", "pastis.md")
generate_markdown_report(base_path, output_file)