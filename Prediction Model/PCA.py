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

fire = pd.read_csv('/Users/jasonding/Desktop/ECE143 Project/forestfires.csv')

fire.month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr': 4,'may':5,'jun': 6,'jul': 7,'aug': 8,'sep': 9,'oct': 10,'nov': 11,'dec': 12})
fire.day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu': 4,'fri':5,'sat': 6,'sun': 7})

for i in range(517):
    if fire.loc[i, 'rain']>0.2:
        fire.loc[i, 'rain']=0
    if fire.loc[i, 'area']>0:
        fire.loc[i, 'area']=1
    else:
        fire.loc[i, 'area']=0

ax = plt.subplot(111, projection='3d')
ax.scatter(fire['rain'], fire['temp'], fire['wind']) 
ax.set_xlabel('rain')
ax.set_ylabel('temp')
ax.set_zlabel('DC')
plt.show()


All_factors = ['day', 'month', 'RH', 'temp', 'wind','rain','FFMC', 'DMC', 'DC', 'ISI']

Area_features=['FFMC', 'DMC', 'DC', 'ISI']
x = fire.loc[:, Area_features].values 
y = fire.loc[:,['area']].values
x = StandardScaler().fit_transform(x)
pd.DataFrame(data = x, columns = Area_features).head()
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])
#print(principalDf.head(5))
#print(fire[['area']].head())
finalDf = pd.concat([principalDf, fire[['area']]], axis = 1)
#print(finalDf.head(5))
colors = ['g', 'r']
Label_Com = ['No fire','Fire']
for index in range(2):
    PC1 = finalDf.loc[finalDf['area'] == index]['PC1']
    PC2 = finalDf.loc[finalDf['area'] == index]['PC2']
    plt.scatter(PC1, PC2, c=colors[index], cmap='brg', s=10, alpha=1, marker='8', linewidth=0)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()


