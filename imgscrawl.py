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
searchterm = 'item'
searchterm2 = searchterm +'/'
upper_path= '/Users/yyw/Desktop/ugot/'
rpath= upper_path + searchterm2
# chrom webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
browser.get('https://item.taobao.com/item.htm?spm=2013.1.20141003.4.15f83eec1zP1dA&scm=1007.10011.70203.100200300000001&id=39519371533&pvid=ee905aef-e080-437f-b719-f3b5a62bb2e5')
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
counter = 0
succounter = 0
 
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
if not os.path.exists(rpath):
    os.mkdir(rpath)

for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.implicitly_wait(0.3)
    browser.execute_script("window.scrollBy(0,{})".format(_))
    
for x in browser.find_elements_by_xpath('//*[@id="J_DivItemDesc"]//img'):
    
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",x.get_attribute('src'))

    # 이미지 url
    img = x.get_attribute('src')
    # 이미지 확장자
    imgtype = "jpg"
    first_url ="https://img.alicdn.com/imgextra/"
    # 구글 이미지를 읽고 저장한다.
    try:
        req = urllib.request.Request(img, headers={'User-Agent': header})
        if img[-3:] == imgtype and img[:len(first_url)] == first_url :
        #raw_img = urllib.request.urlopen(req.data).read()
            succounter = succounter + 1 
            urllib.request.urlretrieve(req.get_full_url(),os.path.join(rpath , searchterm + "_" + str(succounter) + "." + imgtype))
 
        
    except:
        pass
print (succounter, "succesfully downloaded")


'''
   req = urllib.request.Request(img, headers={'User-Agent': header})

    raw_img = urllib.request.urlopen(req.data).read()
    File = open(os.path.join(rpath , searchterm + "_" + str(counter) + "." + imgtype)
    File.write(raw_img)
    File.close()
    succounter = succounter+1
'''