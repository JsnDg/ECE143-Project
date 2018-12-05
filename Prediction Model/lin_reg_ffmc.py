# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:54:47 2018

@author: meher
"""

import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, metrics 
from numpy import genfromtxt
my_data = genfromtxt('forestfires.csv', delimiter=',')

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
