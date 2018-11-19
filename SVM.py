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

csv_file=open('/Users/jasonding/Desktop/ECE143 Project/forestfires.csv')
fire_lines = csv.reader(csv_file)

data = []

for one_line in fire_lines:
    data.append(one_line)
    
def cal_accuracy(predict, split, y_test):
    '''
    Calculate the accuracy of prediction with test data
    '''
    count=0
    for i in range(517-split):
        if predict[i]==y_test[i]:
            count=count+1
    accuracy=count/(517-split)
    return accuracy

def Do_SVM(split, SVM_C, train):
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
    
   for i in range(split, 517):
      if train==0:
          X_test.append(data[i][4:8])
      if train==1:
          X_test.append(data[i][8:12])
      y_test.append(data[i][12])

   for i in range(split-1):
      y_train[i]=float(y_train[i])
      if y_train[i]>0:
          y_train[i]=1
      else:
          y_train[i]=0
        
   for i in range(517-split):
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
   '''
   print('linear', cal_accuracy(predict_linear, split, y_test))
   print('rbf', cal_accuracy(predict_rbf, split, y_test))
   print('sigmoid', cal_accuracy(predict_sigmoid, split, y_test))
   '''
   a = cal_accuracy(predict_linear, split, y_test)
   b = cal_accuracy(predict_rbf, split, y_test)
   c = cal_accuracy(predict_sigmoid, split, y_test)
   return a, b, c

def draw_SVM_trend(a,b,SVM_C,Type):
    
    for i in range(a,b):
        a, b, c= Do_SVM(i, SVM_C, Type)
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

    plt.show()
