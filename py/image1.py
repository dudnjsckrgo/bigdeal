# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib.request

# 검색할 이미지의 키워드 입력

url = 'https://detail.tmall.com/item.htm?id=564610856465&spm=a21wu.241046-kr.4691948847.7.41cab6cbU1bptG&scm=1007.15423.84311.100200300000001&pvid=acd3b122-e351-440c-826f-02c3afe19805&sku_properties=134942334:28383'

 # html 소스 가져오기
text = requests.get(url).text

# html 문서로 파싱
text_source = StringIO(text)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음
imgs = doc.findall('.//img')

img_list = []   # 이미지 경로가 담길 list
b=0
for a in imgs:
    b+=1
    saveName=str(b)+".jpg"
    img_list.append(a.get('src'))
    print(a.get('src'))
    urllib.request.urlretrieve("http:"+a.get('src'),saveName)
