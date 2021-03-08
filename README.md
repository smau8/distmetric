# distmetric
The goal of the project is to create an installable package written in Python that measures distances between 
phylogenetic trees using different methods/metrics. The package will primarily be focused on being used in API (Jupyter Notebook).

### In development

### Package installation
Developers can install the package `distmetric` via conda or by directly cloning the GitHub repository. As demonstrated below, if installing via conda, three dependencies/additional python packages–`toytree`, `pandas`, `numpy`–will need to be installed separately prior to using this package. For development purposes, this package can be cloned and installed via pip in "development mode" so that the package can then be used locally on a user's computer and any changes made to the code will be reflected immediately when using the package. 
```
# install via conda
conda install toytree pandas numpy -c conda-forge  # install dependencies
conda install distmetric

# installing directly via cloning GitHub repository
git clone https://github.com/smau8/distmetric.git
cd ./distmetric
pip install -e .
```
