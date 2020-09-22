# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:30:25 2019

@author: yyw
"""
import speech_recognition as sr
while True:
    try:
        r= sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
            
        print(r.recognize_google(audio,language='ko-KR'))
        with open("C:/Users/yyw/Desktop/공부/폐기물.txt",'a+',encoding ='utf-8') as f1:
            f1.write(r.recognize_google(audio,language='ko-KR')+'\n')
            
    except:
        pass
    

#'C:/Users/yyw/Documents/GOMRecorder/새로운 녹음 01.mp3'