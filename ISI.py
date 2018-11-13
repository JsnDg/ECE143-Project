'''
Jianing Zhang 11/12/2018
Analysis of ISI with respect to FFMC and Wind. Factors affecting FFMC are also included to see if there is any correlation
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
fire_data=genfromtxt('forestfires.csv',delimiter=',')
print(fire_data.shape)

FFMC=fire_data[1:517,4]
area=fire_data[1:517,12]
wind=fire_data[1:517,10]
ISI=fire_data[1:517,7]

rain=fire_data[1:517,11]
rh=fire_data[1:517,8]
temp=fire_data[1:517,9]
fire=[]
fire_final=[]
for i in range(0,516):
    if ISI[i]>50:
        print(i)
        fire_final=np.delete(fire_data,i)
    if area[i]>0:
        fire.append('r')
    else:
        fire.append('g')

plt.scatter(ISI,FFMC,color=fire)
plt.xlabel('ISI')
plt.ylabel('FFMC')
plt.show()



plt.scatter(ISI,wind,color=fire)
plt.xlabel('ISI')
plt.ylabel('Wind')
plt.show()

plt.scatter(ISI,rain,color=fire)
plt.xlabel('ISI')
plt.ylabel('Rain')
plt.show()

plt.scatter(ISI,rh,color=fire)
plt.xlabel('ISI')
plt.ylabel('Relative Humidity')
plt.show()

plt.scatter(ISI,temp,color=fire)
plt.xlabel('ISI')
plt.ylabel('Temperature')
plt.show()

print(type(fire_final))