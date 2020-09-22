# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:57:04 2019

@author: yyw
"""
 # importing required modules
 
from pdfminer1.pdfinterp import PDFResourceManager, process_pdf
from pdfminer1.converter import TextConverter
from pdfminer1.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen
from googletrans import Translator
from pdfminer1.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer1.converter import TextConverter
from pdfminer1.layout import LAParams


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
def pdftolist(path):
    pdf_file = open(path, "rb+")
    contents = read_pdf_file(pdf_file)
    
    print(len(contents))
    listcontent= contents.split('.')
    
    with open('t2.txt','w+',encoding ='utf-8') as f1:
        b=0
        for a in listcontent:
            b+=1
            #translator = Translator()
            #print(translator.translate(a,dest='ko').text)
            f1.write(a+'\n')
        
    pdf_file.close()
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
pdftolist("C:/Users/Administrator/Downloads/tutorial.pdf")