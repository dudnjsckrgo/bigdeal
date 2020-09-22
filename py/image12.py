# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib.request


from googletrans import Translator
import pytesseract
import cv2
import  imutils
#저장할 이미지 이름
d="car"
#url 입력
url = ('https://korean.alibaba.com/product-detail/creality-mini-3d-printer-printing-size-220-220-250mm-diy-ender-3-pro-3d--62023231479.html?spm=a2700.8270666-43.2016122619263.12.1def2f91AYn7vx')

 # html 소스 가져오기
text1 = requests.get(url).text

# html 문서로 파싱
text_source = StringIO(text1)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음
imgs = doc.findall('.//img')


img_list = []   # 이미지 경로가 담길 list
b=0
for a in imgs:   
    img_list.append(a.get('src'))
    print(a.get('src'))
    
img_list=list(set(img_list))
'''
for a in img_list:
    b+=1
    saveName=d+str(b)+".jpg"
    urllib.request.urlretrieve("http:"+a,saveName)
'''
b=1
saveName=d+str(b)+".jpg"
imgFile1 ='C:/Users/yyw/.spyder-py3/'+saveName
img1= cv2.imread(imgFile1);
img1= imutils.resize(img1, width=500)
for a in img_list:
    b+=1
    saveName=d+str(b)+".jpg"
    imgFile2 ='C:/Users/yyw/.spyder-py3/'+saveName
    img2= cv2.imread(imgFile2);
    img2= imutils.resize(img2, width=500)
    addv = np.vstack((img1,img2))

cv2.imshow('imgv',addv)
cv2.waitKey(0)