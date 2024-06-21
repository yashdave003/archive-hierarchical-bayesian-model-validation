# hierarchical-bayesian-model-validation

Repository to store code relating to [Hierarchical Bayesian Model](https://iopscience.iop.org/article/10.1088/1361-6420/ab4d92) Validation project.

## Repo Setup

### Cloning the Repo
After you've installed quarto, go into your terminal on your *local* device and type 

`git clone https://github.com/yashdave003/hierarchical-bayesian-model-validation.git` 

### Environment Setup

This section will ensure that you have all the necessary packages. We recommend using Conda ([download here](https://www.anaconda.com/download)) to keep track of your environment. 

Run the following in your terminal within the main directory: 

```
conda create --name hbmv 
conda activate hbmv
pip3 install -r requirements.txt # will take a while
ipython kernel install --user
```

If you get an `error: externally-managed-environment` on the third line, run `pip3 install -r requirements.txt --break-system-packages`

Remember to always activate the right environment before running anything with `conda activate hbmv`.
