# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:00:27 2019

@author: yyw
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#import imgscrawl
from time import sleep
import pickle
############################################
username = "skyutech"
password = "sky4275"
############################################


driver= webdriver.Chrome('C:/chromedriver/chromedriver.exe')

#driver.get("https://i.taobao.com/my_taobao.htm?nekot=c2t5dXRlY2g%3D1566976500555")
class Taobao:


    def __init__(self):
        self.open()
        self.save_cookie(driver,path)
        self.load_cookie(driver,path)
        self.login()
        #self.imgcrawling()
        #self.order()
        # self.payment()


    def open(self):
        driver.get("https://login.taobao.com/member/login.jhtml")
    def save_cookie(self,driver, path): 
        cookies_list = driver.get_cookies()
        print(cookies_list)
        print('\n')
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        print(cookies_dict)
        with open(path, 'wb') as filehandler:
            pickle.dump(cookies_dict, filehandler)
    def load_cookie(self,driver, path):
        with open(path, 'rb') as cookiesfile:
             cookies = pickle.load(cookiesfile)
        for key in cookies:
             driver.add_cookie({'name' : '{}'.format(key) , 'value' : '{}'.format(cookies[key])})
        
    def login(self):
        driver.get("https://login.taobao.com/member/login.jhtml")
        ############################################
        username = "skyutech"
        password = "sky4275"
        ############################################
        sleep(0.5)#트래킹 공격이라 인식할수있게때문에 정보에 딜레이를 준다
        driver.find_element_by_id("TPL_username_1").send_keys(username)
        sleep(1);
        driver.find_element_by_id("TPL_password_1").send_keys(password)
        sleep(1);
         #   def imgcrawling():
  #      imgscrawl
        


if __name__ == "__main__":
    nike = Taobao()
