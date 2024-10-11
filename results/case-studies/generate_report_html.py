import os
import pandas as pd
from pathlib import Path
import git

def get_plot(plots_path, case_study_path, filename):
    return os.path.join(str(plots_path.relative_to(case_study_path)), filename)

def create_image_grid(plots_path, case_study_path, plot_name, layers, cols=2, plot_type="grid", img_width="60%"):
    rows = -(-len(layers) // cols)  # Ceiling division
    grid = f"<table style='width: 100%;'>\n"
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
                grid += f"    <td style='width: {100/cols}%;'><img src=\"{get_plot(plots_path, case_study_path, filename)}\" alt=\"Layer {layer} Plot\" style='width: {img_width}; height: auto;'></td>\n"
            else:
                grid += f"    <td style='width: {100/cols}%;'></td>\n"
        grid += "  </tr>\n"
    grid += "</table>\n"
    return grid

def generate_html_report(dataset_name):
    base_path = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
    case_study_path = Path(os.path.join(base_path, "results", "case-studies", dataset_name))
    wavelet_path = Path(os.path.join(case_study_path, "wavelet", "approx1e5", "gray"))
    cdf_path = Path(os.path.join(wavelet_path, "CDFs"))
    csv_path = Path(os.path.join(wavelet_path, "CSVs"))
    plots_path = Path(os.path.join(wavelet_path, "plots"))

    master_df = pd.read_csv(os.path.join(csv_path, "master_df.csv"))

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dataset_name.upper()} Dataset Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 1200px; margin: 0 auto; }}
        h1, h2 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>{dataset_name.upper()} Dataset - {pd.Timestamp.now().strftime('%Y-%m-%d')}</h1>

    <h2>Dataset Description</h2>
    <ul>
        <li><strong>Original source:</strong> [Add source information here]</li>
        <li><strong>Sizes:</strong> [Add size information here]</li>
        <li><strong>Image Type:</strong> Gray</li>
        <li><strong>Date range covered:</strong> [Add date range here]</li>
        <li><strong>Number of Images (and channels):</strong> [Add number of images here]</li>
    </ul>

    <h2>Why did we choose it?</h2>
    <p>[Add reasons for choosing this dataset]</p>

    <h2>Cleaning - what did we do?</h2>
    <p>[Add cleaning process details]</p>

    <h2>Hypotheses</h2>
    <p>[Add hypotheses, basis/representation used, and assumptions about signal subsets]</p>

    <h2>Tests and Questions</h2>

    <h3>Full Grid Search Combo Plots</h3>
    {create_image_grid(plots_path, case_study_path, "full_grid_search_combo_plot", range(2, 9), cols=2)}

    <h3>Compare CDF PDF Plots</h3>
    {create_image_grid(plots_path, case_study_path, "compare_cdf_pdf", range(2, 10), cols=1, plot_type="compare", img_width="90%")}

    <h2>Results</h2>

    <h3>Best parameters from the proposed prior distribution:</h3>
    {master_df[['total_samples', 'best_r', 'best_eta', 'kstest_stat_best']].to_html()}

    <h3>KS statistics along with the cutoff for a p-value of 0.05:</h3>
    {master_df.filter(regex='total_samples|kstest_stat.*').to_html()}

    <h2>Major Take-aways</h2>
    <p>[Add major conclusions and insights]</p>

</body>
</html>
"""

    output_file = os.path.join(case_study_path, f"{dataset_name}.html")
    with open(output_file, 'w') as f:
        f.write(html_content)

    output_file = os.path.join(base_path, "results", "reports", f"{dataset_name}.html")
    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"HTML report generated: {output_file}")

if __name__ == "__main__":
    dataset_name = input("Enter the dataset name: ")
    generate_html_report(dataset_name)