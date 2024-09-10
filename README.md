# hierarchical-bayesian-model-validation

Repository to store code relating to [Hierarchical Bayesian Model](https://iopscience.iop.org/article/10.1088/1361-6420/ab4d92) Validation project.

## Environment Setup

This project uses conda for package management and requires Python 3.11. The conda environment is named `hbmv`. The setup process differs slightly depending on your operating system.

### Prerequisites

- Ensure you have Conda installed on your system. If not, download and install it from [Anaconda's website](https://www.anaconda.com/products/distribution).

### Setup Instructions

#### For Mac/Linux Users

1. Open Terminal.

2. Navigate to the project directory:
   ```
   cd path/to/project
   ```

3. Make the setup script executable:
   ```
   chmod +x setup.py
   ```

4. Run the setup script:
   ```
   ./setup.py
   ```

5. After the script completes, activate the environment:
   ```
   conda activate hbmv
   ```

#### For Windows Users

1. Open Command Prompt or PowerShell.

2. Navigate to the project directory:
   ```
   cd path\to\project
   ```

3. Run the setup script:
   ```
   bash -i setup.sh
   ```

4. After the script completes, activate the environment:
   ```
   conda activate hbmv
   ```

### Manual Setup (if automated setup fails)

If you encounter issues with the automated setup, you can follow these manual steps:

1. Create a new conda environment:
   ```
   conda env create -f environment.yml
   ```

2. Activate the environment:
   ```
   conda activate hbmv
   ```

3. Install IPython kernel:
   ```
   python -m ipykernel install --user --name=hbmv
   ```

## Package List

The project requires Python 3.11 and the following packages:

- numpy==2.1.1
- pandas==2.2.2
- scipy==1.14.1
- PyWavelets==1.7.0
- Pillow==10.4.0
- tqdm==4.66.5
- seaborn==0.13.2
- matplotlib (latest version)
- nibabel==5.2.1
- matlabengine==24.1.2 (installed via pip)

## Troubleshooting

If you encounter any issues during setup:

1. Ensure Conda is up to date:
   - For Mac/Linux:
     ```
     conda update -n base -c defaults conda
     ```
   - For Windows:
     ```
     conda update -n base -c defaults conda
     ```

2. Clear the Conda cache:
   - For Mac/Linux:
     ```
     conda clean -a
     ```
   - For Windows:
     ```
     conda clean -a
     ```

3. If you're using Mac and encounter permission issues, try prefixing commands with `sudo`.

4. On Windows, if you get "conda is not recognized as an internal or external command", you may need to add Conda to your system PATH or use the Anaconda Prompt instead of the regular Command Prompt.

5. If problems persist, try creating the environment manually and install packages one by one using `conda install` or `pip install`.

For any other issues, please refer to the official documentation of the respective packages or seek assistance from the project maintainers.