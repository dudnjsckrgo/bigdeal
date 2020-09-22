# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:43:55 2019

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
import re

import json
import os
import urllib.request
from time import sleep

class Lotte:
    
    def init(self,item_url):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/lotte.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n=2
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get(item_url)
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=0
        self.q=0
    def positioncrawl(self):
        self.q=0

        # chrom webself.driver 사용하여 브라우저를 가져온다.
       
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
       
        x=self.driver.find_elements_by_xpath('//*[@id="storeListArea1"]/div[1]/div/table/tbody/tr/td[2]/a')
        self.z=[]
        for i in x:
            m=i.text.strip()
            if not -1 == m.find('\n'):
                m=m[:m.find('\n')]    
            
            self.z.append(m)
           
        print(self.z)
        '''
        self.y=[]
        for i in x:
            self.y.append(i.get_attribute('innerHTML').strip())
            print(self.y)
        '''
    def toexcel(self):
        m=0
        while True:
            if m==len(self.z):
                break
            
            self.excel.edit_excel_data(self.i+1,1,self.z[m])
            #self.excel.edit_excel_data(self.i+1,2,self.y[m])
            self.i+=1
            
            m+=1
            
        self.excel.save_excel_data()
    def nextpage(self):
        try:
            x=self.driver.find_element_by_xpath('/html/body/form[2]/fieldset/div/div[2]/div[4]/div[2]/a[{}]'.format(self.n))
            self.n+=1
            if self.n==12:
                self.n=3
            webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        except:
           self.n=2
           self.q=1
       

        
    def newwindow(self):
        
        self.window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(self.window_after) 
    def nextposition(self):
        x=self.driver.find_element_by_xpath('/html/body/form[2]/fieldset/div/div[2]/ul/li[{}]/a/span'.format(self.m))
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        self.m+=1
class LotteMart:
    
    def init(self,item_url):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/lottemart.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n=3
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get(item_url)
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=0
        self.q=2
        self.window_before = self.driver.window_handles[0]
    def positioncrawl(self):
        
        self.driver.switch_to.window(self.window_before)
        # chrom webself.driver 사용하여 브라우저를 가져온다.
       
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
       
       
        self.y=[]
        for self.q in range(2,18):
            x=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[{}]/td[3]'.format(self.q))
            self.y.append(x)
        self.z=[]
        for i in self.y:
            m=i.text.strip()
            #if not -1 == m.find('\n'):
            #    m=m[:m.find('\n')]    
            
            self.z.append(m)
           
        print(self.z)
        '''
        self.y=[]
        for i in x:
            self.y.append(i.get_attribute('innerHTML').strip())
            print(self.y)
        '''
        self.u=[]
        self.u2=[]
        for num in range(2,18):
            print(self.z[num-2].split('/'))
            self.b=self.z[num-2].split('/')
            p = re.compile("[(].+[)]")
            
            for num1 in range(len(self.b)):
                self.u=p.findall(self.b[num1])
                self.u1=self.u[0]
                u1=self.u1[1:-1]
                print(self.u1[1:-1])
                print(type(u1))
                #self.u2.append(u1)
                self.excel.edit_excel_data(self.i+1,1,u1)
                self.i+=1
                print(self.u1[1:-1])
        
        
        self.excel.save_excel_data()  
    def toexcel(self):
        m=0
        while True:
            if m==len(self.u2):
                break
            
            self.excel.edit_excel_data(self.i+1,1,self.u2[m])
            #self.excel.edit_excel_data(self.i+1,2,self.y[m])
            self.i+=1
            
            m+=1
            
        self.excel.save_excel_data()
    def nextpage(self):
        try:
            x=self.driver.find_element_by_xpath('/html/body/div/div/p/a[{}]'.format(self.n))
            self.n+=1
            if self.n==13:
                self.n=3
            webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        except:
           self.n=2
           self.q=1

       
    def newwindow(self):
        
        self.window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(self.window_after) 
    def nextposition(self):
        x=self.driver.find_element_by_xpath('/html/body/form[2]/fieldset/div/div[2]/ul/li[{}]/a/span'.format(self.m))
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        self.m+=1
class Homeplus:
    
    def init(self,item_url):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homeplus.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n=3
        self.m=2
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get(item_url)
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=0
      
        self.window_before = self.driver.window_handles[0]
    def positioncrawl(self):
        
        self.driver.switch_to.window(self.window_before)
        # chrom webself.driver 사용하여 브라우저를 가져온다.
       
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
       
       
        self.y=[]
        for self.q in range(2,19):
            x=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[3]/tbody/tr[{}]/td[3]'.format(self.q))
            self.y.append(x)
        self.z=[]
        for i in self.y:
            m=i.text.strip()
            #if not -1 == m.find('\n'):
            #    m=m[:m.find('\n')]    
            
            self.z.append(m)
           
        print(self.z)
        '''
        self.y=[]
        for i in x:
            self.y.append(i.get_attribute('innerHTML').strip())
            print(self.y)
        '''
        self.u=[]
        
        for num in range(2,19):
            print(self.z[num-2].split('/'))
            self.b=self.z[num-2].split('/')
            p = re.compile("[(].+[)]")
            
            for num1 in range(len(self.b)):
                self.u=p.findall(self.b[num1])
                self.u1=self.u[0]
                u1=self.u1[1:-1]
                print(self.u1[1:-1])
                print(type(u1))
                self.excel.edit_excel_data(self.i+1,1,u1)
                self.i+=1
                print(self.u1[1:-1])
        self.excel.save_excel_data()         
