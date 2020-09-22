# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:37:42 2019

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
df = read_csv('C:/Users/yyw/Downloads/poplulation.csv', usecols=[0,1,2,3,4,5], engine='python')
print(len(df.year))
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
future.T.to_excel('/Users/yyw/Desktop/study/일반폐기물처리/predict.xlsx',sheet_name='Sheet1')
#dataframe=dataframe.set_index('year')
