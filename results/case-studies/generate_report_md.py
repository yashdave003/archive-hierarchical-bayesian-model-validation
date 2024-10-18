import os
import pandas as pd
from pathlib import Path
import git

def get_plot(plots_path, case_study_path, filename):
    return os.path.join(str(plots_path.relative_to(case_study_path)), filename)

def create_image_grid(plots_path, case_study_path, plot_name, groups, cols=2, plot_type="grid", img_width="45%"):
    rows = -(-len(groups) // cols)  # Ceiling division
    grid = ""
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            if idx < len(groups):
                group = groups[idx]
                if plot_type == "grid":
                    filename = f"{plot_name}_layer{group}.jpg"
                elif plot_type == "compare":
                    filename = f"compare_cdf_pdf_layer_{group}.jpg"
                grid += f'<img src="{get_plot(plots_path, case_study_path, filename)}" alt="Layer {group} Plot" width="{img_width}"/>\n'
        grid += "\n"
    return grid

def generate_markdown_report(dataset_name, representation):
    base_path = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
    case_study_path = Path(os.path.join(base_path, "results", "case-studies", dataset_name))
    representation_path = Path(os.path.join(case_study_path, representation, "approx1e5", "gray"))
    csv_path = Path(os.path.join(representation_path, "CSVs"))
    plots_path = Path(os.path.join(representation_path, "plots"))

    index_col = 'layer' if representation == 'wavelet' else 'band'
    master_df = pd.read_csv(os.path.join(csv_path, "master_df.csv"), index_col=index_col)

    layers_or_bands = master_df.index.tolist()

    markdown_content = f"""
# {dataset_name.upper()} Dataset ({representation.capitalize()}) - {pd.Timestamp.now().strftime('%Y-%m-%d')}

## Dataset Description

* **Original source:** [Add source information here]
* **Sizes:** [Add size information here]
* **Image Type:** Gray
* **Date range covered:** [Add date range here]
* **Number of Images (and channels):** [Add number of images here]
* **Representation:** {representation.capitalize()}

## Why did we choose it?

[Add reasons for choosing this dataset]

## Cleaning - what did we do?

[Add cleaning process details]

## Hypotheses

[Add hypotheses, basis/representation used, and assumptions about signal subsets]

## Tests and Questions

### Full Grid Search Combo Plots

{create_image_grid(plots_path, case_study_path, f"full_grid_search_combo_plot", layers_or_bands, cols=2, img_width="45%")}

### Compare CDF PDF Plots

{create_image_grid(plots_path, case_study_path, f"compare_cdf_pdf", layers_or_bands, cols=1, plot_type="compare", img_width="90%")}

## Results

Here are the best parameters from the proposed prior distribution:

{master_df[['total_samples', 'best_r', 'best_eta', 'kstest_stat_initial', 'kstest_stat_best', 'kstest_stat_cutoff_0.05', 'n_pval_0.05']].to_markdown()}

Here are the KS statistics along with the cutoff for a p-value of 0.05:

{master_df.filter(regex='total_samples|kstest_stat.*').to_markdown()}

Here are the comparisons with other common priors (Gaussian, Laplace, Student t):

{master_df.filter(regex='param_.*|best_.*|kstest_stat_.*[^0-9]$').to_markdown()}

All the columns you can access:

{list(master_df.columns)}

## Major Take-aways

[Add major conclusions and insights]
"""

    output_file = os.path.join(case_study_path, f"{dataset_name}_{representation}.md")
    with open(output_file, 'w') as f:
        f.write(markdown_content)

    print(f"Markdown report generated: {output_file}")

if __name__ == "__main__":
    args = input("Enter the dataset name: ").split()
    dataset_name = args[0]
    if len(args) == 2:
        transform = args[1]

    generate_markdown_report(dataset_name, transform)