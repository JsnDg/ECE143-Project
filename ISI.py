'''
Jianing Zhang 11/12/2018
Analysis of ISI with respect to FFMC and Wind. Factors affecting FFMC are also included to see if there is any correlation
'''
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from numpy import genfromtxt

fire_data=genfromtxt('forestfires.csv',delimiter=',')

FFMC=fire_data[1:517,4]
area=fire_data[1:517,12]
wind=fire_data[1:517,10]
ISI=fire_data[1:517,7]

rain=fire_data[1:517,11]
rh=fire_data[1:517,8]
temp=fire_data[1:517,9]
fire=[]
fire_final=[]
print(fire_data.shape)

for i in range(0,516):
    if ISI[i]>50:
        print('Outlier in line:', i+2)
        fire_final=np.delete(fire_data,i,0)
    if area[i]>0:
        fire.append('r')
    else:
        fire.append('g')
print(fire_final.shape)

plt.scatter(ISI,FFMC,color=fire)
plt.xlabel('FFMC')
plt.ylabel('ISI')
plt.show()

plt.scatter(ISI,wind,color=fire)
plt.xlabel('Wind')
plt.ylabel('ISI')
plt.show()

plt.scatter(ISI,rain,color=fire)
plt.xlabel('Rain')
plt.ylabel('ISI')
plt.show()

plt.scatter(ISI,rh,color=fire)
plt.xlabel('Relative Humidity')
plt.ylabel('ISI')
plt.show()

plt.scatter(ISI,temp,color=fire)
plt.xlabel('Temperature')
plt.ylabel('ISI')
plt.show()

ISI_X=np.column_stack(([fire[:,4]],[fire[:,10]]))
ISI_Y=np.column_stack([fire[:,7]])
reg = linear_model.LinearRegression()
reg.fit(ISI_X,ISI_Y)
ISI_Y_pred = reg.predict(ISI_X)
plt.scatter(ISI_X, ISI_Y,color='black')
plt.plot(ISI_X, ISI_Y_pred, color='blue', linewidth=3)
