#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:03:07 2017

@author: Sayali Sonawane
"""
# Import packages
import numpy as np
import plotly
from plotly.graph_objs import Layout,Histogram

# Generate data randomly
x = np.random.randn(500)

# Define trace
# Horizontal chart: set value for y-axis
trace =Histogram(y=x,showlegend=True,marker = dict(color = 'rgb(0, 128, 0)',))

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
# Font family can be used in a layout to define font type, font size and font color for title           
plotly.offline.plot({
                         "data": [
                                  trace
                                  ], 
                        "layout": Layout(title="Horizontal Histogram",font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
                                  },filename='Horizontal_Histogram.html',image='jpeg')
