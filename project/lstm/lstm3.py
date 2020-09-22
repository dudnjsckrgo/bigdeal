# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:23:36 2019

@author: yyw
"""
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential
import lstm, time

#1단계: 데이터 불러오기
epochs  = 1
seq_len = 50

print('> Loading data... ')

X_train, y_train, X_test, y_test = lstm.load_data('C:/Users/yyw/Downloads/SP500.csv', seq_len, True)
#데이터 확인
print(X_train)

print('> Data Loaded. Compiling...')
#2단계: 모델 생성
model = lstm.build_model([1, 50, 100, 1])

model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=epochs,
    validation_split=0.05)

predicted = lstm.predict_point_by_point(model, X_test)

#3단계: 모델 학습
model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=1,
    validation_split=0.05)

#4단계: 주가 예측한 것을 그려보자!
predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
lstm.plot_results_multiple(predictions, y_test, 50)
