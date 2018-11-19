# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 07:24:23 2018

@author: meher
"""

from numpy import genfromtxt
my_data = genfromtxt('forestfires.csv', delimiter=',')
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

Z_dat=my_data[1:517,12]
X_dat=my_data[1:517,0]
Y_dat=my_data[1:517,1]

X, Y, Z, = np.array([]), np.array([]), np.array([])
for i in range(len(X_dat)):
        X = np.append(X,X_dat[i])
        Y = np.append(Y,Y_dat[i])
        Z = np.append(Z,Z_dat[i])
zmin = 1
zmax = 9
zi[(zi<zmin) | (zi>zmax)] = 0
# create x-y points to be used in heatmap
xi = np.linspace(X.min(),X.max(),1000)
yi = np.linspace(Y.min(),Y.max(),1000)
zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')
CS = plt.contourf(xi, yi, zi, 15, cmap=plt.cm.gist_heat)
plt.colorbar()  
plt.show()

