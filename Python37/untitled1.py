# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:59:21 2019

@author: Administrator
"""
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request
 
#찾고자 하는 검색어를 url로 만들어 준다.
searchterm = 'person'
searchterm2 = searchterm +'/'
upper_path= '/Users/Administrator/Desktop/ugot/a/'
rpath= upper_path + searchterm2
# chrom webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
browser.get('https://www.google.com/search?q=person&source=lnms&tbm=isch')
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
counter = 0
succounter = 0
 
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
if not os.path.exists(rpath):
    os.mkdir(rpath)

for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")
    
for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
 
    # 이미지 url
    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    # 이미지 확장자
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    
    # 구글 이미지를 읽고 저장한다.

    req = urllib.request.Request(img, headers={'User-Agent': header})
    raw_img = urllib.request.urlopen(req).read()
    File = open(os.path.join(rpath , searchterm + "_" + str(counter) + "." + imgtype), "wb")
    File.write(raw_img)
    File.close()
    succounter = succounter + 1

print (succounter, "succesfully downloaded")
browser.close()
