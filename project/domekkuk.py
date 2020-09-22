# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:59:21 2019

@author: Administrator
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
#exel_path ='/Users/Administrator/Downloads/온라인판매20190726.xlsx'
import pyperclip, pyautogui 
from excel import Excel
from selenium import webdriver

import json
import os
import urllib.request
from time import sleep

#찾고자 하는 검색어를 url로 만들어 준다.


class Domekkuk:
        
    def imgcrawl(self,searchterm,upper_path,item_name):
        upper_url='domeggook.com/main/item/itemMD.php'
        self.searchterm2 = searchterm +'/'
    
        self.rpath= upper_path + self.searchterm2
        # chrom webself.driver 사용하여 브라우저를 가져온다.
        self.driver = webdriver.Chrome('C:/chromeself.driver/chromeself.driver.exe')
        self.driver.get(upper_url)
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
    
        self.counter = 0
        self.succounter = 0
        delay=1000
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '')))
        x=self.driver.find_element_by_xpath('//*[@id="searchWordForm"]')
        webdriver.ActionChains(self.driver).move_to_element(x).click(x).send_keys(item_name,Keys.ENTER).perform()
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        if not os.path.exists(self.rpath):
            os.mkdir(self.rpath)
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
            sleep(0.1)
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
            
     
            
        for x in self.driver.find_elements_by_xpath('//img'):
            try:
                self.counter = self.counter + 1
                print ("Total Count:", self.counter)
                print ("Succsessful Count:", self.succounter)
                print ("URL:",x.get_attribute('src'))
            
                # 이미지 url
                self.img = x.get_attribute('src')
                # 이미지 확장자
                self.imgtype ="jpg"
                self.first_url ="https://img.alicdn.com/imgextra/"
                self.ben_url= '60x60q90.jpg'
                self.ben_url2= '430x430q90.jpg'
            except:  
                pass
            # 구글 이미지를 읽고 저장한다.
            try:
                req = urllib.request.Request(self.img, headers=self.header)
                
                if self.img[-3:] == self.imgtype and self.img[:len(self.first_url)] == self.first_url :
                
                #raw_self.img = urllib.request.urlopen(req.data).read()
                    if self.img[-len(self.ben_url):] != self.ben_url and self.img[-len(self.ben_url2):] != self.ben_url2:
                        self.succounter = self.succounter  + 1 
            
                        urllib.request.urlretrieve(req.get_full_url(),os.path.join(self.rpath , searchterm + "_" + str(self.succounter) + "." + self.imgtype))
            except:
                pass
        print (self.succounter, "succesfully downloaded")
        return self.succounter
        
class Kukje:
        
    def imgcrawl(self,searchterm,upper_path,item_url):
        
        self.searchterm2 = searchterm +'/'
    
        self.rpath= upper_path + self.searchterm2
        # chrom webself.driver 사용하여 브라우저를 가져온다.
        self.driver = webdriver.Chrome('C:/chromeself.driver/chromeself.driver.exe')
        self.driver.get(item_url)
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}
    
        self.counter = 0
        self.succounter = 0
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
        if not os.path.exists(self.rpath):
            os.mkdir(self.rpath)
        self.driver.implicitly_wait(10)
        for _ in range(300):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
            sleep(0.1)
            self.driver.execute_script("window.scrollBy(0,{})".format(_))
            
     
            
        for x in self.driver.find_elements_by_xpath('//img'):
            try:
                self.counter = self.counter + 1
                print ("Total Count:", self.counter)
                print ("Succsessful Count:", self.succounter)
                print ("URL:",x.get_attribute('src'))
            
                # 이미지 url
                self.img = x.get_attribute('src')
                # 이미지 확장자
                self.imgtype ="jpg"
                self.first_url ="https://img.alicdn.com/imgextra/"
                self.ben_url= '60x60q90.jpg'
                self.ben_url2= '430x430q90.jpg'
            except:  
                pass
            # 구글 이미지를 읽고 저장한다.
            try:
                req = urllib.request.Request(self.img, headers=self.header)
                
                if self.img[-3:] == self.imgtype and self.img[:len(self.first_url)] == self.first_url :
                
                #raw_self.img = urllib.request.urlopen(req.data).read()
                    if self.img[-len(self.ben_url):] != self.ben_url and self.img[-len(self.ben_url2):] != self.ben_url2:
                        self.succounter = self.succounter + 1 
            
                        urllib.request.urlretrieve(req.get_full_url(),os.path.join(self.rpath , searchterm + "_" + str(self.succounter) + "." + self.imgtype))
            except:
                pass
        print (self.succounter, "succesfully downloaded")
        return self.succounter