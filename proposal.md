# Project Plan

### Project goal
The goal of the project is to create an installable package written in Python that measures distances between phylogenetic trees using different metrics. `distmetric` aims to standardize and centralize different methods used to calculate phylogenetic tree distances in one package, making it more accessible for researchers to utilize and compare between metrics easily. This package will be used in an API and will preferably be accessed via Jupyter Notebook.

### Code Description and File Structure
The package will organized with three types of files.
1. Each `.py` file within the src folder with the exception of `sampling.py` will contain all relevant functions and class objects created for each tree comparison method (ex. `quartets.py`, `robinsonfoulds.py`). `sampling.py` will feature functions that can be used across all tree comparison methods (ex. indicating calculating distances between pairwise or random trees, generating random trees for testing)
2. Dunder files and `setup.py` help make the package installable and operational.
3. `README.md` and `proposal.md` will contain informative write-ups for this package.

Current file structure:
```bash
.
├── README.md
├── proposal.md
├── setup.py
└── src
    ├── __init__.py
    ├── quartets.py
    └── sampling.py
```
Dependencies/libraries the code will utilize include:
1. `pandas`: to output and store resulting distance calculations in a dataframe
2. `numpy`: to implement statistical calculations
3. `toytree`: to read trees in newick format, render phylogenetic trees, and generate random trees for testing

### Data Description: Sample User input and output
The user will provide `distmetric` with a series of phylogenetic trees in newick format as a string. Toytree will be used to parse and read each newick string as a phylogenetic tree. An example of a tree written in newick format is demonstrated below. After reading in each tree, `distmetric` will then process these trees by calculating distance metrics according to whichever method the user indicates (ex. quartets vs. Robinson-Foulds). Users can also indicate if they would like to calculate these distance metrics in a pairwise or random fashion (ex. if a user provides a number of genealogies along the same genome). The resulting calculated distance metrics will be stored and returned as a pandas dataframe. 

Sample input:
```python
import toytree
newick = "((r9:0.875,r8:0.875)100:0.125,(r7:0.875,(r6:0.75,(r5:0.625,(r4:0.5,(r3:0.375,(r2:0.25,(r1:0.125,r0:0.125)100:0.125)100:0.125)100:0.125)100:0.125)100:0.125)100:0.125)100:0.125);"
tre0 = toytree.tree(newick)
tre0.draw()
```

Sample output (pandas dataframe rendered in markdown):
```
'|    | trees   |   Quartet intersection |
 |---:|:--------|-----------------------:|
 |  0 | 1, 2    |               0.942857 |
 |  1 | 2, 3    |               0.92381  |
 |  2 | 3, 4    |               0.733333 |
 |  3 | 4, 5    |               0.790476 |
 |  4 | 5, 6    |               0.942857 |'
```

### Description or demonstration of user interaction
The user will ideally import the package on Jupyter notebook and execute the different commands with the class objects.
```
import distmetric

quartets.get_quartets()
quartets.compare_quartets()
```

### Existing programs and references
Existing programs are mostly packages that are focused on calculating the RobinsonFoulds metric. These examples include [ETE](http://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html#robinson-foulds-distance) and [Dendropy](https://dendropy.org/library/treecompare.html?highlight=robinson%20foulds#dendropy.calculate.treecompare.robinson_foulds_distance), which are both written in Python. `distmetric` attempts to explore other phylogenetic distance metrics, with the goal of creating readable and accessible code to various metrics within the same package. 
