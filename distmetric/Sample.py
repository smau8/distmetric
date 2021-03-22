#!/usr/bin/env python

"""
Sampling and generating random trees for phylogenetic calcluations downstream
"""

import toytree
import numpy as np
import pandas as pd


class Sample:
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

        Consensus option is for users to calculate distance metrics between each tree
        relative to the consensus tree
        """
        if self.method == "pairwise":
            self.pairwisesamplingout = np.arange(start=0, stop=self.ntrees, step=1)
            return self.pairwisesamplingout

        if self.method == "random":
            self.randomsamplingout = np.random.choice(self.ntrees, size=self.ntrees, replace=False)
            return self.randomsamplingout

        if self.method == "consensus":
            return self.method



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

        # store output
        self.treestringout = ""
        self.trees = []
                
    def get_randomtrees(self):
        """
        Generate a specified number of random trees (indicated with ntrees)
        and write these trees into one list. 
        """
        # output trees
        self.trees = [
            toytree.rtree.unittree(ntips=self.ntips, treeheight=self.treeheight)    
            for i in range(self.ntrees)
        ]
        # save as toytree multitree
        #self.trees = toytree.mtree(self.trees)
    
        return self.trees

