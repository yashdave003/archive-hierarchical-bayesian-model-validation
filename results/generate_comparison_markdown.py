import os
import pandas as pd
from pathlib import Path
import git
import argparse

def get_project_root():
    return Path(git.Repo('.', search_parent_directories=True).working_tree_dir)

def get_relative_plot_path(plots_path, output_path, filename):
    """Get the relative path for a plot file from the output path."""
    plot_full_path = os.path.abspath(os.path.join(plots_path, filename))
    relative_path = os.path.relpath(plot_full_path, start=output_path)
    return relative_path

def create_image_grid(plots_paths, identifiers, output_path, plot_name, groups, cols=2, plot_type="grid", img_width="45%"):
    rows = -(-len(groups) // cols)
    grid = ""
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            if idx < len(groups):
                group = groups[idx]
                grid += '<div style="display: flex; justify-content: space-around; margin-bottom: 20px;">\n'
                for plot_path, identifier in zip(plots_paths, identifiers):
                    if plot_type == "grid":
                        filename = f"{plot_name}_layer{group}.jpg"
                    elif plot_type == "compare":
                        filename = f"compare_cdf_pdf_layer_{group}.jpg"
                    full_path = os.path.join(plot_path, filename)
                    if os.path.exists(os.path.join(get_project_root(), "results", full_path)):
                        grid += f'<div style="text-align: center;">\n'
                        grid += f'<img src="{get_relative_plot_path(plot_path, output_path, filename)}" alt="Layer {group} Plot" width="{img_width}"/>\n'
                        grid += f'<p>{identifier}</p>\n'
                        grid += '</div>\n'
                grid += '</div>\n'
        grid += "\n"
    return grid

def create_comparison_grid(plots_paths, identifiers, output_path, groups, plot_pairs, cols=2, img_width="80%"):
    rows = -(-len(groups) // cols)
    grid = ""
    for i in range(rows):
        grid += '<div style="display: flex; flex-direction: column; margin-bottom: 40px;">\n'
        for j in range(cols):
            idx = i * cols + j
            if idx < len(groups):
                group = groups[idx]
                grid += f'  <h3>Layer {group}</h3>\n'
                for plot_path, identifier in zip(plots_paths, identifiers):
                    grid += f'  <div style="margin-bottom: 20px;">\n'
                    grid += f'    <h4>{identifier}</h4>\n'
                    grid += f'    <div style="display: flex; gap: 20px; justify-content: center;">\n'
                    for filename_template, label in plot_pairs:
                        filename = filename_template.format(group)
                        full_path = os.path.join(plot_path, filename)
                        if os.path.exists(os.path.join(get_project_root(), "results", full_path)):
                            grid += f'      <div style="text-align: center;">\n'
                            grid += f'        <img src="{get_relative_plot_path(plot_path, output_path, filename)}" alt="{label} Layer {group}" style="width: {img_width};">\n'
                            grid += f'        <p>{label}</p>\n'
                            grid += f'      </div>\n'
                    grid += f'    </div>\n'
                    grid += f'  </div>\n'
        grid += '</div>\n\n'
    return grid

def merge_dataframes_with_prefixes(dfs, identifiers):
    """Merge dataframes side by side with prefixed columns based on identifiers."""
    merged_df = pd.DataFrame(index=dfs[0].index)
    
    for df, identifier in zip(dfs, identifiers):
        prefix = identifier[0].upper() + '_'  # Take first letter of identifier and capitalize
        for col in df.columns:
            merged_df[prefix + col] = df[col]
    
    return merged_df

def generate_comparative_markdown_report(data_names):
    """Generate comparative markdown report for multiple datasets."""
    # Parse first data_name to get common components
    first_data = data_names[0].split('-')
    dataset_name = first_data[1]
    representation = first_data[2]
    channel = first_data[3]
    
    # Get identifiers (the varying part between data_names)
    identifiers = [name.split('-')[0] for name in data_names]
    comparison_name = f"{identifiers[0]}VS{'VS'.join(identifiers[1:])}-{dataset_name}-{representation}-{channel}"
    
    # Set up paths
    base_path = os.path.join(get_project_root(), "results")
    plots_paths = []
    master_dfs = []
    
    for data_name in data_names:
        identifier = data_name.split('-')[0]
        plots_path = os.path.join("case-studies", dataset_name, representation, identifier, channel, "plots")
        csv_path = os.path.join("case-studies", dataset_name, representation, identifier, channel, "CSVs")
        plots_paths.append(plots_path)
        
        # Read data
        index_col = 'layer' if representation == 'wavelet' else 'band'
        df = pd.read_csv(os.path.join(base_path, csv_path, "master_df.csv"), index_col=index_col)
        master_dfs.append(df)
    
    # Merge dataframes with prefixes
    merged_df = merge_dataframes_with_prefixes(master_dfs, identifiers)
    layers_or_bands = master_dfs[0].index.tolist()

    # Define plot pairs
    combo_plot_pairs = [
        ("full_grid_search_combo_plot_layer{}.jpg", "Full Grid Search"),
        ("optimized_full_grid_search_combo_plot_layer{}.jpg", "Fine Grid Search")
    ]

    output_path = os.path.join(base_path)

    markdown_content = f"""# Comparative Analysis: {dataset_name.upper()} Dataset ({representation.capitalize()}) - {pd.Timestamp.now().strftime('%Y-%m-%d')}
## Dataset Variations
* **Variations compared:** {', '.join(identifiers)}
* **Image Type:** {channel.capitalize()}
* **Representation:** {representation.capitalize()}

## Comparative Results

### Full Grid Search Combo Plots Comparison
{create_comparison_grid(plots_paths, identifiers, output_path, layers_or_bands, combo_plot_pairs, cols=1, img_width="80%")}

### Compare CDF PDF Plots
{create_image_grid(plots_paths, identifiers, output_path, "compare_cdf_pdf", layers_or_bands, cols=1, plot_type="compare", img_width="90%")}

## Comparative Parameter Analysis

### Best parameters comparison:
{merged_df[[f'{id[0].upper()}_total_samples' for id in identifiers] +
           [f'{id[0].upper()}_best_r' for id in identifiers] + 
           [f'{id[0].upper()}_best_eta' for id in identifiers] +
           [f'{id[0].upper()}_kstest_stat_best' for id in identifiers]].round(7).to_markdown()}

## Individual Analyses
"""
    # Add individual analyses
    for identifier, df in zip(identifiers, master_dfs):
        markdown_content += f"""
### {identifier}
#### Optimization progression:
{df.filter(regex='.*_r$|.*_eta$|iter.*').round(7).to_markdown()}
"""

    output_file = os.path.join(base_path, "draft_reports", f"{comparison_name}.md")
    os.makedirs(os.path.join(base_path, "draft_reports"), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    print(f"Comparative markdown report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate comparative markdown report for multiple dataset analyses')
    parser.add_argument('data_names', nargs='+', help='Space-separated data names in the format <size>-<dataset_name>-<representation>-<channel>')
    args = parser.parse_args()

    generate_comparative_markdown_report(args.data_names)