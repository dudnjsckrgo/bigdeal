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
from time import sleep

#찾고자 하는 검색어를 url로 만들어 준다.
item_name=''
upper_url=' http://www.all4sound.com/product/search_product.asp?product_name='
url = upper_url+item_name

def imgcrawl(searchterm,upper_path,item_url):
    
    searchterm2 = searchterm +'/'

    rpath= upper_path + searchterm2
    # chrom webdriver 사용하여 브라우저를 가져온다.
    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    driver.get(item_url)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.132 Safari/537.36'}

    counter = 0
    succounter = 0
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
    if not os.path.exists(rpath):
        os.mkdir(rpath)
    driver.implicitly_wait(10)
    for _ in range(300):
        # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
        sleep(0.1)
        driver.execute_script("window.scrollBy(0,{})".format(_))
        
 
        
    for x in driver.find_elements_by_xpath('//img'):
        try:
            counter = counter + 1
            print ("Total Count:", counter)
            print ("Succsessful Count:", succounter)
            print ("URL:",x.get_attribute('src'))
        
            # 이미지 url
            img = x.get_attribute('src')
            # 이미지 확장자
            imgtype ="jpg"
            first_url ="https://img.alicdn.com/imgextra/"
            ben_url= '60x60q90.jpg'
            ben_url2= '430x430q90.jpg'
        except:  
            pass
        # 구글 이미지를 읽고 저장한다.
        try:
            req = urllib.request.Request(img, headers={'User-Agent': header})
            
            if img[-3:] == imgtype and img[:len(first_url)] == first_url :
            
            #raw_img = urllib.request.urlopen(req.data).read()
                if img[-len(ben_url):] != ben_url and img[-len(ben_url2):] != ben_url2:
                    succounter = succounter + 1 
        
                    urllib.request.urlretrieve(req.get_full_url(),os.path.join(rpath , searchterm + "_" + str(succounter) + "." + imgtype))
        except:
            pass
    print (succounter, "succesfully downloaded")
    return succounter
    
    
    '''
       req = urllib.request.Request(img, headers={'User-Agent': header})
    
        raw_img = urllib.request.urlopen(req.data).read()
        File = open(os.path.join(rpath , searchterm + "_" + str(counter) + "." + imgtype)
        File.write(raw_img)
        File.close()
        succounter = succounter+1
    '''
'''
upper_path=   "C:/Users/Administrator/Desktop/ugot/a/"
searchterm= "item"
item_url="https://detail.tmall.com/item.htm?spm=a220o.1000855.0.0.74c9770280no99&pvid=82bb3da4-ff09-41b4-afd5-bf2cea49c07c&pos=12&acm=03067.1003.1.1977615&id=566800210221&scm=1007.12776.82642.100200300000000&sku_properties=134942334:28316"
imgcrawl(searchterm,upper_path,item_url)
'''