class Emart:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/emart.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.n=3
        self.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
        self.driver.get('https://store.emart.com/branch/list.do')
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
        self.i=405
        self.i1=406
    def positioncrawl(self):
       

        # chrom webself.driver 사용하여 브라우저를 가져온다.
       
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
        #delay= 10
        #WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="cont"]/table/tbody/tr[1]/td[2]/a')))
        x=self.driver.find_element_by_xpath('//*[@id="branchList"]/li[{}]/a'.format(self.i1))
        self.a=x.text.strip()
        print(x.text.strip())
        x.click()
        x=self.driver.find_element_by_xpath('//*[@id="conts"]/div/div[2]/div[2]/div[1]/ul/li[2]/dl/dd[1]')
        self.x=x.text.strip()
        print(self.x)
        self.i1+=1
        '''
        self.z=[]
        for i in x:
            self.z.append(i.get_attribute('innerHTML').strip())
            
        print(self.z)    
        x=self.driver.find_elements_by_xpath('//*[@id="cont"]/table/tbody/tr/td[3]/a')
        self.y=[]
        for i in x:
            self.y.append(i.get_attribute('innerHTML').strip())
        print(self.y)
        '''
    def toexcel(self):

        self.excel.edit_excel_data(self.i+1,1,self.x)
        self.excel.edit_excel_data(self.i+1,2,self.a)    
        self.i+=1
           

            
        self.excel.save_excel_data()
    def nextpage(self):
        try:
            x=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/ul/li/a[{}]'.format(self.n))
        except:
            self.n=3
            x=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/ul/li/a[{}]'.format(self.n))
        self.n+=1
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        self.window_before = self.driver.window_handles[0]
    
if __name__=="__main__":
    item_url='https://ko.wikipedia.org/wiki/%ED%99%88%ED%94%8C%EB%9F%AC%EC%8A%A4'#'https://ko.wikipedia.org/wiki/%EB%A1%AF%EB%8D%B0%EB%A7%88%ED%8A%B8#%EB%A1%AF%EB%8D%B0%EB%A7%88%ED%8A%B8_(%EB%8C%80%ED%98%95%EB%A7%88%ED%8A%B8)'#'http://company.lottemart.com/bc/branch/main.do'#'http://www.lottesuper.co.kr/handler/cc/Store-Start'
    item_url_1="http://www.emarteveryday.co.kr/branch/branchList.jsp"
    
    lotte= Emart()
    lotte.init()
    while True:
        lotte.positioncrawl()
        lotte.toexcel()
        
       # lotte.toexcel()
        #lotte.nextpage()
        #lotte.newwindow()
        #if lotte.q== 1:
        #    lotte.nextposition()
        
        
    
    