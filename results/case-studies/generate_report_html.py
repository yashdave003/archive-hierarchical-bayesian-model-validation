import os
import pandas as pd
from pathlib import Path
import git
import argparse

def get_plot(plots_path, case_study_path, filename):
    return os.path.join(str(plots_path.relative_to(case_study_path)), filename)

def create_image_grid(plots_path, case_study_path, plot_name, layers, cols=2, plot_type="grid", img_width="45%"):
    rows = -(-len(layers) // cols)  # Ceiling division
    grid = f"<table width='100%'>\n"
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
                grid += f"    <td width='{100/cols}%'><img src=\"{get_plot(plots_path, case_study_path, filename)}\" alt=\"Layer {layer} Plot\" width=\"{img_width}\"/></td>\n"
            else:
                grid += f"    <td width='{100/cols}%'></td>\n"
        grid += "  </tr>\n"
    grid += "</table>\n"
    return grid

def generate_html_report(dataset_name, representation):
    base_path = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
    case_study_path = Path(os.path.join(base_path, "results", "case-studies", dataset_name))
    representation_path = Path(os.path.join(case_study_path, representation, "approx1e5", "gray"))
    cdf_path = Path(os.path.join(representation_path, "CDFs"))
    csv_path = Path(os.path.join(representation_path, "CSVs"))
    plots_path = Path(os.path.join(representation_path, "plots"))

    index_col = 'layer' if representation == 'wavelet' else 'band'
    master_df = pd.read_csv(os.path.join(csv_path, "master_df.csv"), index_col=index_col)

    layers_or_bands = master_df.index.tolist()

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dataset_name.upper()} Dataset ({representation.capitalize()}) Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 1200px; margin: 0 auto; }}
        h1, h2 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>{dataset_name.upper()} Dataset ({representation.capitalize()}) - {pd.Timestamp.now().strftime('%Y-%m-%d')}</h1>

    <h2>Dataset Description</h2>
    <ul>
        <li><strong>Original source:</strong> [Add source information here]</li>
        <li><strong>Sizes:</strong> [Add size information here]</li>
        <li><strong>Image Type:</strong> Gray</li>
        <li><strong>Date range covered:</strong> [Add date range here]</li>
        <li><strong>Number of Images (and channels):</strong> [Add number of images here]</li>
        <li><strong>Representation:</strong> {representation.capitalize()}</li>
    </ul>

    <h2>Why did we choose it?</h2>
    <p>[Add reasons for choosing this dataset]</p>

    <h2>Cleaning - what did we do?</h2>
    <p>[Add cleaning process details]</p>

    <h2>Hypotheses</h2>
    <p>[Add hypotheses, basis/representation used, and assumptions about signal subsets]</p>

    <h2>Tests and Questions</h2>

    <h3>Full Grid Search Combo Plots</h3>
    {create_image_grid(plots_path, case_study_path, f"full_grid_search_combo_plot_{representation}", layers_or_bands, cols=2, img_width="90%")}

    <h3>Compare CDF PDF Plots</h3>
    {create_image_grid(plots_path, case_study_path, f"compare_cdf_pdf_{representation}", layers_or_bands, cols=1, plot_type="compare", img_width="90%")}

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

    output_file = os.path.join(case_study_path, f"{dataset_name}_{representation}.html")
    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"HTML report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an HTML report for a dataset.")
    parser.add_argument("dataset_name", help="Name of the dataset")
    parser.add_argument("representation", choices=['wavelet', 'fourier'], help="Type of representation (wavelet or fourier)")
    args = parser.parse_args()

    generate_html_report(args.dataset_name, args.representation)