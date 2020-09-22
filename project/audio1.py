# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:08:33 2019

@author: yyw
"""

import speech_recognition as sr

r= sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
    
print(r.recognize_google(audio,language='ko-KR'))
with open("C:/Users/yyw/Desktop/공부/유해가스2.txt",'a+',encoding ='utf-8') as f1:
    f1.write(r.recognize_google(audio,language='ko-KR')+'\n')