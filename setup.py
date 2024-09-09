#!/usr/bin/env python3

import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")
        sys.exit(1)

def main():
    print("Setting up the hbmv environment...")

    # Check if conda is installed
    try:
        subprocess.run(["conda", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Error: Conda is not installed or not in the system PATH.")
        print("Please install Conda and try again.")
        sys.exit(1)

    # Create conda environment
    print("Creating conda environment...")
    run_command("conda env create -f environment.yml")

    # Activate conda environment
    print("Activating conda environment...")
    activate_command = "conda activate hbmv"
    
    if sys.platform.startswith('win'):
        activate_command = f"call {activate_command}"
    else:
        activate_command = f"source {os.path.expanduser('~/miniconda3/etc/profile.d/conda.sh')} && {activate_command}"

    # Install IPython kernel
    print("Installing IPython kernel...")
    run_command(f"{activate_command} && python -m ipykernel install --user --name=hbmv")

    print("\nSetup completed successfully!")
    print("To activate the environment, run:")
    print("    conda activate hbmv")

if __name__ == "__main__":
    main()