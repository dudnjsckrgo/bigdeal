# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:57:04 2019

@author: yyw
"""
 # importing required modules
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen
from googletrans import Translator v

# 다음 코드는 라이브러리에서 PDF 파일을 읽을 시 사용하는 전형적인 코드 형태이므로, 필요할 때 활용하면 됨
def read_pdf_file(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content
pdf_file = open("C:/Users/yyw/.spyder-py3/pws.pdf", "rb+")
contents = read_pdf_file(pdf_file)

print(len(contents))
listcontent= contents.split('.')

#with open('t2.txt','w+',encoding ='utf-8') as f1:
for a in listcontent:
    translator = Translator()
    
    print(translator.translate(a,dest='ko').text)
   #     f1.write(contents.text)
    
pdf_file.close()
