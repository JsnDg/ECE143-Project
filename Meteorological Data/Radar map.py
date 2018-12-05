#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:58:29 2018

@author: jasonding
"""

import numpy as np
import matplotlib.pyplot as plt

labels = np.array(['temp','RH','wind','rain'])

dataLenth = 4

data = np.array([5,4,2,1])

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) 
angles = np.concatenate((angles, [angles[0]])) 
 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title('Influential map of natural features', va='bottom', fontproperties="SimHei")
ax.fill(angles, data, facecolor='r', alpha=0.25)
ax.grid(True)
plt.show()
