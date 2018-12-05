# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:18:33 2018

@author: meher
"""
import pandas as pd
import matplotlib.pyplot as plt
intensity=fire.area
inten=intensity.iloc[intensity.nonzero()[0]]
total=inten.count()
small=inten[inten < 50 ].count() 
large=inten[inten > 50 ].count() 
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'small fires','large fires'
sizes = [small, large]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
