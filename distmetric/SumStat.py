#!/usr/bin/env python

"""
A function calculating to output mean standard deviations and histograms of phylogenetic tree distances. 
"""

#importing packages

import toytree #toytree to construct phylogenetic trees
import numpy as np #numpy to do statistical operations
import pandas as pd #pandas to manipulate dataframe
import itertools #itertools to iterate efficiently
import os #to get filepaths
import matplotlib.pyplot as plt #for plotting
import toyplot #plotting

#importing modules from this package
from .Sample import Sample, Generator
from .Quartets import Quartets

#class to get mean, std, and output a histogram

class SumStats():

    #Intializing self function
    def __init__(self,df,column_name):
        # store input
        self.df = df #dataframe
        self.column_name = column_name #column to be calculated upon and plotted 

    #getting mean and standard deviation
    def SumStat(self):
        """
        Function that takes an input of a dataframe and returns the mean and standard deviation for distance metrics
        """
        #saving mean
        mean = round(self.df.mean()[0],4)
        #saving standard deviation
        sd = round(self.df.std()[0],4)

        #returning results
        print('mean quartet distance:',mean,' standard deviation:',sd)
        return mean, sd
    
    #outputting histogram and writing the mean and standard deviation
    def SumHist(self):
        """
        Function that takes dataframe as input and plots histogram of distance metrics with mean and standard deviation
        """
        #setting plot parameters
        canvas = toyplot.Canvas(width=600, height=400) 
        #making sure axes are cartesian coordinates and labelling axes
        axes = canvas.cartesian(label="Quartet distance histogram",
                            xlabel="Quartet Distance",
                            ylabel="Frequency") 
        #show axes ticks
        axes.x.ticks.show = True
        axes.y.ticks.show = True
        #Binning values into 10 bins using np.histogram, and coloring them orange
        bars = axes.bars(
            np.histogram(self.df.column_name, bins=10),
            style={"fill":"orange"}
                        )



