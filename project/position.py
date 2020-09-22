# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:50:29 2019

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


import json
import os
import urllib.request
from time import sleep


class Position:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/resultlotte.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n =2
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
       
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=1
        self.q=0
    def getposition(self):
        self.driver.get('https://www.google.co.kr/maps/@45.2000678,17.2800773,5z?hl=ko')
        self.excel.get_B_excel_data(self.n)   
        self.excel.get_C_excel_data(self.n)
        self.n += 1
        
        c=self.excel.str_b
        c1=self.excel.str_c
        c= str(c)+' '+str(c1)
        print(c)
        delay= 4
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        x=self.driver.find_element_by_xpath('//*[@id="searchboxinput"]')
        sleep(2)
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c,Keys.ENTER).perform()
        delay= 15
        sleep(2)
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')))
        x=self.driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
        x.text.strip()
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,5,x.text.strip())
        self.i+=1
        self.excel.save_excel_data()
    def getposition1(self):
        self.driver.get('https://www.google.co.kr/maps/@45.2000678,17.2800773,5z?hl=ko')
        self.excel.get_G_excel_data(self.n)
        
        self.n += 1
        c=self.excel.str_g
        print(c)
        delay= 4
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        x=self.driver.find_element_by_xpath('//*[@id="searchboxinput"]') 
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c,Keys.ENTER).perform()
        delay= 15
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')))
        x=self.driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
        x.text.strip()
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,1,x.text.strip())
        self.i+=1
        self.excel.save_excel_data()
class Position1:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/lottecenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n =1
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
       
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=0
        self.q=0
    def getdistance(self):
        self.driver.get('https://www.google.co.kr/maps/@45.2000678,17.2800773,5z?hl=ko')
        self.excel.get_A_excel_data(self.n)   
        self.n += 1
        c=self.excel.str_a
        print(c)
        delay= 4
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        x=self.driver.find_element_by_xpath('//*[@id="searchboxinput"]') 
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c,Keys.ENTER).perform()
        n=0
        while n<3:
            sleep(2)
        
            try:
                center = pyautogui.locateCenterOnScreen('/Users/yyw/Desktop/point.jpg', grayscale=True)
                self.center3 = center
                pyautogui.click(center,button='right')
                break
            except:
                pass
            n+=1
        while n<3:
    
            sleep(2)
            try:
                center = pyautogui.locateCenterOnScreen('/Users/yyw/Desktop/here.jpg', grayscale=True)
                self.center3 = center
                pyautogui.click(center)
            except:
                pass
            n+=1
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        
        
        
        x=self.driver.find_element_by_xpath('//*[@id="reveal-card"]/div/div[2]/button[2]')
        
        
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,7,x.text.strip())
        self.i+=1
        self.excel.save_excel_data()
    def getposition(self):
        self.driver.get('https://www.google.co.kr/maps/@45.2000678,17.2800773,5z?hl=ko')
        self.excel.get_G_excel_data(self.n)
        
        self.n += 1
        c=self.excel.str_g
        print(c)
        delay= 4
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        x=self.driver.find_element_by_xpath('//*[@id="searchboxinput"]') 
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c,Keys.ENTER).perform()
        delay= 15
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')))
        x=self.driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
        x.text.strip()
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,1,x.text.strip())
        self.i+=1
        self.excel.save_excel_data()        
if __name__=="__main__":
    distance=Position()
    distance.init()
    
    
    while True:
        distance.getposition()
        '''
        try:
            distance.getposition()
            
        except:
            
            distance.n+=1
            distance.i+=1
        '''
            
           