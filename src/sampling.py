#!/usr/bin/env python

"""
Sampling methods accessible for all phylogenetic methods/metrics.
"""

import toytree
import numpy as np
import pandas as pd


def generate_randomtrees(ntrees, trefilepath):
    """
    Generate a specified number of random trees (defined as ntrees)
    and write these trees as individual tree files to the destination
    designated with trefilepath.
    """
    i=0
    generate_randomtrees_df = pd.DataFrame(columns = ['treetest #', 'newick']) 
    for i in range (0, int(npairs)):
        tree = toytree.rtree.unittree(10, seed=i)
        #print(tree)
        generate_randomtrees_df = generate_randomtrees_df.append({'treetest #' : "tree" + str(i+1), 'newick' : tree.write()},  
                ignore_index = True)
        tree.write(trefilepath + str(i+1) + ".tre", tree_format=0)
        i = i+1
        #print(i)
    return generate_randomtrees_df

def pairwise_sampling(ntrees):
    """
    Generate order/pairings to calculate phylogenetic tree distances 
    between neighboring genealogies.
    """
	pass

def random_sampling(ntrees):
    """
    Generate order/pairings to calculate phylogenetic tree distances 
    between random genealogies.
    """
	pass