# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:22:01 2018

@author: meher
"""

import pandas as pd
fire=pd.read_csv('forestfires.csv')
month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
intensity=fire.area
month_num=month.iloc[intensity.nonzero()[0]]
month_num.plot.hist(bins=12)
