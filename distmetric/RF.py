#!/usr/bin/env python

"""
Calculating phylogenetic tree distances using the Robinson Foulds method, 
based on RF method in toytree & ete3. 
"""

import toytree
import numpy as np
import pandas as pd
import itertools
import os

from .Sample import Sample, Generator


class RF():
    """
    Class object to calculate phylogenetic tree distances with the quartet method
    """
    def __init__(self, trees, sampmethod, consensustree=None):
        # store inputs
        self.trees = toytree.mtree(trees)
        self.treelist = self.trees.treelist
        self.sampmethod = sampmethod

        # store output
        self.getrfout = {}
        self.samporder = []
        self.output = pd.DataFrame(columns = ['trees', 'RF'])
        
        self.consensustree = consensustree
        if self.consensustree == None:
            self.consensustree = self.trees.get_consensus_tree()
    
    
    def get_rf(self):
        """
        Function to get RFs depending on user input (pairwise/random sampling of trees
        vs. compare all trees with consensus tree)
        Returns result in a dictionary, with key as tree # and value as RF value. 
        """
        if self.sampmethod == "pairwise" or self.sampmethod == "random":
            samporder = Sample(len(self.trees), self.sampmethod)
            self.samporder = samporder.sampling()

            for idx in range(len(self.trees)-1):
                ttre1 = self.treelist[(self.samporder[idx])]
                ttre2 = self.treelist[(self.samporder[idx+1])]

                rf = ttre1.treenode.robinson_foulds(ttre2.treenode)[0]
                max_rf = ttre1.treenode.robinson_foulds(ttre2.treenode)[1]
                final_rf = rf/max_rf

                self.getrfout[str(self.samporder[idx]) + ", " + str(self.samporder[idx+1])] = final_rf
        
        else:   #self.sampmethod == "consensus":
            for idx in range(len(self.trees)):
                ttre1 = self.treelist[idx]
                rf = ttre1.treenode.robinson_foulds(self.consensustree.treenode, unrooted_trees=True)[0]
                max_rf = ttre1.treenode.robinson_foulds(self.consensustree.treenode, unrooted_trees=True)[1]
                final_rf = rf/max_rf
                
                self.getrfout[str(idx) + ", consensus"] = final_rf
        
        return self.getrfout 
    
    
    def compare_rf(self):
        """
        Function to compile tree # and associated RFs into a final data frame as output
        """
        for idx in self.getrfout:
            self.output = self.output.append({'trees' : idx, 
                                              'RF' : self.getrfout[idx]},
                                              ignore_index = True)
        return self.output
    
    def run(self):
        """
        Define run function
        """
        self.get_rf()
        self.compare_rf()