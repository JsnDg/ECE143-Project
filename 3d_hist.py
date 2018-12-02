# -*- coding: utf-8 -*-
"""
For plotting the the frequency of fires in different grids of the park
The areas with fire are filtered first and their frequency of recording a fire is plotted as a 3D plot. 
Outliers are not included by default as only data with fires is considered.
area column indicates the spread of the fire. Considered as intensity for all purposes.
"""
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fire=pd.read_csv('forestfires.csv')

intensity=fire.area
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X=fire.X
Y=fire.Y
x=X.iloc[intensity.nonzero()[0]]
y=Y.iloc[intensity.nonzero()[0]]
#chose fewer bins to make it look less crowded.
hist, xedges, yedges = np.histogram2d(x,y,bins=4,range=[[0, 9], [0,9]])
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()
plt.ylim(9,0)
#plt.xlim(9,0)
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("frequency of fires")

plt.show()
