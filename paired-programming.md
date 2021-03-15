# Feedback for Scarlet on project so far
--Roí A.K., 3/14 - 3/15 2021

This document describes my feedback about the distmetric package.
It's broken down by:
  - My understanding of the goals
  - My understanding of the data being used
  - My understanding of the code as written so far

Finally, it will contain a summary of my code contributions/ideas to the project. 

## The Goal
The goal for the project is clearly written in the propsal: this package takes phylogenetic trees in newick format, calculates distances between trees using a variety of accepted methods, and outputs all the results in a dataframe so researchers could easily compare distances from different methods.

So far what's unclear is how many different methods will be used - will the package try to collect all the different methods available? Will the package import packages that already estimate distance or rewrite each methods to make the comparisons easier?
Another question is whether the package will output any calculation of the *quality* of each method in the comparison? Or simply give a dataframe with different distances without interpretation?

## The Data
It is extremely clear what the data will be. Users will input newick strings of different trees to calculate distances. The output will be a csv of tree pairings and different distances (each column will be a different method).

## The Code

  - ### Skeleton of code
    The two modules currently in the package, `Quartets.py` and `Sample.py`, contain proper skeleton codes, each with a single class object that has a clear function and a couple of simple functions within each class. 
    
    The individual functions are sparsely commented currently. It would be helpful for new users (especially for someone like me who is still a bit uncomfortable with python) when looking at the code, to get a sense of what each line does and each command. I'm not sure if this is common, but comments between each function would also be helpful to understand how the output of one function gets fed into the next one.    
    
  - ### What code does so far 
    `Sample.py` simply samples from a list of newick strings, either in a pairwise fashion or randomly. It also has a class called 'Generator' that randomly makes newick strings based on number of tips, height, and tree format as input by the user.

    `Quartets.py` currently has one class with two functions, an initializing function, and a function that runs and gives output. 
    
    The first function takes the input of newick string format trees and calculates quartets from them. My limited understanding of this is that it constructs trees (?) based on quartets or 4-taxon unrooted trees. This is where I had a bit of a hard time based on *a* not being my field and *b* wanting more comments in the code.
    
    The second function then calculates quartet distance from the two trees. It takes orders of pairs of trees based on `Sample.py`. After the trees are paired up, it calculates the difference between the quartets in each tree.
    It then appends the names of the trees, the comparison being made, and the 'quartet intersection' or distance estimate. 

  - ### Individual function ideas
    Some individual function ideas include:
    - Summary statistics: calculate mean distance and std of each distance method.
    - Visualization: plotting histogram of each distance method, and labelling mean and std
    - Functions to get difference in distance measurements from different methods 

## Code Contributions/Ideas
I created a class called SumStats which begins a skeleton code for how to calculate summary statistics from the outputted dataframe of phylogenetic distances. The class has a function that outputs the calculated means and standard deviations for the columns of quartet intersections. It then has a function that outputs a nice pretty histogram using `toyplot` of the distances given from the quartet method.

The idea for this skeleton code is that when multiple new methods of phylogenetic distance estimation are added to the package, this module will allow for easy comparison of both summary statistics and histograms of all methods. That will give some sense of consistency across distance estimations. 

The major flaw in my code contribution is that it's very preliminary, and I also don't think I initialized the class well.
Therefore, it's not installable yet.

I also made a demo Jupyter notebook to demonstrate how this code might work.