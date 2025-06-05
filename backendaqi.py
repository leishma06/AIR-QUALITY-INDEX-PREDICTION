# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 12:00:24 2025

@author: leish
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
data=pd.read_csv(r"C:\Users\leish\python\aqi dataset.csv")
print(data)
print(data.dropna(inplace=True))
print(data.isnull().sum())
print(data.shape)
print(data.columns)
x=data[['SO2', 'CO', 'NO', 'NO2', 'NOX', 'NH3', 'O3','WS', 'WD', 'RH', 'SR', 'TC']]
y=data['AQI']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train.shape)
#LINEAR REGRESSION 
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
print(y_pred)
print(r2_score(y_test,y_pred))
#REGRESSION USING KNN
reg1=KNeighborsRegressor()
reg1.fit(x_train,y_train)
y_pred=reg1.predict(x_test)
print(y_pred)
print(r2_score(y_test,y_pred))
#REGRESSION USING DECISIONTREE
reg2=DecisionTreeRegressor()
reg2.fit(x_train,y_train)
y_pred=reg2.predict(x_test)
print(y_pred)
print(r2_score(y_test,y_pred))
#REGRESSION USING RANDOMFOREST
reg3=RandomForestRegressor(n_estimators=100)
reg3.fit(x_train,y_train)
y_pred=reg3.predict(x_test)
print(y_pred)
print(r2_score(y_test,y_pred))
#IMPORTING RANDOM FOREST PREDICTION TO A PICKLE FILE
import pickle
with open('model.pkl','wb') as file:
    pickle.dump(reg3,file)
    
    