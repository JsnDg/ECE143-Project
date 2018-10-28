#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:38:23 2018

@author: jasonding
"""

import datetime
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

import sys, csv , operator

fire = pd.read_csv('/Users/jasonding/Desktop/ECE143 Project/forestfires.csv')

fire.month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr': 4,'may':5,'jun': 6,'jul': 7,'aug': 8,'sep': 9,'oct': 10,'nov': 11,'dec': 12})
fire.day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu': 4,'fri':5,'sat': 6,'sun': 7})

'''X&area'''
plt.scatter(fire['day'], fire['area'])
plt.xlabel('day')
plt.ylabel('area')
plt.show()

'''obvious'''
plt.scatter(fire['FFMC'], fire['area'])
plt.xlabel('FFMC')
plt.ylabel('area')
plt.show()

plt.scatter(fire['DMC'], fire['area'])
plt.xlabel('DMC')
plt.ylabel('area')
plt.show()

'''obvious'''
plt.scatter(fire['DC'], fire['area'])
plt.xlabel('DC')
plt.ylabel('area')
plt.show()

'''obvious'''
plt.scatter(fire['ISI'], fire['area'])
plt.xlabel('DC')
plt.ylabel('area')
plt.show()

'''obvious'''
plt.scatter(fire['temp'], fire['area'])
plt.xlabel('temp')
plt.ylabel('area')
plt.show()

plt.scatter(fire['RH'], fire['area'])
plt.xlabel('RH')
plt.ylabel('area')
plt.show()

plt.scatter(fire['wind'], fire['area'])
plt.xlabel('wind')
plt.ylabel('area')
plt.show()

plt.scatter(fire['rain'], fire['area'])
plt.xlabel('rain')
plt.ylabel('area')
plt.show()

'''Month&X'''
'''obvious'''
plt.scatter(fire['month'], fire['area'])
plt.xlabel('month')
plt.ylabel('area')
plt.show()

plt.scatter(fire['month'], fire['FFMC'])
plt.xlabel('month')
plt.ylabel('FFMC')
plt.show()

'''obvious'''
plt.scatter(fire['month'], fire['DMC'])
plt.xlabel('month')
plt.ylabel('DMC')
plt.show()

'''obvious'''
plt.scatter(fire['month'], fire['DC'])
plt.xlabel('month')
plt.ylabel('DC')
plt.show()

plt.scatter(fire['month'], fire['ISI'])
plt.xlabel('month')
plt.ylabel('ISI')
plt.show()

'''obvious'''
plt.scatter(fire['month'], fire['temp'])
plt.xlabel('month')
plt.ylabel('temp')
plt.show()

plt.scatter(fire['month'], fire['RH'])
plt.xlabel('month')
plt.ylabel('RH')
plt.show()

plt.scatter(fire['month'], fire['wind'])
plt.xlabel('month')
plt.ylabel('wind')
plt.show()

'''obvious: rainy Augest'''
plt.scatter(fire['month'], fire['wind'])
plt.xlabel('month')
plt.ylabel('wind')
plt.show()

'''X&FFMC'''
'''obvious'''
plt.scatter(fire['rain'], fire['FFMC'])
plt.xlabel('rain')
plt.ylabel('FFMC')
plt.show()

'''obvious'''
plt.scatter(fire['RH'], fire['FFMC'])
plt.xlabel('RH')
plt.ylabel('FFMC')
plt.show()

'''obvious'''
plt.scatter(fire['temp'], fire['FFMC'])
plt.xlabel('temp')
plt.ylabel('FFMC')
plt.show()

plt.scatter(fire['wind'], fire['FFMC'])
plt.xlabel('wind')
plt.ylabel('FFMC')
plt.show()

'''X&DMC'''
plt.scatter(fire['rain'], fire['DMC'])
plt.xlabel('rain')
plt.ylabel('DMC')
plt.show()

'''obvious'''
plt.scatter(fire['RH'], fire['DMC'])
plt.xlabel('RH')
plt.ylabel('DMC')
plt.show()

'''obvious'''
plt.scatter(fire['temp'], fire['DMC'])
plt.xlabel('temp')
plt.ylabel('DMC')
plt.show()

'''X&DC'''
plt.scatter(fire['rain'], fire['DC'])
plt.xlabel('rain')
plt.ylabel('DC')
plt.show()

'''obvious'''
plt.scatter(fire['temp'], fire['DC'])
plt.xlabel('temp')
plt.ylabel('DC')
plt.show()

'''X&ISI'''
'''obvious'''
plt.scatter(fire['FFMC'], fire['ISI'])
plt.xlabel('FFMC')
plt.ylabel('ISI')
plt.show()

plt.scatter(fire['wind'], fire['ISI'])
plt.xlabel('wind')
plt.ylabel('ISI')
plt.show()



