# -*- coding: utf-8 -*-
from numpy import genfromtxt
my_data = genfromtxt('forestfires.csv', delimiter=',')
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

intensity=my_data[1:517,12]
X=my_data[1:517,0]
Y=my_data[1:517,1]

def plot_heat_map(Z_dat,X_dat,Y_dat):
    '''
    For plotting the intensity of fires in different grids identified
    by the x and y co-ordinates of the grid.
    '''
    import numpy as np
    assert isinstance(Z_dat, np.ndarray)
    assert isinstance(Y_dat, np.ndarray)
    assert isinstance(X_dat, np.ndarray)
    assert 0<X_dat.all()<10
    assert 0<Y_dat.all()<10
    assert 0<=Y_dat.all()<1000
    X, Y, Z, = np.array([]), np.array([]), np.array([])
    for i in range(len(X_dat)):
        X = np.append(X,X_dat[i])
        Y = np.append(Y,Y_dat[i])
        Z = np.append(Z,Z_dat[i])
        #Grids are from 1-9 in both the axes.
    zmin = 1
    zmax = 9
    # create x-y points to be used in heatmap
    xi = np.linspace(X.min(),X.max(),1000)
    yi = np.linspace(Y.min(),Y.max(),1000)
    zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')
    CS = plt.contourf(xi, yi, zi, 15, cmap=plt.cm.gist_heat)
    plt.colorbar()  
    plt.show()

plot_heat_map(intensity, X, Y)
