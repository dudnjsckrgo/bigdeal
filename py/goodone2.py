# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib.parse
import urllib.request
from PIL import Image

from googletrans import Translator
import pytesseract
from http import cookiejar

import cv2

#저장할 이미지 이름
import imutils
d="skindd"
#url 입력
url = ('https://smartstore.naver.com/ugot/products/4636408608')
#실행 언어 설정
lang1= 'kor'
 # html 소스 가져오기
text1 = requests.get(url).text
#text1 = urllib.parse.quote(text1)
# html 문서로 파싱
text_source = StringIO(text1)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음
imgs = doc.findall(".//img")


img_list = []   # 이미지 경로가 담길 list

for a in imgs:   
    img_list.append(a.get('src'))
    #print(a.get('src'))
    
img_list=list(set(img_list))
b=0
for a in img_list:
    b += 1
    saveName=d+str(b)+".jpg"
    urllib.request.urlretrieve("http:"+a,saveName)

b=0

for a in img_list:
    b+=1
    saveName = d+str(b)+".jpg"
    imgFile ='C:/Users/yyw/.spyder-py3/'+saveName
    
    # Read the image file
    img = cv2.imread(imgFile)
    # Resize the image - change width to 500
    #img= imutils.resize(img, width=500)
    
    # Display the original image
   
    
    tex = pytesseract.image_to_string( img , lang=lang1 )
    
    #print(tex)
    
    translator = Translator()
    print("------------------"+str(b)+"---------------------")
    print(translator.translate(tex,dest='ko').text)
    
    
 



