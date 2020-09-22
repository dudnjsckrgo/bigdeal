# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:55:55 2019

@author: yyw
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
#크롬 웹 드라이버의 경로를 설정
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
# 크롬을 통해 네이버 로그인 화면에 접속
driver.get('https://nid.naver.com/nidlogin.login')
#아이디와 비밀번호를 입력합니다.(0.5초씩 기다리기)
'''
sleep(0.5)#트래킹 공격이라 인식할수있게때문에 정보에 딜레이를 준다
driver.find_element_by_name('id').send_keys('lisk9401')
sleep(0.5)
driver.find_element_by_name('pw').send_keys('2019sky!')
'''
id = 'lisk9401'
pw = '2019sky!'
sleep(1)
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
sleep(1)
#xpath를 이용해 로그인을 시도
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
sleep(1)
driver.get("http://mail.naver.com")
html= driver.page_source
soup= BeautifulSoup(html,'lxml') #파싱할수있는 형태로 초기화
#메일 제목을 하나씩 파싱합니다.
title_list =soup.findAll('strong', {"class":"mail_title"})#strong 태그의 mail_title이란 클래스를 파싱
#모든 메일 제목을 출력합니다.
for title in title_list:
    print(title.text)
    