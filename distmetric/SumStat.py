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
        self.df = df #dataframe
        self.column_name = column_name #column to be calculated upon and plotted
        
        # store output
        self.mean = ""
        self.std = "" 
        self.mark = ""

    def get_mean(self):
        """
        Function that takes an input of a dataframe and returns the mean for distance metrics
        """
        #saving mean
        self.mean = self.df[self.column_name].mean()
        #returning result
        return self.mean
    
    def get_std(self):
        """
        Function that takes an input of a dataframe and returns the standard deviation for distance metrics
        """
        #saving standard deviation
        self.std = self.df[self.column_name].std()
        # return result
        return self.std

    def histogram(self):
        """
        Function that takes dataframe as input and plots histogram of distance metrics with mean and standard deviation
        """
        #setting plot parameters
        canvas = toyplot.Canvas(width=600, height=400) 
        #making sure axes are cartesian coordinates and labelling axes
        axes = canvas.cartesian(xlabel= self.column_name,
                            ylabel="Frequency") 
        #show axes ticks
        axes.x.ticks.show = True
        axes.y.ticks.show = True
        #Binning values using np.histogram
        self.mark = axes.bars(np.histogram(self.df[self.column_name], density=True))
        return self.mark