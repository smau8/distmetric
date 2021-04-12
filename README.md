# distmetric
## Calculating distance metrics between phylogenetic trees
The goal of the project is to create an installable package written in Python that measures distances between 
phylogenetic trees using different methods/metrics. `distmetric` will be used to complement existing Python phylogenomic tree libraries and support growing Python package development in phylogenetics. The package will primarily be focused on being used in API (Jupyter Notebook).

### In development

### Package installation
Developers can install the package `distmetric` directly by cloning the GitHub repository. After cloning, it is recommended to install the package locally via pip so that the package can used in "development mode" and any changes made to the code will be reflected immediately when using the package. As demonstrated below, three dependencies/additional python packages–`toytree`, `pandas`, `numpy`–will need to be installed separately prior to using this package.
```
# install dependencies via conda
conda install toytree pandas numpy -c conda-forge

# installing directly via cloning GitHub repository
git clone https://github.com/smau8/distmetric.git
cd ./distmetric
pip install -e .
```

### Working example
**Overview**
The package currently is able to measure distances between phylogenetic trees using the Quartets and Robinson Foulds method with the `Quartets` and `RobinsonFoulds` class objects. Users can also indicate how they would like to measure these distances and are provided with three options: pairwise (compare between tree 1 vs. 2, tree 2 vs. 3 etc.), random (compare between tree 1 vs. 6, 5 vs. 2) and consensus (compare each tree with the consensus tree). The output is presented using a pandas data frame and users can interpret their data using the `SumStat` class object, which returns the mean, standard deviation and histogram distribution of the distance metrics. 

### 1) INPUT: Generating/Parsing trees
Generating trees using the Generator class object in `Sample.py` as input. Display trees using multitrees from toytree. 
```python
# import package
import distmetric
```
```python
# generate 10 random trees as input with Generator class object, defaults to 10 tip trees
TREES = distmetric.Generator(10)
randomtrees = TREES.get_randomtrees()

# examining what the trees look like:
toytree.mtree(randomtrees).draw(ts = 'c', nrows=2, ncols=5);
```
![tree](https://github.com/smau8/distmetric/blob/main/demos/demo-working-example1.png)

### 2) ANALYSIS: Calculate distances between trees in given user input
Calculate distance metrics in 1) pairwise order, 2) random order, or 3) relative to a consensus tree. 
Implement analysis with either the Robinson-Foulds or Quartets method. 

```python
# calculate quartet distances between each tree and the consensus tree
quart = distmetric.Quartets(randomtrees, "consensus")
quart.run()
quart.output
# see below for data frame results
```
|    | trees        |   Quartet_intersection |
|---:|:-------------|-----------------------:|
|  0 | 0, consensus |               0.761905 |
|  1 | 1, consensus |               1        |
|  2 | 2, consensus |               1        |
|  3 | 3, consensus |               0.928571 |
|  4 | 4, consensus |               0.761905 |
|  5 | 5, consensus |               1        |
|  6 | 6, consensus |               0.8      |
|  7 | 7, consensus |               0.847619 |
|  8 | 8, consensus |               0.761905 |
|  9 | 9, consensus |               1        |

```python
# calculate Robinson Foulds distances in a pairwise manner
rfs = distmetric.RF(randomtrees, "pairwise")
rfs.run()
rfs.output
# see below for data frame results
```
|    | trees   |        RF |
|---:|:--------|----------:|
|  0 | 0, 1    | 0.277778  |
|  1 | 1, 2    | 0         |
|  2 | 2, 3    | 0.0555556 |
|  3 | 3, 4    | 0.333333  |
|  4 | 4, 5    | 0.277778  |
|  5 | 5, 6    | 0.222222  |
|  6 | 6, 7    | 0.111111  |
|  7 | 7, 8    | 0.277778  |
|  8 | 8, 9    | 0.277778  |

```python
# calculate Robinson Foulds distances in a random manner
rfs = distmetric.RF(randomtrees, "random")
rfs.run()
rfs.output
```
|    | trees   |        RF |
|---:|:--------|----------:|
|  0 | 8, 1    | 0.277778  |
|  1 | 1, 3    | 0.0555556 |
|  2 | 3, 2    | 0.0555556 |
|  3 | 2, 4    | 0.277778  |
|  4 | 4, 5    | 0.277778  |
|  5 | 5, 9    | 0         |
|  6 | 9, 7    | 0.166667  |
|  7 | 7, 6    | 0.111111  |
|  8 | 6, 0    | 0.333333  |


### 3) INTREPETING DATA: Summary statistics and histogram
Interpret data with summary statistics (mean, std, max, min) and histogram to show distribution of results and sensitivity of the two metric methods. Further data interpretation and plotting can be done with toyplot. 
```python
# summarize data
df = rfs.output
stats = distmetric.SumStat(df, "RF")
stats.get_sumstat()
```
![SumStats](https://github.com/smau8/distmetric/blob/main/demos/demo-working-example2.png)

```python
stats.histogram()
```
![histogram](https://github.com/smau8/distmetric/blob/main/demos/demo-working-example3.png)
