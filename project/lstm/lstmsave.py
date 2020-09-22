# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:45:57 2019

@author: yyw
"""
 
# 0. 사용할 패키지 불러오기
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
import seaborn as sns
import tensorflow as tf

from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from numpy import argmax
from tensorflow.keras.models import load_model
# 1. 실무에 사용할 데이터 준비하기
# load the dataset
def create_dataset(dataset, look_back=1):
 dataX, dataY = [], [] 

 for i in range(len(dataset)-look_back-1):
  
  a = dataset[i:(i+look_back), 0]
  dataX.append(a)
  dataY.append(dataset[i + look_back, 0])
  
 return numpy.array(dataX), numpy.array(dataY)
dataframe = read_csv('C:/Users/yyw/Downloads/training.csv', usecols=[1], engine='python')
dataframe1 = read_csv('C:/Users/yyw/Downloads/training.csv', usecols=[0], engine='python')
#dataframe=dataframe.set_index('year')

print("dataframe1:",dataframe1)

dataset3 = dataframe1.values
print("dataset3::",dataset3)
dataset = dataframe.values
dataset = dataset.astype('float32')
print("dataset:",dataset)
# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

print("dataset2:",dataset)
# split into train and test sets
train_size = int(len(dataset))
print("train_size:",train_size)
test_size = len(dataset)
print("test_size:",test_size)
train = dataset[:,:]
test = dataset[:,:]
# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))

testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
# 2. 모델 불러오기

model = load_model('lmst_model1.h5')
testPredict= model.predict(testX )
# 3. 모델 사용하기
print("testPredict:",scaler.inverse_transform(testPredict))
for i in range(18):    
    testPredict= numpy.reshape(testPredict, (testPredict.shape[0], 1, testPredict.shape[1]))
    testPredict= model.predict(testPredict )
    print("testPredict:",scaler.inverse_transform(testPredict))
    

testPredict = scaler.inverse_transform(testPredict)

plt.plot(testPredict)
plt.show()