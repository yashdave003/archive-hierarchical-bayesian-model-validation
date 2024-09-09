#!/bin/bash

echo "Setting up the hbmv environment..."

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Error: Conda is not installed or not in the system PATH."
    echo "Please install Conda and try again."
    exit 1
fi

# Create conda environment
echo "Creating conda environment..."
conda env create -f environment.yml

# Activate conda environment
echo "Activating conda environment..."
source ~/miniconda3/etc/profile.d/conda.sh || source ~/anaconda3/etc/profile.d/conda.sh
conda activate hbmv

# Install IPython kernel
echo "Installing IPython kernel..."
python -m ipykernel install --user --name=hbmv

echo "Setup completed successfully!"
echo "To activate the environment, run:"
echo "    conda activate hbmv"