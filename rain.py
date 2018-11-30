# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:46:20 2018

@author: meher
"""

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
fire=pd.read_csv('forestfires.csv')
rain=fire.rain
r_1=rain[rain.le(1)].count() 
r_2=rain[rain.le(4)].count()
r_3=rain[rain.ge(4)].count()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels ='rain>0','rain=0'
sizes = [0.004,0.996]
explode = (0.1,0)
colors = ['blue','orange']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        #shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(colors, labels, loc="best")
plt.show()