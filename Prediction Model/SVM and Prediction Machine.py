#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:37:31 2018

@author: jasonding
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.preprocessing import StandardScaler

from sklearn import svm

fire=np.genfromtxt('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv', delimiter=',', skip_header=True)

data = fire.tolist()
    
def cal_accuracy(predict, y_test):
    '''
    Calculate the accuracy of prediction with test data
    predict: result of prediction
    '''
    count=0
    pool=len(predict)
    for i in range(pool):
        if predict[i]==y_test[i]:
            count=count+1
    accuracy=count/pool
    return accuracy

def Do_SVM(split, SVM_C, train, test_sample):
   '''
   Use SVC to classify
   split: the number of training data, the number of test data will be 517-split
   SVM: C value for SVM
   train: the type of data for training: natural-1 or model-0
   '''
   X_train=[]
   y_train=[]
   X_test=[]
   y_test=[]

   for i in range(1, split):
      if train==0:
          X_train.append(data[i][4:8])
      if train==1:
          X_train.append(data[i][8:12])
      y_train.append(data[i][12])

   for i in range(split-1):
      y_train[i]=float(y_train[i])
      if y_train[i]>0:
          y_train[i]=1
      else:
          y_train[i]=0

   if test_sample > 0:
       for i in range(test_sample, 517):#split
            if train==0:
                X_test.append(data[i][4:8])
            if train==1:
                X_test.append(data[i][8:12])
            y_test.append(data[i][12])
    
       for i in range(517-test_sample):#split
            y_test[i]=float(y_test[i])
            if y_test[i]>0:
                y_test[i]=1
            else:
                y_test[i]=0
   else:
       for i in range(split, 517):#split
            if train==0:
                X_test.append(data[i][4:8])
            if train==1:
                X_test.append(data[i][8:12])
            y_test.append(data[i][12])
    
       for i in range(517-split):#split
            y_test[i]=float(y_test[i])
            if y_test[i]>0:
                y_test[i]=1
            else:
                y_test[i]=0
        
   '''
   Three kinds of SVM methods
   '''    
   clf_linear=svm.SVC(SVM_C,kernel='linear').fit(X_train,y_train)
   clf_rbf=svm.SVC(SVM_C, kernel='rbf').fit(X_train,y_train)
   clf_sigmoid=svm.SVC(SVM_C, kernel='sigmoid').fit(X_train,y_train)

   predict_linear = clf_linear.predict(X_test)
   predict_rbf = clf_rbf.predict(X_test)
   predict_sigmoid= clf_sigmoid.predict(X_test)

   a = cal_accuracy(predict_linear, y_test)
   b = cal_accuracy(predict_rbf, y_test)
   c = cal_accuracy(predict_sigmoid, y_test)
   return a, b, c

def draw_SVM_trend(a,b,SVM_C,Type,test_sample):
    '''
    a is the lower bounder of training samples
    a: int; 0=<a<b
    b is the upper bounder of training samples
    b: int; a<b<517
    SVM_C is the C value for SVM
    SVM_C: int
    Type is for applying natural features-1 or model features-0 
    Type: int; C=0 or 1
    test_sample is to control the number of test samples to be the same
    test_sample: int; test_sample >=0
    '''
    assert isinstance(a, int)
    assert a>=0
    assert isinstance(b, int)
    assert b>=a
    assert b<517
    assert isinstance(SVM_C, int)
    assert isinstance(Type, int)
    assert Type==0 or Type==1
    assert isinstance(test_sample, int)
    assert test_sample>=0
    
    if test_sample==0:
        print('After training, use the rest as test data')
    else:
        print('test samples are from %d to 517'%(test_sample))
    for i in range(a,b):
        a, b, c= Do_SVM(i, SVM_C, Type, test_sample)
        plt.scatter(i, a, c='g')
        plt.scatter(i, b, c='r') 
        plt.scatter(i, c, c='y')
        plt.legend('LRS') 

    plt.xlabel('Sample number')
    if Type==0:
        print('This SVM applied features in the model: FFMC, DMC, DC and ISI')
        plt.ylabel('Accuracy of model features')
    else:
        print('This SVM applied natural features: temp, RH, wind and rain')
        plt.ylabel('Accuracy of natrual features')
    plt.title('Accuracy related to the number of training data and SVM method', va='bottom')
    plt.show()

def Give_prediction(temp_value, RH_value):
    '''
    The most suitable SVM method sigmoid kernel is used
    All the data is used as training data
    From our test, C value for SVM training is selected to be 1
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
    for i in range(517):
        X_train.append(data[i][8:10])
        y_train.append(data[i][12])
    
    for i in range(517):
      y_train[i]=float(y_train[i])
      if y_train[i]>0:
          y_train[i]=1
      else:
          y_train[i]=0
          
    clf_sigmoid=svm.SVC(1, kernel='sigmoid').fit(X_train,y_train)
    predict_rbf = clf_sigmoid.predict([[temp_value, RH_value]])
    if predict_rbf == 1:
        print('Forest fire alarm!')
    if predict_rbf == 0:
        print('Low probability of forest fire.')
    
'''
Example function: 
This function will draw the trend of accuracy
The number of training data from 300 to 480
The C value for SVM is selected to be 1
Natural features will be used
After training, the rest of data will be used as test data
'''
draw_SVM_trend(300,480,1,1,0)

'''
Example function:
This function will show the prediction when temp=25
and RH=20
'''
Give_prediction(25, 20)