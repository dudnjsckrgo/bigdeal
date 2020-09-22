# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:38:36 2019

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


class Distance:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homepluscenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.excel2=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/emartcenter.xlsx'
        self.excel2.get_execel(path)
        self.excel2.get_sheet('Sheet1')
        self.n =1
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get('https://map.naver.com/')
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=0
        self.q=0
        self.y2=5
        self.y3=0
    def data(self):
        
        self.excel.get_E_excel_data(self.n)
        self.excel.get_D_excel_data(self.n)
        self.excel2.get_E_excel_data(self.y2)
        self.excel2.get_A_excel_data(self.y2)
    def getdistance(self):
        self.driver.get('https://map.naver.com/')
        try:
            x=self.driver.find_element_by_xpath('//*[@id="intro_popup_close"]/span')
        
            webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        except:
            pass
        
        self.excel2.get_E_excel_data(self.y2)
        self.excel2.get_A_excel_data(self.y2)
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[3]/a')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[3]/a')    
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')
        
        c=self.excel2.str_a
        
        
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c, Keys.ENTER).perform()
        
        
        
        
        
        c=self.excel.str_e   
        self.excel.get_E_excel_data(self.n)
        self.excel.get_D_excel_data(self.n)  
        print(self.excel.str_e)
        
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c, Keys.ENTER).perform()
   
        
        x=distance.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[2]/button[3]')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 5
    
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[2]/div/directions-summary-list/div[2]/directions-summary-item-car[1]/div[1]/span[2]')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[2]/div/directions-summary-list/div[2]/directions-summary-item-car[1]/div[1]/span[2]')
        
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,9,x.text.strip())
        self.n += 1
        self.i+=1
        self.excel.save_excel_data()
    def getdistance1(self):
        self.driver.get('https://map.naver.com/')
        try:
            x=self.driver.find_element_by_xpath('//*[@id="intro_popup_close"]/span')
        
            webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        except:
            pass
        
        self.excel2.get_E_excel_data(self.y2)
        self.excel2.get_A_excel_data(self.y2)
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[3]/a')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[1]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[3]/a')    
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/ul/li[2]/a')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')
        
        c='우림테이프 동부지사'
        
        
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c, Keys.ENTER).perform()
        
        
        
        
        self.excel.get_A_excel_data(self.n)
        c=self.excel.str_a   
        self.excel.get_A_excel_data(self.n)
        self.excel.get_D_excel_data(self.n)  
        print(self.excel.str_a)
        
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c, Keys.ENTER).perform()
   
        
        x=distance.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[1]/directions-search/div[2]/button[3]')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        delay= 5
    
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[2]/div/directions-summary-list/div[2]/directions-summary-item-car[1]/div[1]/span[2]')))
        x=self.driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/directions-layout/directions-result/div[2]/div/directions-summary-list/div[2]/directions-summary-item-car[1]/div[1]/span[2]')
        
        print(x.text.strip())
        self.excel.edit_excel_data(self.i+1,9,x.text.strip())
        self.n += 1
        self.i+=1
        self.excel.save_excel_data()
class Center:
    def init(self):
        
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homepluscenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n =1
        self.i=0
    def search1(self):
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get('https://map.naver.com/')
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        x=self.driver.find_element_by_xpath('//*[@id="search-input"]')
        c='홈플러스 물류센터'
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(c, Keys.ENTER).perform()
    def search2(self):
        self.i1=1
        while True:
            try:
                delay= 5
                WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[2]/div[2]/ul/li[{}]/div[1]/dl/dd[1]'.format(self.i1))))
                x=self.driver.find_element_by_xpath('//*[@id="panel"]/div[2]/div[1]/div[2]/div[2]/ul/li[{}]/div[1]/dl/dd[1]'.format(self.i1))
                print(x.text.strip())
                self.i1+=1
                self.excel.edit_excel_data(self.i+1,1,x.text.strip())
                self.i+=1
                self.excel.save_excel_data()
            except:
                 break
            
    def nextpage(self):
        try:
            x=self.driver.find_element_by_xpath('//*[@id="panel"]/div[2]/div[1]/div[2]/div[2]/div/div/a[{}]'.format(self.n))
        except:
            self.n=2
            x=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/ul/li/a[{}]'.format(self.n))
        self.n+=1
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        
if __name__=="__main__":
    
    distance=Distance()
    distance.init()
    while True:
        '''
        distance.data()
        if distance.excel.str_d==None:
                distance.y2+=1
                distance.n=2
                distance.i=1
        if not distance.excel2.str_e==distance.excel.str_d:
                distance.i +=1
                distance.n +=1
                continue
        distance.getdistance()
        '''
        try:
            distance.data()
            '''
            if distance.excel.str_d==None:
                distance.y2+=1
                distance.n=2
                distance.i=1
            if not distance.excel2.str_e==distance.excel.str_d:
                distance.i +=1
                distance.n +=1
                continue
           '''     
            distance.getdistance1()

                
        except:
            distance.n+=1
            distance.i+=1
            continue
       