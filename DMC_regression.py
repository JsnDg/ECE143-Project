'''
@Kunmao Li

using linear regression(least square method)
evaluate the model by MSE and RMSE

'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

fire = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
fire.month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
fire.day=fire.day.map({'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7})
fire['ln(area+1)']=np.log(fire['area']+1)
df1=pd.DataFrame(fire,columns=['DMC','temp','RH','rain','ln(area+1)'])

X=df1[['temp','RH','rain']]
Y=df1['DMC']
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)
print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

linreg = LinearRegression()
linreg.fit(X_train, y_train)
print (linreg.intercept_)
print (linreg.coef_)
df1['lin_DMC']=linreg.intercept_
var=['temp','RH','rain']
for i in range(3):
	df1['lin_DMC'] += linreg.coef_[i]*df1[var[i]]
print(df1['lin_DMC'])
y_pred = linreg.predict(X_test)

print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

predicted = cross_val_predict(linreg, X, Y, cv=10)

fig, ax = plt.subplots()
ax.scatter(Y, predicted)
ax.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()