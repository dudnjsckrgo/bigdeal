# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:57:04 2019

@author: yyw
"""
# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('C:/Users/Administrator/Downloads/tutorial.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0)
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 
