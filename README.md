# Project Plan

### Project goal
The goal of the project is to create an installable package written in Python that measures distances between phylogenetic trees using different methods/metrics. The package will primarily be focused on being used in API (Jupyter Notebook).  

### Code Description
Create a class object for each tree comparison method (ex. Robinson-Foulds, Quartets) and within each tree object define functions that users can apply to their trees.
Dependencies/libraries the code will utilize include:
1. `pandas`: to output and store resulting distance calculations in a dataframe
2. `numpy`: to implement statistical calculations
3. `toytree`: to read trees in newick format, render phylogenetic trees, and generate random trees for testing

### Data Description
User input will be a series of phylogenetic trees that will be parsed in newick format.
Output will be distance metrics presented using pandas dataframes.

### Description or demonstration of user interaction
The user will ideally import the package on Jupyter notebook and execute the different commands with the class objects.
```
import distmetric
distmetric.robinsonfoulds()
distmetric.quartets()
```
