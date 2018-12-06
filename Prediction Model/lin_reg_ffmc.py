# -*- coding: utf-8 -*-
'''
Fitting FFMC with respct to the natural features it depends on. As a linear fit predicts the FFMC values based on the natural ones decently,
no other mechanisms were employed.
'''
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, metrics 
from numpy import genfromtxt
#Using the data after removing outliers
my_data = genfromtxt('forestfires_refined.csv', delimiter=',')
#x1,x2,x3,x4 contain the natural features,Y is FFMC.
my_data_new=np.delete(my_data,0,0)
Y=np.column_stack([my_data_new[:,4]])
x1=np.column_stack([my_data_new[:,8]])
x2=np.column_stack([my_data_new[:,11]])
x3=np.column_stack([my_data_new[:,9]])
x4=np.column_stack([my_data_new[:,10]])
X=np.column_stack((x1,x2,x3,x4))

# create linear regression object 
reg = linear_model.LinearRegression() 
  
# train the model using the training sets 
reg.fit(X,Y) 
  
# regression coefficients 
print('Coefficients: \n', reg.coef_) 
