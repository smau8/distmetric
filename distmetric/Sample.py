#!/usr/bin/env python

"""
Methods to sample and generate random trees accessible 
to all phylogenetic methods/metrics in package.
"""

import toytree
import numpy as np
import pandas as pd


class Sample:
    """
    Sampling methods accessible for all phylogenetic methods/metrics
    """
    def __init__(self, ntrees, method):
        # store input
        self.ntrees = ntrees
        self.method = method

        # store output
        self.pairwisesamplingout = np.zeros((self.ntrees, 1), dtype=int)
        self.randomsamplingout = np.zeros((self.ntrees, 1), dtype=int)

    
    def sampling(self):
        """
        Generate pairwise order/pairings to calculate phylogenetic tree distances 
        (ex. 10 trees provided, compare tree 1 & 2, compare 2 & 3 etc.)
    
        OR Generate random order/pairings to calculate phylogenetic tree distances 
        (ex. 10 trees provided, compare tree 1 & 5, compare 5 & 6 etc.)
        """
        if self.method == "pairwise":
            self.pairwisesamplingout = np.arange(start=0, stop=self.ntrees, step=1)
            return self.pairwisesamplingout

        if self.method == "random":
            self.randomsamplingout = np.random.choice(self.ntrees, size=self.ntrees, replace=False)
            return self.randomsamplingout


class Generator:
    """
    Generate random trees.
    """
    def __init__(self, ntrees, ntips=10, treeheight=1e6, tree_format=0):
        # store input
        self.ntrees = ntrees
        self.ntips = ntips
        self.treeheight = treeheight
        self.tree_format = tree_format
        #self.writefile = writefile

        # store output
        self.treestringout = ""
        self.trees = []
                
    def get_randomtrees(self):
        """
        Generate a specified number of random trees (indicated with ntrees)
        and write these trees into one list. 
        """
        # output
        self.trees = [
            toytree.rtree.unittree(ntips=self.ntips, treeheight=self.treeheight)    
            for i in range(self.ntrees)
        ]
    
        return(self.trees)

