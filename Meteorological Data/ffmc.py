# -*- coding: utf-8 -*-
import pandas as pd
fire = pd.read_csv('forestfires.csv')
month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7})
df1=pd.DataFrame(fire,columns=['FFMC','temp','rain','RH','wind','area'])

def plots_for_ffmc(month,day,df1):
    '''Different plots for FFMC as it depends on all of the natural
    features
    '''
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import numpy as np
    import scipy.io as sio
    from mpl_toolkits.mplot3d import Axes3D
    assert isinstance(day, pd.core.series.Series)
    assert isinstance(month, pd.core.series.Series)
    plt.figure(1)
    df1['FIRE'] = np.where(df1['area']>0, 'fire', 'no fire')
    sns.pairplot(df1,vars=['FFMC','temp','rain','RH','wind'],kind='reg',hue='FIRE',palette='hls',markers=["o", "x"])

    plt.figure(2)
    g = sns.PairGrid(df1)
    g.map_diag(sns.kdeplot)
    g.map_offdiag(sns.kdeplot,cmap="Blues_d",n_levels=40)
    plt.show()

    q=df1['FIRE']
    C = []  # the list serving as the color palatte 
    for a in q:
        if a == 'fire':
            C.append('red') # mark the bars/scatters with red color if there's fire
        else:
            C.append('green') # mark the bars/scatters with green color if there's no fire

    plt.figure(3)
    sub=121
    for i in ['temp','rain']:
        plt.subplot(sub)
        plt.title('FFMC-'+i, fontsize=14, position=(0.5,1.05))
        pal='Reds'
        sns.kdeplot(df1[i],df1['FFMC'],shade = True,cmap = pal,shade_lowest=False,n_levels = 40)# the color change indicates the change of density
        plt.grid(linestyle = '--')
        plt.scatter(df1[i], df1['FFMC'], s=5, alpha = 0.5, color = C, marker='+') #scatter(green:no fire; red:fire)
        if sub==122:
            plt.axis([-6,6.5,0,1000])
        sns.rugplot(df1[i], color='r', axis='x',alpha = 0.5)
        sns.rugplot(df1['FFMC'], color='blue', axis='y',alpha = 0.5)
        sub += 1
    plt.show()

    plt.figure(4) 
    plt.title('FFMC-temp', fontsize=14, position=(0.5,1.05))
    pal='Blues'
    sns.kdeplot(df1['temp'],df1['FFMC'],cbar = True,shade = True,cmap = pal,shade_lowest=False,n_levels = 40)
    plt.grid(linestyle = '--')
    plt.scatter(df1['temp'], df1['FFMC'], s=5, alpha = 0.5, color = C, marker='+') #scatter(green:no fire; red:fire)
    sns.rugplot(df1['temp'], color="orange", axis='x',alpha = 0.5)
    sns.rugplot(df1['FFMC'], color="purple", axis='y',alpha = 0.5)
    plt.show()

    plt.figure(5) 
    plt.title('FFMC-rain', fontsize=14, position=(0.5,1.05))
    pal='Blues'
    sns.kdeplot(df1['rain'],df1['FFMC'],cbar = True,shade = True,cmap = pal,shade_lowest=False,n_levels = 40)
    plt.grid(linestyle = '--')
    plt.scatter(df1['rain'], df1['FFMC'], s=5, alpha = 0.5, color = C, marker='+') #scatter(green:no fire; red:fire)
    sns.rugplot(df1['rain'], color="blue", axis='x',alpha = 0.5)
    sns.rugplot(df1['FFMC'], color="green", axis='y',alpha = 0.5)
    plt.axis([-6,6.5,0,1000])
    plt.show()

    fig1=plt.figure(6)
    ax = fig1.add_subplot(111, projection='3d')   

    x,y,z = np.array(fire['temp']),np.array(fire['rain']),np.array(fire['FFMC'])
    x = x.flatten('F')   
    y = y.flatten('F')


    dx = 0.6 * np.ones_like(x) # set the width of the histograms, the constant can be adjusted based on observation of plots
    dy = 0.2 * np.ones_like(y)
    dz = abs(z) * z.flatten()
    dz = dz.flatten() / abs(z)
    z = np.zeros_like(z)

    ax.set_title('temp-rain-FFMC')
    ax.set_xlabel('temp')
    ax.set_ylabel('rain')
    ax.set_zlabel('FFMC')
    plt.axis([0,35,-6,6.5])#set the interval of axises to move the bunch of histograms to the centeral area for better observation

    ax.bar3d(x, y, z, dx, dy, dz, color=C, zsort='average') #green bars: no fire; red bars:fire
    plt.show()
plots_for_ffmc(month,day,df1)
