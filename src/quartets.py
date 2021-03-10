#!/usr/bin/env python

"""
A function calculating phylogenetic tree distances based on the quartet method. 
"""

import toytree
import numpy as np
import pandas as pd
import itertools
import os


class quartets:
    """
    class object to calculate phylogenetic tree distances with the quartet method
    """
    def __init__(self):
        self.output = pd.DataFrame(columns = ['trees', 'Quartet intersection']) 
               
        self.get_quartets()
        self.compare_quartets()
        self.run()
        # to be continued
        
    def get_quartets(self):
    """
    Find all possible quartets for that particular
    phylogenetic tree
    """
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
    
        return sorted_set        

        
    def compare_quartets(self):
    """
    Compare two sets of quartets generated from two
    phylogenetic trees. (to be continued, need to 
    store output in __init__ object)
    """
        i=0
        compare_quartets_df = pd.DataFrame(columns = ['trees', 'Quartet intersection']) 
        for i in range (0, int(nquartets)-1):
            q0 = get_quartets(toytree.tree(str(trefilespath) + "/tree" + str(i+1) + ".tre"))
            q1 = get_quartets(toytree.tree(str(trefilespath) + "/tree" + str(i+2) + ".tre"))
            diffs = q0.symmetric_difference(q1)
            len(diffs)
            compare_quartets_df = compare_quartets_df.append({'trees' : str(i+1)+ ", " + str(i+2), 'Quartet intersection' : len(q0.intersection(q1)) / len(q0)},  
                                ignore_index = True)
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            compare_quartets_df.to_csv(str(trefilespath)+ "compare_quartets" + str(nquartets) + ".csv", index=False)
        return compare_quartets_df


    def run(self, arg):
    """
    Define run function
    """
        self.get_quartets(arg)
        self.compare_quartets(arg)