#!/usr/bin/env python

"""
A function calculating phylogenetic tree distances based on the quartet method. 
"""

import toytree
import numpy as np
import pandas as pd
import itertools
import os

from .Sample import Sample, Generator


class Quartets():
    """
    Class object to calculate phylogenetic tree distances with the quartet method
    """
    def __init__(self, trees, sampmethod):
        # store inputs
        self.trees = toytree.mtree(trees)
        self.treelist = self.trees.treelist
        self.sampmethod = sampmethod

        # store output
        self.getquartetsout = {}
        self.samporder = []
        self.output = pd.DataFrame(columns = ['trees', 'Quartet_intersection'])
        
        
    def get_quartets(self):
        """
        Find all possible quartets for each phylogenetic tree
        from user input and store in self.getquartetsout dictionary
        with key as tree # and value as quartet set.
        """       
        # iterate over each tree in input
        for idx in range(len(self.trees)):
            ttre = self.treelist[idx]
            
            # store all quartets in this SET
            qset = set([])
    
            # get a SET with all tips in the tree
            fullset = set(ttre.get_tip_labels())
    
            # get a SET of the descendants from each internal node
            for node in ttre.idx_dict.values():   

                # skip leaf nodes
                if not node.is_leaf():
            
                    children = set(node.get_leaf_names())
                    prod = itertools.product(
                        itertools.combinations(children, 2),
                        itertools.combinations(fullset - children, 2),
                    )
                    quartets = set([tuple(itertools.chain(*i)) for i in prod])
                    qset = qset.union(quartets)

            # order tups in sets
            sorted_set = set()
            for qs in qset:
                if np.argmin(qs) > 1:
                    tup = tuple(sorted(qs[2:]) + sorted(qs[:2]))
                    sorted_set.add(tup)
                else:
                    tup = tuple(sorted(qs[:2]) + sorted(qs[2:]))
                    sorted_set.add(tup)            
            self.getquartetsout[idx] = sorted_set
        return self.getquartetsout    

        
    def compare_quartets(self):
        """
        Compare two sets of quartets generated from each pair of
        phylogenetic trees based on pairwise or random sampling order.
        Return data frame with tree # and quartet metric. 
        """
        # generate sampling order depending on pairwise or random user input
        samporder = Sample(len(self.trees), self.sampmethod)
        self.samporder = samporder.sampling()
        
        # iterate over each pair of trees depending on sampling order
        for idx in range(len(self.trees)-1): 
            
            q0 = self.getquartetsout[self.samporder[idx]]
            q1 = self.getquartetsout[self.samporder[idx+1]]
        
            diffs = q0.symmetric_difference(q1)
            len(diffs)
            
            self.output = self.output.append({'trees' : str(self.samporder[idx])+ ", " + str(self.samporder[idx+1]), 
                                              'Quartet_intersection' : len(q0.intersection(q1)) / len(q0)},
                                             ignore_index = True)
        #pd.set_option("display.max_rows", None, "display.max_columns", None)
        # return data frame as output
        return self.output        
        
        
    def run(self):
        """
        Define run function
        """
        self.get_quartets()
        self.compare_quartets()