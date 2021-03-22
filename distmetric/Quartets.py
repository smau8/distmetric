#!/usr/bin/env python

"""
Calculating phylogenetic tree distances based on the quartet method. 
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
    def __init__(self, trees, sampmethod, consensustree=None):
        # store inputs
        self.trees = toytree.mtree(trees) 
        # get consensus tree (if given the use user's consenus tree, or else, get consensus tree from trees provided in user input)
        self.consensustree = consensustree
        if self.consensustree == None:
            self.consensustree = self.trees.get_consensus_tree()
        # append consensus tree as last in tree list
        self.trees.treelist.append(self.consensustree)
        
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
        with key as tree #/consensus and value as quartet set.
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
            
            # if last tree, this means this is the quartet set for the consensus tree
            if idx == len(self.trees)-1:
                self.getquartetsout['consensus'] = sorted_set
            # if not, treat quartet set as set for a normal tree that will soon be used for comparisons
            else:
                self.getquartetsout[idx] = sorted_set
        return self.getquartetsout    

        
    def compare_quartets(self):
        """
        Compare two sets of quartets generated from each pair of
        phylogenetic trees based on pairwise or random sampling order.
        Return data frame with tree # and quartet metric. 
        """
        # follow sampling order if user wants to calculate distances in pairwise/random fashion
        if self.sampmethod == "pairwise" or self.sampmethod == "random":
            # generate sampling order depending on pairwise or random user input
            # define max length as self.trees - 1 because last tree in list is consensus tree
            length = len(self.trees)-1
            samporder = Sample(length, self.sampmethod)
            self.samporder = samporder.sampling()
        
            # iterate over each pair of trees depending on sampling order
            for idx in range(len(self.trees)-2):             
                q0 = self.getquartetsout[self.samporder[idx]]
                q1 = self.getquartetsout[self.samporder[idx+1]]
        
                # diffs = q0.symmetric_difference(q1)
                # len(diffs)
            
                self.output = self.output.append({'trees' : str(self.samporder[idx])+ ", " + str(self.samporder[idx+1]), 
                                                  'Quartet_intersection' : len(q0.intersection(q1)) / len(q0)},
                                                 ignore_index = True)
        # compares each tree with consensus
        else:
            consensus = self.getquartetsout['consensus']
            for idx in range(len(self.trees)-1):
                q0 = self.getquartetsout[idx]
                self.output = self.output.append({'trees' : str(idx) + ", consensus", 
                                                  'Quartet_intersection' : len(q0.intersection(consensus)) / len(consensus)},
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