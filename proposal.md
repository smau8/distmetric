# Project Plan

### Project goal
The goal of the project is to create an installable package written in Python that measures distances between phylogenetic trees using different metrics. `distmetric` aims to standardize and centralize calculating phylogenetic tree distances across different methods in one package, making it more accessible for researchers to compare between metrics easily. This package will primarily be focused on being used in API and will preferably be accessed via Jupyter Notebook.

### Code Description
Create a class object for each tree comparison method (ex. Robinson-Foulds, Quartets) and within each tree object define functions that users can apply to their trees.
Dependencies/libraries the code will utilize include:
1. `pandas`: to output and store resulting distance calculations in a dataframe
2. `numpy`: to implement statistical calculations
3. `toytree`: to read trees in newick format, render phylogenetic trees, and generate random trees for testing

### Data Description/User input
The user will provide `distmetric` with a series of phylogenetic trees in newick format as a string. Toytree will be used to parse the newick string and render it as a phylogenetic tree. An example of a tree written in newick is demonstrated here (adapted example from [Toytree tutorial](https://toytree.readthedocs.io/en/latest/4-tutorial.html#Parsing-Newick/Nexus-data):
```
newick = "((a:1,b:1)90:3,(c:3,(d:1, e:1)100:2)100:1)100;"
tre0 = toytree.tree(newick, tree_format=0)
```
`distmetric` will then process these trees and compare them by calculating pairwise distances or random distances.
Output will be distance metrics presented using pandas dataframes.

### Description or demonstration of user interaction
The user will ideally import the package on Jupyter notebook and execute the different commands with the class objects.
```
import distmetric
distmetric.robinsonfoulds()
distmetric.quartets()
```

### Existing programs
Current programs existing are mostly packages that are focused on an individual phylogenetic tree metric and these packages are written in a number of different languages. 
