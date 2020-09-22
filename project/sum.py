# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:18:21 2019

@author: yyw
"""
from selenium import webdriver
from time import sleep
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from openpyxl import load_workbook
import pyperclip
from excel import Excel


class SUM:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/lottesuper.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.total=0.0
        self.i=1
    def Sum(self):
        
        self.excel.get_F_excel_data(self.i)
        self.total+= float(self.excel.str_f)
        self.i+=1
    def result(self):
        print(sum)
if __name__=="__main__":
    total= SUM()
    total.init()
    for SUM.i in range(372):
        total.Sum()
        total.result()        