# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:12:34 2019

@author: yyw
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/Users/yyw/.spyder-py3/chromedriver.exe' # 윈도우 
#chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

# 크롤링할 사이트 호출
driver.get("http://www.python.org")

# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
assert "Python" in driver.title

# <input id="id-search-field" name="q" 검색창 name으로 검색하기
# 태그 name으로 특정한 태그를 찾을 수 있음
elem = driver.find_element_by_name("q")

# input 텍스트 초기화 
# elem.clear()

# 키 이벤트 전송가능함
# 태그가 input 태그이므로 입력창에 키이벤트가 전달되면, 입력값이 자동으로 작성됨
elem.send_keys("pycon")

# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
elem.send_keys(Keys.RETURN)

# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
assert "No results found." not in driver.page_source

# 명시적으로 일정시간을 기다릴 수 있음 (10초 기다림)
time.sleep(10)

# 크롬 브라우저 닫기 가능함
driver.quit()