#!/usr/bin/env python

"""
Outputting summary statistics after calculating phylogenetic tree distances. 
"""

#importing packages
import toytree      #toytree to construct phylogenetic trees
import numpy as np  #numpy to do statistical operations
import pandas as pd #pandas to manipulate dataframe
import itertools    #itertools to iterate efficiently
import os           #to get filepaths
import toyplot      #plotting


class SumStat():
    def __init__(self, df, column_name):
        # store input
        self.df = df                                     #dataframe
        self.column_name = column_name                   #column to be calculated upon and plotted
        self.arr = np.array(self.df[self.column_name])   #store dataframe column as numpy array

        # store output
        self.mean = np.mean(self.arr)
        self.std = np.std(self.arr)
        self.min = np.amin(self.arr)
        self.max = np.amax(self.arr)
        self.mark = ""

    def get_sumstat(self):
        """
        Returns mean, standard deviation, minimum and maximum values for inputted distance metrics
        """
        #returning results
        return "mean: {}".format(self.mean), "std: {}".format(self.std), "min: {}".format(self.min), "max: {}".format(self.max)

    def histogram(self):
        """
        Function that takes dataframe as input and plots histogram of distance metrics with mean and standard deviation
        Will potentially normalize using mathematical method or already normalized RFs/Quartets as input?
        """
        # setting plot parameters
        canvas = toyplot.Canvas(width=600, height=400) 
        # making sure axes are cartesian coordinates and labelling axes
        axes = canvas.cartesian(xlabel= self.column_name, ylabel="Frequency") 
        # show axes ticks
        axes.x.ticks.show = True
        axes.y.ticks.show = True
        # Binning values using np.histogram
        self.mark = axes.bars(np.histogram(self.arr,range=(0,1), bins=20))
        return self.mark