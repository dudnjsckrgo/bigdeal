# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:19:51 2019

@author: Administrator
"""

import pyautogui
from selenium.webself.driver.support.ui import Webself.driverWait
from selenium.webself.driver.support import expected_conditions
from selenium.webself.driver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from openpyxl import load_workbook
from selenium import webself.driver
import re
from time import sleep

#exel_path ='/Users/Administrator/Downloads/온라인판매20190726.xlsx'
import pyperclip, pyautogui 
self.driver = webself.driver.Chrome('C:/chromeself.driver/chromeself.driver.exe')
self.driver.get('https://itemscout.io/')
sleep(3)
delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="container"]/table[1]/tr/td[2]/div/div[1]/span')))
x=self.driver.find_element_by_xpath('//*[@id="container"]/table[1]/tr/td[2]/div/div[1]/span')
webself.driver.ActionChains(self.driver).move_to_element(x).click(x).perform()
sleep(2)
delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'itemscout-dropdown-item')))
self.one_division=self.driver.find_elements_by_class_name('itemscout-dropdown-item')


self.one_division[0].click()
sleep(5)

delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="container"]/table[1]/tr/td[2]/div/div[2]/span')))
x=self.driver.find_element_by_xpath('//*[@id="container"]/table[1]/tr/td[2]/div/div[2]/span')
webself.driver.ActionChains(self.driver).move_to_element(x).click(x).perform()

sleep(3)
delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'itemscout-dropdown-item')))
self.two_division=self.driver.find_elements_by_class_name('itemscout-dropdown-item')

self.two_division[0].click()
sleep(5)

delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="container"]/table[1]/tr/td[2]/div/div[3]/span')))
x=self.driver.find_element_by_xpath('//*[@id="container"]/table[1]/tr/td[2]/div/div[3]/span')
webself.driver.ActionChains(self.driver).move_to_element(x).perform()
webself.driver.ActionChains(self.driver).move_to_element(x).click(x).perform()
sleep(3)
delay=1000
Webself.driverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'itemscout-dropdown-item')))
self.three_division=self.driver.find_elements_by_class_name('itemscout-dropdown-item')

self.three_division[0].click()
sleep(5)
for _ in range(80):
        
    self.driver.execute_script("window.scrollBy(0,{})".format(_))
    
self.name_tables=self.driver.find_elements_by_xpath('//*[@id="container"]/div[2]/table/tbody/tr/td[2]/a/label')
self.comp_tables=self.driver.find_elements_by_xpath('//*[@id="container"]/div[2]/table/tbody/tr/td[7]/a/label')

x=self.name_tables[0]
x=x.get_attribute('innerHTML').strip()
print(x)

x=self.comp_tables[0]
x=x.get_attribute('innerHTML').strip()
print(x)
 





'''   print(x)
html = x.get_attribute('innerHTML')
re_img = re.compile("<[Ii][Dd][=]\s+[^>]+>", re.MULTILINE)

img_tag = re_img.findall(html)
print(img_tag)
'''