# -*- coding: utf-8 -*-
import pandas as pd
fire=pd.read_csv('forestfires.csv')
intensity=fire.area
rain=fire.rain

def rain_plot(rain):
    '''
    Plots the frequency of observing fires in respective months
    '''
    import matplotlib.pyplot as plt
    assert isinstance(rain, pd.core.series.Series)
    assert rain.all()>=0
    r_1=rain[rain.le(1)].count() 
    r_2=rain[rain.le(4)].count()
    r_3=rain[rain.ge(4)].count()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels ='rain>0','rain=0'
    sizes = [r_2+r_3-r_1,r_1]
    explode = (0.1,0)
    colors = ['blue','orange']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.legend(colors, labels, loc="best")
    plt.show()
    
rain_plot(rain)
