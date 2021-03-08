#!/usr/bin/env python

"""
A function calculating phylogenetic tree distances based on the quartet method. 
"""

import toytree
import numpy as np
import pandas as pd

class quartets:
	def __init__(self):
		pass

	def get_quartets(self):
		"""
        Find all possible quartets for that particular
        phylogenetic tree
        """
		pass

	def compare_quartets(self):
		"""
        Compare two sets of quartets generated from two
        phylogenetic trees.
        """
		pass

	def run(self, arg):
        """
        Put it all together into a single function call that returns 
        a dataframe with your results
        """
        self.get_quartets(arg)
        self.compare_quartets(arg)