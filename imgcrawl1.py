# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import urllib.parse
from urllib.request import urlopen as uReq 
from googletrans import Translator
import pytesseract
import cv2
from PIL import Image
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup 
import re
import urllib3
import sele
#저장할 이미지 이름


def imgcrawl(url,file_name):
    d=file_name
     # html 소스 가져오기
    
   
    uClient = uReq(url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    link_info_list = [] 
    
    containers = page_soup.findAll("img")
    
    print(containers)
    img_list = [] 
   # img_src=img.get("src")
    
    for a in containers:   
        img_list.append(a.get('src'))
        #print(a.get('src'))
        
    
    b=0
    for a in img_list:
        b += 1
        saveName=d+str(b)+".jpg"
        urllib.request.urlretrieve("http:"+a,saveName)
   
   
def imgocr(file_name,lang1):
    d=file_name
    for a in range(1,21):
        saveName = d+' ('+str(a)+')'+".jpg"
        imgFile ='C:/Users/yyw/.spyder-py3/img/'+saveName
        image = cv2.imread(imgFile)
        tex = pytesseract.image_to_string(image, lang=lang1)
        
        print(tex)
        
        with open('t4.txt','a+',encoding ='utf-8') as f1:
            f1.write("-----------------------------------------------------------"+str(a)+"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f1.write(tex+'\n')
        
imgcrawl("https://item.taobao.com/item.htm?spm=a21wu.241046-kr.4691948847.195.41cab6cbxF6YRN&scm=1007.15423.84311.100200300000004&id=559511051941&pvid=06f76c49-96dd-43d9-9057-846118250fc9","2")



