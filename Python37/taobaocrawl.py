# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:23:27 2019

@author: yyw
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
#크롬 웹 드라이버의 경로를 설정
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
# 크롬을 통해 네이버 로그인 화면에 접속
driver.get("http://www.donga.com/news/article/all/20171227/87929276/4")
#아이디와 비밀번호를 입력합니다.(0.5초씩 기다리기)
############################################
username = "skyutech"
password = "sky4275"
############################################
sleep(0.5)#트래킹 공격이라 인식할수있게때문에 정보에 딜레이를 준다
driver.find_element_by_id("TPL_username_1").send_keys(username)
sleep(1);
driver.find_element_by_id("TPL_password_1").send_keys(password)
sleep(1);
'''
id = 'skyutech'
pw = 'sky4275'
sleep(1)
driver.execute_script("document.getElementsByName('TPL_username')[0].value=\'" + id + "\'")
sleep(1)
driver.execute_script("document.getElementsByName('TPL_password')[0].value=\'" + pw + "\'")
sleep(1)

#xpath를 이용해 로그인을 시도
driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
'''


html= driver.page_source
print(html.text)
soup= BeautifulSoup(html,'lxml') #파싱할수있는 형태로 초기화

#메일 제목을 하나씩 파싱합니다.
title_list =soup.find_all('strong','mail_title')#strong 태그의 mail_title이란 클래스를 파싱
#모든 메일 제목을 출력합니다.
for title in title_list:
    print(title.text)

    
