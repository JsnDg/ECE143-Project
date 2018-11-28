'''
@author: Kunmao Li


1. new varaible generated:
  1). ln(area+1): float64
  Based on the characteristics of variable 'area' from the plots, remodel 'area' with logarithm transform
  2). FIRE: str
  Fire indicator: fire/no fire ,indicating whether there's fire

3. 2D Visualization(DC & temp/rain)
  Figure 15: pairplots(diagonal:the kernel density estimation; non-diagonal: scatter plots with linear regression line given)
    also, the data has been classified according to variable 'FIRE' and displayed green when no fire and red when on fire
  Figure 16: pairplots(diagonal: single variable distribution; non-diagonal: kernel density plots of two variables)
  Figure 17-20: more complicated, detailed and advanced plots given: 
    kde plots: demonstrate the density distribution between two variables with color change according to the color palatte set
    scatter plots: spot the data easily 
    axis: also display the distribution line of each variable with different color 
    color bar: relate the color shade/range with data values for identifying the level of density 

4. 3D Visualization(DC & temp,RH,rain)
  Figure 21-23:histograms: x,y-axis: temp,rain; z-axis: DC
  classify the histograms by variable 'FIRE': (red histograms:fire; green histograms:no fire)


'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D


fire = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
fire.month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
fire.day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7})
data=pd.DataFrame(fire,columns=['X','Y','month','day','FFMC','DC','DC','ISI','temp','RH','wind','rain','area'])

'''
According to the plots of 'area', the parameter is pretty distorted towards 0.0
Thus using logrithm transform ln(area+1) to remodel 'area' and generate the new varibale 'ln(area+1)'
'''
fire['ln(area+1)']=np.log(fire['area']+1)

'''
Based on the  forest Fire Weather Index system, DC is influenced by temperature(temp) and rain
To clarify the correlation between DC and the rest variables initially, create the pairplots.
figure 15: 16 pairplots totally
         :4 Diagonal plots: kde plots indicating the probability density of the variable
         :14 Non-Diagonal plots: scatter diagrams with linear regression line generated                      
         p.s.: for better visualization, adding variable'FIRE',which indicates 'fire' or 'no fire'
               and mark the data values with two colors(red for fire;green for no fire)
figrue 16: 16 pairplots totally
         :4 Diagonal plots: single paramter distribution
         :14 Non-Diagonal plots: kdeplots of two variables(the core indicates the highest density)
'''

plt.figure(1)
df1=pd.DataFrame(fire,columns=['DC','temp','rain','ln(area+1)'])
# set [ln(area+1)>0]=1 ; [ln(area+1)=0]=0 
df1['FIRE'] = np.where(df1['ln(area+1)']>0, 'fire', 'no fire')
sns.pairplot(df1,vars=['DC','temp','rain'],kind='reg',hue='FIRE',palette='hls',markers=["o", "x"])

plt.figure(2)
g = sns.PairGrid(df1)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot,cmap="Blues_d",n_levels=40)
plt.show()

'''
2D: 
figure 17: DC-temp & DC-RH & DC-rain 
figure 18-20: DC-temp / RH / rain
p.s.: for the plots related to rain, for better observation, adjustment is needed since scatters were initially distributed around 0.00
'''
plt.figure(3)
sub=121
for i in ['temp','rain']:
  plt.subplot(sub)
  plt.title('DC-'+i, fontsize=14, position=(0.5,1.05))
  pal='Reds'
  sns.kdeplot(df1[i],df1['DC'], # demonstrate the probability distribution of two variables
           cbar = True,    # display color bar
           shade = True,   # display shades
           cmap = pal,  # set the color palatte
           shade_lowest=False,  # not display periphery color/shade
           n_levels = 40   # number of curves, the higher, the smoother
           )# the color change indicates the change of density
  plt.grid(linestyle = '--')
  plt.scatter(df1[i], df1['DC'], s=5, alpha = 0.5, color = 'k', marker='+') #scatter
  if sub==122:
    plt.axis([-6,6.5,0,1000])
  sns.rugplot(df1[i], color='r', axis='x',alpha = 0.5)
  sns.rugplot(df1['DC'], color='blue', axis='y',alpha = 0.5)
  sub += 1
plt.show()

plt.figure(4) # DC-temp
plt.title('DC-temp', fontsize=14, position=(0.5,1.05))
pal=sns.cubehelix_palette(8, gamma=2,as_cmap=True)
sns.kdeplot(df1['temp'],df1['DC'],cbar = True,shade = True,cmap = pal,shade_lowest=False,n_levels = 40)
plt.grid(linestyle = '--')
plt.scatter(df1['temp'], df1['DC'], s=5, alpha = 0.5, color = 'k', marker='+') #scatter
sns.rugplot(df1['temp'], color="orange", axis='x',alpha = 0.5)
sns.rugplot(df1['DC'], color="purple", axis='y',alpha = 0.5)
plt.show()

plt.figure(5) # DC-rain
plt.title('DC-rain', fontsize=14, position=(0.5,1.05))
pal=sns.cubehelix_palette(8, start=.5, rot=-.75,as_cmap=True)
sns.kdeplot(df1['rain'],df1['DC'],cbar = True,shade = True,cmap = pal,shade_lowest=False,n_levels = 40)
plt.grid(linestyle = '--')
plt.scatter(df1['rain'], df1['DC'], s=5, alpha = 0.5, color = 'k', marker='+') #scatter
sns.rugplot(df1['rain'], color="blue", axis='x',alpha = 0.5)
sns.rugplot(df1['DC'], color="green", axis='y',alpha = 0.5)
plt.axis([-6,6.5,0,1000])
plt.show()

'''
3D: DC & temp,rain
  Figure 21-23:histograms: x,y-axis: temp,rain z-axis: DMC
  classify the histograms by variable 'FIRE': (red histograms:fire; green histograms:no fire)
'''
fig1=plt.figure(6)
ax = fig1.add_subplot(111, projection='3d')   

x,y,z = np.array(fire['temp']),np.array(fire['rain']),np.array(fire['DC'])
x = x.flatten('F')   
y = y.flatten('F')

'''
mark the bars with two colors for better observation
red: fire
green: no fire
'''
q=df1['FIRE']
C = []  # the list serving as the color palatte 
for a in q:
    if a == 'fire':
        C.append('red') # mark the bars with red color if there's fire
    else:
        C.append('green') # mark the bars with green color if there's no fire

dx = 0.6 * np.ones_like(x) # set the width of the histograms, the constant can be adjusted based on observation of plots
dy = 0.2 * np.ones_like(y)
dz = abs(z) * z.flatten()
dz = dz.flatten() / abs(z)
z = np.zeros_like(z)

ax.set_title('temp-rain-DC')
ax.set_xlabel('temp')
ax.set_ylabel('rain')
ax.set_zlabel('DC')
plt.axis([0,35,-6,6.5])#set the interval of axises to move the bunch of histograms to the centeral area for better observation

ax.bar3d(x, y, z, dx, dy, dz, color=C, zsort='average')
plt.show()


