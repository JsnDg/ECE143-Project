#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:20:02 2018

@author: jasonding
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import csv
from sklearn.preprocessing import StandardScaler
from itertools import combinations
from IPython.core.pylabtools import figsize

fire = pd.read_csv('forestfires.csv')

for i in range(517):
    '''
    Initalize the value of area: when area is larger the zero, set it to one;
    '''
    if fire.loc[i, 'rain']>0.15:
        fire.loc[i, 'rain']=0
    if fire.loc[i, 'area']>0:
        fire.loc[i, 'area']=1
    else:
        fire.loc[i, 'area']=0

plt.rcParams['figure.dpi'] = 80

def doplot(x,y):
    '''
    This function is for 2D scatter ploting
    Its two inputs should be strings of the column names of the dataset
    '''
    ax = plt.subplot(111)
    colors = ['g', 'r']
    Label_Com = ['No fire','Fire']
    for index in range(2):
        x_axis = fire.loc[fire['area'] == index][x]
        y_axis = fire.loc[fire['area'] == index][y]
        plot.scatter(x_axis, y_axis, c=colors[index], cmap='brg', alpha=1, marker='.', linewidth=0)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.show()

def triplot(x,y,z):
    '''
    This function is for 3D scatter ploting
    Its three inputs should be strings of the column names of the dataset
    '''
    ax = plt.subplot(111, projection='3d')
    colors = ['g', 'r']
    Label_Com = ['No fire','Fire']
    for index in range(3):
        x_axis = fire.loc[fire['area'] == index][x]
        y_axis = fire.loc[fire['area'] == index][y]
        z_axis = fire.loc[fire['area'] == index][z]
        ax.set_xlabel(x, fontsize=13)
        ax.set_ylabel(y, fontsize=13)
        ax.set_zlabel(z, fontsize=13)
        ax.scatter(x_axis, y_axis, z_axis, c=colors[index], cmap='brg', alpha=1, marker='.', linewidth=0)
        ax.set_title('3D plot of natural features: temp, wind, RH', fontsize=16)
    plt.show()


doplot('rain','RH')
doplot('temp','RH')
doplot('RH','wind')
doplot('wind','temp')

doplot('rain','DMC')
doplot('RH','DMC')
doplot('temp','DMC')

triplot('temp','rain','DMC')
triplot('RH','temp','DMC')
triplot('RH','rain','DMC')

doplot('rain','DC')
doplot('temp','DC')

triplot('temp','rain','DC')
triplot('rain','temp','DC')

triplot('temp','wind','FFMC')
triplot('temp','RH','FFMC')
triplot('wind','RH','FFMC')

triplot('RH','wind','temp')

