'''
@author: Kunmao Li

Function: create the heat maps demonstrating the fire intensity of burned areas in the Montesinho park

1.  Red color : there is fire(area or ln(area+1)>0) 
	No color: no fire(area or ln(area+1)=0)
	p.s.:area is the variable indicating the burned area of the forest (in ha): 0.00 to 1090.84 
	     ln(area+1) is the logarithm transform of variable area
2.  The color bar next to the heat map indicates the change of intensity of fire in different areas within the park
	The darker/more saturated the red is, the intensity of fire in that area is higher
	The range of the color shade in the heat map is based on the robust quantile rather than the actual value change of variables(area or ln(area+1))
3.	Axises for figure 1&2 are the same:
	X axis:spatial coordinate within the Montesinho park map: 1 to 9(the dataset divides the coordinatepark area into 1-9)
	Y axis:spatial coordinate within the Montesinho park map: 1 to 9(the dataset divides the coordinatepark area into 1-9)
	So the shape of heat map resembels the actual map of Montesinho park
	Differences:
	figure 1: heat map is set based on variable area
	figure 2: heat map is set based on variable ln(area+1)

'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

fire = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
fire.month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
fire.day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7})
fire['ln(area+1)']=np.log(fire['area']+1)

df1=pd.DataFrame(fire,columns=['X','Y','area'])
df2=pd.DataFrame(fire,columns=['X','Y','ln(area+1)'])
df1.head()
df2.head()
pt1 = df1.pivot_table(index='Y', columns='X', values='area', aggfunc=np.sum) #set the table and group the variables
pt2 = df2.pivot_table(index='Y', columns='X', values='ln(area+1)', aggfunc=np.sum)
pt1.head()
pt2.head()

plt.figure(1)
f, ax1 = plt.subplots(figsize = (9, 9))
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))

cmap = 'Reds' # choose the palatte for heat map
sns.heatmap(pt1, cmap = cmap, linewidths = 0.1,ax = ax1,annot=True, annot_kws={'size':9,'weight':'bold'})#annotate: add statistics in the box of heat map
plt.xlabel('X:spatial coordinate within the Montesinho park map: 1 to 9',fontsize=14,position=(0.6,1.05))
plt.ylabel('Y:spatial coordinate within the Montesinho park map: 1 to 9',fontsize=14)
plt.title('fire intensity: burned area of the forest',fontsize=14, position=(0.5,1.05))

plt.figure(2)
f, ax2 = plt.subplots(figsize = (9, 9))
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))

cmap = 'Reds'# choose the palatte for heat map
sns.heatmap(pt2, cmap = cmap, linewidths = 0.1,ax = ax2,annot=True, annot_kws={'size':9,'weight':'bold'})#annotate: add statistics in the box of heat map
plt.xlabel('X:spatial coordinate within the Montesinho park map: 1 to 9',fontsize=14,position=(0.6,1.05))
plt.ylabel('Y:spatial coordinate within the Montesinho park map: 1 to 9',fontsize=14)
plt.title('fire intensity: burned area of the forest with logorithm transform',fontsize=14, position=(0.5,1.05))

plt.show()