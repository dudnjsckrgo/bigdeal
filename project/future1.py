# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:13:26 2019

@author: yyw
"""
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import load_model
pd.options.display.float_format = '{:.2f}'.format
df = read_csv('C:/Users/yyw/Downloads/사업장생활폐기물.csv', usecols=[0,1,2,3,4,5], engine='python')
#df=df.iloc[1:9,:]

print(df)
styear=2010.5
print(df.year-styear)
df['x']=df.year-styear
df['x2']=((df.year-styear)**2)
print(df)
print(sum(df.x2))
xy= pd.DataFrame(index=['year','총계','가연성','불연성','재활용가능자원','음식물류폐기물'])
for x in range(8):
    xy[x]=df.iloc[x,1:6]*df.x[x]
    print(xy.T)
#xy.T.to_excel('/Users/yyw/Desktop/study/일반폐기물처리/predict17.xlsx',sheet_name='Sheet1')

df1 = read_csv('C:/Users/yyw/Desktop/study/일반폐기물처리/predict17.csv', usecols=[1,2,3,4,5,6], engine='python')
a= pd.DataFrame(index=[0])
ea=8
for n in range(1,6):   
    sum(df1.iloc[:,n])
    print(sum(df1.iloc[:,n]))
    a1=ea*sum(df1.iloc[:,n])/(ea*sum(df.x2))
    a[n-1]=a1
    print("a",a)
b= pd.DataFrame(index=[0])    
for n in range(1,6):   
    sum(df.iloc[:,n])
    print(sum(df.iloc[:,n]))
    b1=sum(df.x2)*sum(df.iloc[:,n])/(ea*sum(df.x2))
    b[n-1]=b1
    print("b",b)
future= pd.DataFrame(index=range(5))     
for n in range(5,20):
    y=a*n+b
    y=y.T
    print(y.T)
    future[n-5]=y
    
    
#future.columns = ['one','total','man','woman','dense']
future=future.T
print(future)
future.to_excel('/Users/yyw/Desktop/study/일반폐기물처리/predict18.xlsx',sheet_name='Sheet1')  
  
'''

print((df.total.iloc[len(df.year)-1]-df.total.iloc[0])/(len(df.year)-1))
print((df.iloc[len(df.year)-1]-df.iloc[0])/(len(df.year)-1))
mean=(df.iloc[len(df.year)-1]-df.iloc[0])/(len(df.year)-1)
future= pd.DataFrame(index=['year','one','total','man','woman','dense'])     
for x in range(1,12):
    futuredata=df.iloc[len(df.year)-1]+mean*x
    
    print(futuredata)
    future[x-1]=futuredata
    future.T
    print(future.T)
future.T.to_excel('/Users/yyw/Desktop/study/일반폐기물처리/predict1.xlsx',sheet_name='Sheet1')
'''