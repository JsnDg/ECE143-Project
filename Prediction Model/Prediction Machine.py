#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 23:48:18 2018

@author: jasonding
"""

import pandas as pd
import numpy as np
import csv
from sklearn.preprocessing import StandardScaler

from sklearn import svm

csv_file=open('/Users/jasonding/Desktop/ECE143 Project/forestfires.csv')
fire_lines = csv.reader(csv_file)

data = []

for one_line in fire_lines:
    data.append(one_line)
    
def Give_prediction(temp_value, RH_value):
    '''
    Use to predict whether a fire will occur or not according to real time data
    The most suitable SVM method sigmoid kernel is used
    All the data is used as training data
    From our test, C value for SVM training is selected to be 0.1
    Use only two dominant natural features, temp and RH to make prediction
    The temp is between 0 and 35
    The RH is between 0 and 100 
    '''
    assert isinstance(temp_value, int)
    assert temp_value<35 and temp_value>0
    assert isinstance(RH_value, int)
    assert RH_value<100 and RH_value>0
    
    X_train=[]
    y_train=[]
    for i in range(1, 518):
        X_train.append(data[i][8:10])
        y_train.append(data[i][12])
    
    for i in range(517):
      y_train[i]=float(y_train[i])
      if y_train[i]>0:
          y_train[i]=1
      else:
          y_train[i]=0
          
    clf_sigmoid=svm.SVC(0.1, kernel='sigmoid').fit(X_train,y_train)
    predict_rbf = clf_sigmoid.predict([[temp_value, RH_value]])
    if predict_rbf == 1:
        print('Forest fire alarm!')
    if predict_rbf == 0:
        print('Low probability of forest fire.')