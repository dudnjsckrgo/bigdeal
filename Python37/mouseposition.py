# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:53:17 2019

@author: Administrator
"""
import pyautogui
pyautogui.FAILSAFE = False
print(pyautogui.position())
print(pyautogui.size())
#pyautogui.moveTo(819, 41)
'''
while True:
    try:
        
        address="C:/Users/Administrator/Desktop/ugot/a/[64AUDIO]Tia Fourte/"
        center = pyautogui.locateCenterOnScreen('/Users/Administrator/Desktop/ugot/a/address.jpg', grayscale=True)
        pyautogui.click(center)
        pyautogui.typewrite(address, interval=0.1)
        pyautogui.press('enter')
        center = pyautogui.locateCenterOnScreen('/Users/Administrator/Desktop/ugot/a/filename.jpg', grayscale=True)
        pyautogui.click(center)
        tumb_img="[64AUDIO]Tia Fourte_1.jpg"
        pyautogui.typewrite(tumb_img, interval=0.1)
        center = pyautogui.locateCenterOnScreen('/Users/Administrator/Desktop/ugot/a/open.jpg', grayscale=True)
        pyautogui.click(center)
        break
    except:
        pass
'''