'''
Jianing Zhang 11/12/2018
Analysis of ISI with respect to FFMC and Wind. Factors affecting FFMC are also included to see if there is any correlation
Linear regression included
'''
#import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from numpy import genfromtxt
#read as numpy array
fire_data=genfromtxt('forestfires.csv',delimiter=',')
#Dissect data into columns, below are primary and direct factors
FFMC=fire_data[1:517,4]
area=fire_data[1:517,12]
wind=fire_data[1:517,10]
ISI=fire_data[1:517,7]
#Dissect secondary data
rain=fire_data[1:517,11]
rh=fire_data[1:517,8]
temp=fire_data[1:517,9]
fire=[]#create array to record fire and non-fire


for i in range(0,516):
    assert area[i]>=0
    assert isinstance(ISI[i],(int,float))#assert to use in graphing later
    if ISI[i]>50:
        print('Outlier in line:', i+2)#Obvious outlier picked through visualization. The data is marked and will be removed to train machine learning model.
    if area[i]>0:
        fire.append('r')#Mark fire as red
    else:
        fire.append('g')#Mark no fire as green

#Plot ISI and FFMC using scatterplot, a direct factor
plt.scatter(ISI,FFMC,color=fire)
plt.xlabel('FFMC')
plt.ylabel('ISI')
plt.show()
#Plot ISI and wind,a direct factor
plt.scatter(ISI,wind,color=fire)
plt.xlabel('Wind')
plt.ylabel('ISI')
plt.show()
#Plot ISI and rain, an indirect factor
plt.scatter(ISI,rain,color=fire)
plt.xlabel('Rain')
plt.ylabel('ISI')
plt.show()
#Plot ISI and relative humidity(RH), an indirect factor
plt.scatter(ISI,rh,color=fire)
plt.xlabel('Relative Humidity')
plt.ylabel('ISI')
plt.show()
#Plot ISI and temperature, an indirect factor
plt.scatter(ISI,temp,color=fire)
plt.xlabel('Temperature')
plt.ylabel('ISI')
plt.show()

#Investigate further into relationship between ISI and direct factors.
#Use linear regression model to see whether we can express ISI in terms of FFMC linearly.
for j in range(1,516):
    assert isinstance(fire_data[i,4], float)
    assert isinstance(fire_data[i,7], float)
    assert isinstance(fire_data[i,10], float)
ISI_x1=np.column_stack([fire_data[1:,4]])#Pick out FFMC column from datasheet
ISI_Y=np.column_stack([fire_data[1:,7]])#Pick out ISI column from datasheet
reg = linear_model.LinearRegression()
reg.fit(ISI_Y,ISI_x1)#Use linear regression model provided by sklearn
ISI_Y_pred = reg.predict(ISI_x1)#Try to predict ISI given FFMC values and the linear equation we just found
plt.scatter(ISI_Y, ISI_x1,color='black')
plt.plot(ISI_x1, ISI_Y_pred, color='blue', linewidth=3)
plt.show()#plot the equation and data
#Linear model has limitations, could be applied only at the clustered areas.

#Use linear regression model to see whether we can express ISI in terms of FFMC linearly.
ISI_x2=np.column_stack([fire_data[1:,10]])#Pick out wind column from datasheet
ISI_Y=np.column_stack([fire_data[1:,7]])#Pick out ISI column from datasheet
reg = linear_model.LinearRegression()
reg.fit(ISI_Y,ISI_x2)#Use linear regression model provided by sklearn
ISI_Y_pred = reg.predict(ISI_x2)#Try to predict ISI given wind values and the linear equation we just found
plt.scatter(ISI_Y, ISI_x2,color='black')
plt.plot(ISI_x2, ISI_Y_pred, color='blue', linewidth=3)
plt.show()#plot the equation and data
#Linear model could not satisfy our demands due to data being too scattered.
