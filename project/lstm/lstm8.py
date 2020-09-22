# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:48:39 2019

@author: yyw
"""

# LSTM for international airline passengers problem with regression framing
import numpy
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
# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
 dataX, dataY = [], []

 for i in range(len(dataset)-look_back):
  
  a = dataset[i:(i+look_back), 0]
  dataX.append(a)
  dataY.append(dataset[i + look_back, 0])
  
 return numpy.array(dataX), numpy.array(dataY)
# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset
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
# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
model.summary()
# 5. 학습과정 살펴보기

#print(hist.history['acc'])
# make predictionsm
trainPredict = model.predict(trainX)
print("trainX:",trainX)
print("trainPredict:",trainPredict)
testPredict = model.predict(testX)
print("testPredict:",testPredict)
#testX=(17,1,1)
testPredict = model.predict(testX)
#for i in range(18):
# model.predict()
#invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])

testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

print("testPredict:",testPredict)
# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))
model.save('lmst_model1.h5')
#model.load_weights('lstm_weights.hdf5')
# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
# shift test predictions for plotting





#plt.plot(trainPredictPlot)
plt.plot(scaler.inverse_transform(dataset))
plt.show()