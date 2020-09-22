# -*- coding: utf-8 -*-
import requests
from lxml.html import parse
from io import StringIO
import urllib.parse
import urllib.request
from googletrans import Translator
import pytesseract
import cv2
from PIL import Image
import img2pdf
import os 
#저장할 이미지 이름

'''
def imgcrawl1(url,file_name):
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
'''    
   
def imgocr(file_name,lang,upper_path,model,text_name,num):
    for a in range(1,num):
        saveName = file_name+'_'+str(a)+"."+model
        imgFile = upper_path + saveName
        image = cv2.imread(imgFile)
        tex = pytesseract.image_to_string(image, lang=lang)
        try:
            print(tex)
            translator = Translator()
            print(translator.translate(tex,dest='ko').text)
            with open(upper_path[2:]+text_name+'_'+lang+'.txt','a+',encoding ='utf-8') as f1:
                f1.write("-----------------------------------------------------------"+str(a)+"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f1.write(tex+'\n')
                
            with open(upper_path+text_name+'_번역.txt','a+',encoding ='utf-8') as f2:
                f2.write("-----------------------------------------------------------"+str(a)+"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f2.write(translator.translate(tex,dest='ko').text+'\n')
        except:
            print(tex)
            translator = Translator()
            print(translator.translate(tex,dest='ko').text)
            with open(upper_path[2:]+text_name+'.txt','a+',encoding ='utf-8') as f1:
                f1.write("-----------------------------------------------------------"+str(a)+"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                f1.write(tex+'\n')

def img2pdf1(num,file_name,upper_path,model):
    for a in range(2,num):  
        # storing image path 
        saveName = file_name+'_'+str(a)+"."+model
        img_path = upper_path+saveName
        # storing pdf path 
        filename1 = file_name+'_'+str(a)+".pdf"
        pdf_path = upper_path+filename1
          
        # opening image 
        image = Image.open(img_path) 
        #resize_image=image.resize((640, 640))  
        # converting into chunks using img2pdf 
        pdf_bytes = img2pdf.convert(image.filename) 
          
        # opening or creating pdf file 
        file = open(pdf_path, "wb") 
          
        # writing pdf files with chunks 
        file.write(pdf_bytes) 
          
        # closing image file 
        image.close() 
          
        # closing pdf file 
        file.close() 
          
        # output 
        print("Successfully made pdf file") 
def imgresize(file_name,upper_path,model,num):
     for a in range(1,2):  
        # storing image path 
        saveName = file_name+'_'+str(a)+"."+model
        img_path = upper_path+saveName
        filename1 = file_name+'_'+str(a)+".jpg"
        jpg_path = upper_path+filename1
        # storing pdf path 
        size=(640,640)
        # opening image 
        image = Image.open(img_path)
        '''
        image=image.thumbnail(size, Image.ANTIALIAS) 
        '''
        resize_img= image.resize(size)
        # converting into chunks using img2pdf 
        resize_img.save(jpg_path)  
        
        # output 
        print("Successfully made resize jpg file")
'''     
upper_path=input('상위폴더를 지정하시오\n')#"C:/Users/Administrator/Desktop/ugot/a/"
if upper_path=="":
    upper_path="C:/Users/Administrator/Desktop/ugot/a/item/"
model=input("확장자를 지정하시오\n") #"gif"
if model=="":
    model="jpg"            
text_name=input("텍스트이름을 지정하시오\n")#"text"
if text_name == "":
    text_name="text"
num=input("이미지의 개수를 입력하시오\n")#19
num=int(num)+1
file_name=input("파일이름을 지정하시오\n")#1
if file_name=="":
    file_name="item"
#imgocr(file_name="1",lang1= 'chi_sim',upper_path=upper_path,model=model,text_name=text_name,num=num)
imgresize(file_name=file_name,upper_path=upper_path,model=model,num=num)
img2pdf1(file_name=file_name,upper_path=upper_path,model=model,num=num)
'''