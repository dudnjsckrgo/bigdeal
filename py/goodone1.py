# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib.request
import re
from googletrans import Translator
import pytesseract

import cv2
import imutils
#저장할 이미지 이름
d="car"
#url 입력
url = ('https://detail.tmall.com/item.htm?id=564610856465&spm=a21wu.241046-kr.4691948847.7.41cab6cbU1bptG&scm=1007.15423.84311.100200300000001&pvid=acd3b122-e351-440c-826f-02c3afe19805&sku_properties=134942334:28383')
#실행 언어 설정
lang1= 'chi_sim'
 # html 소스 가져오기
text1 = requests.get(url).text

# html 문서로 파싱
text_source = StringIO(text1)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음

imgs = doc.findall('.jpg')


img_list = []   # 이미지 경로가 담길 list

for a in imgs:   
    img_list.append(a.get('src'))
    print(a.get('src'))
    '''
img_list=list(set(img_list))
b=0
for a in img_list:
    b+=1
    saveName=d+str(b)+".jpg"
    urllib.request.urlretrieve("http:"+a,saveName)

b=0

for a in img_list:
    b+=1
    saveName=d+str(b)+".jpg"
    imgFile ='C:/Users/yyw/.spyder-py3/'+saveName
    
    # Read the image file
    img= cv2.imread(imgFile);
    # Resize the image - change width to 500
    img= imutils.resize(img, width=500)
    
    # Display the original image
    cv2.imshow("Original Image", img)
    
    tex = pytesseract.image_to_string(img ,lang=lang1)
    
    print(tex)
    
    translator = Translator()
    
    print(translator.translate(tex,src='zh-cn',dest='ko').text)
    
    cv2.namedWindow("Input image")
    
    cv2.imshow("input image",img)
    cv2.waitKey(0)
    

    
cv2.destroyWindow("Test")
    
cv2.destroyWindow("Main")

 
    # RGB to Gray scale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("1 - Grayscale Conversion", gray)
    
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow("2 - Bilateral Filter", gray)


# Noise removal with iterative bilateral filter(removes noise while preserving edges)
#gray = cv2.bilateralFilter(gray, 11, 17, 17)
#cv2.imshow("3 - Bilateral Filter", gray)


# Find Edges of the grayscale image
edged = cv2.Canny(gray, 170, 200)
#cv2.imshow("4 - Canny Edges", edged)
'''

