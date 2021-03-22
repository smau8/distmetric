# distmetric
The goal of the project is to create an installable package written in Python that measures distances between 
phylogenetic trees using different methods/metrics. The package will primarily be focused on being used in API (Jupyter Notebook).

### In development

### Package installation
Developers can install the package `distmetric` directly by cloning the GitHub repository. After cloning, it is recommended to install the package locally via pip so that the package can used in "developmeent mode" and any changes made to the code will be reflected immediately when using the package. As demonstrated below, three dependencies/additional python packages–`toytree`, `pandas`, `numpy`–will need to be installed separately prior to using this package.  
```
# install dependencies via conda
conda install toytree pandas numpy -c conda-forge

# installing directly via cloning GitHub repository
git clone https://github.com/smau8/distmetric.git
cd ./distmetric
pip install -e .
```

### Working example
The package currently is able to measure distances between phylogenetic trees using the Quartets and Robinson Foulds method with the `Quartets` and `RobinsonFoulds` class objects. Users can also indicate how they would like to measure these distances and are provided with three options: pairwise (compare between tree 1 vs. 2, tree 2 vs. 3 etc.), random (compare between tree 1 vs. 6, 5 vs. 2) and consensus (compare each tree with the consensus tree). The output is presented using a pandas data frame and users can interpret their data using the `SumStat` class object, which returns the mean, standard deviation and histogram distribution of the distance metrics. 

```python
import distmetric

# generate 10 random trees as input with Generator class object
TREES = distmetric.Generator(10)
randomtrees = TREES.get_randomtrees()
# an example of what the trees look like:
randomtrees[0].draw();
```
![tree](https://github.com/smau8/distmetric/blob/main/demos/demo-working-example1.png)

```python
# calculate quartet distances in a pairwise fashion
quart = distmetric.Quartets(randomtrees, "consensus")
quart.run()
df1 = quart.output
# see below for data frame results
```
|    | trees        |   Quartet_intersection |
|---:|:-------------|-----------------------:|
|  0 | 0, consensus |               0.795238 |
|  1 | 1, consensus |               1        |
|  2 | 2, consensus |               0.72381  |
|  3 | 3, consensus |               0.795238 |
|  4 | 4, consensus |               0.942857 |
|  5 | 5, consensus |               0.795238 |
|  6 | 6, consensus |               0.795238 |
|  7 | 7, consensus |               0.92381  |
|  8 | 8, consensus |               0.852381 |
|  9 | 9, consensus |               0.72381  |

```python
# calculate Robinson Foulds distances in a random fashion
rfs = distmetric.RF(randomtrees, "pairwise")
rfs.run()
rfs.output
# see below for data frame results
```
|    | trees   |       RF |
|---:|:--------|---------:|
|  0 | 0, 1    | 0.222222 |
|  1 | 1, 2    | 0.277778 |
|  2 | 2, 3    | 0.111111 |
|  3 | 3, 4    | 0.277778 |
|  4 | 4, 5    | 0.277778 |
|  5 | 5, 6    | 0.333333 |
|  6 | 6, 7    | 0.222222 |
|  7 | 7, 8    | 0.111111 |
|  8 | 8, 9    | 0.166667 |

```python
rfs3 = distmetric.RF(randomtrees, "random")
rfs3.run()
df3 = rfs3.output
```
|    | trees   |        RF |
|---:|:--------|----------:|
|  0 | 4, 3    | 0.277778  |
|  1 | 3, 9    | 0.0555556 |
|  2 | 9, 6    | 0.277778  |
|  3 | 6, 7    | 0.222222  |
|  4 | 7, 5    | 0.277778  |
|  5 | 5, 2    | 0.333333  |
|  6 | 2, 0    | 0.333333  |
|  7 | 0, 8    | 0.333333  |
|  8 | 8, 1    | 0.166667  |

```python
# summarize quartets data
stats1 = distmetric.SumStat(df1, "Quartet_intersection")
print(stats1.get_mean())
print(stats1.get_std())
stats1.histogram()
```
![histogram](https://github.com/smau8/distmetric/blob/main/demos/demo-working-example2.png)
