# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:13:05 2019

@author: yyw
"""
import pyautogui as pag

while True:
    x , y = pag.position()
    print('x: %s, y: %s' % (x,y))
