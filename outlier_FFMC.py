# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import genfromtxt
my_data = genfromtxt('forestfires.csv', delimiter=',')
import numpy as np
print(my_data.shape)
FFMC=my_data[1:517,4]
rain=my_data[1:517,11]
rh=my_data[1:517,8]
temp=my_data[1:517,9]
wind=my_data[1:517,10]
area=my_data[1:517,12]
fire=[]
for i in range(0,516):
    if area[i]==0:
        fire.append('g')
    else:
        fire.append('r')
import matplotlib.pyplot as plt
plt.scatter(FFMC,rain,color=fire)
plt.show()
#outlier:object 379
plt.scatter(FFMC,rh,color=fire)
plt.show()
#outlier:object 379
plt.scatter(FFMC,temp,color=fire)
plt.show()
#outlier:object 379
plt.scatter(FFMC,wind,color=fire)
plt.show()
#outlier:object 379
#removing outlier - item 379:
for i in range(515):
    if FFMC[i]<20:
        print(i)
my_data_new=np.delete(my_data,379,0)