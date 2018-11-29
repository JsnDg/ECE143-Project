# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:13:51 2018

@author: meher
"""

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fire=pd.read_csv('forestfires.csv')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X=fire.X
Y=fire.Y
x=X.iloc[intensity.nonzero()[0]]
y=Y.iloc[intensity.nonzero()[0]]
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 9], [0, 9]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.xlabel("x")
plt.ylabel("y")
#plt.zlabel("frequency of fires")

plt.show()