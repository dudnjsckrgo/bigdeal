# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:54:35 2019

@author: yyw
"""
 
from PyPDF2 import PdfFileWriter, PdfFileReader

 

# Creating a routine that appends files to the output file

def append_pdf(input,output):

    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

 
def mergeall(file_name,upper_path,num):
# Creating an object where pdf pages are appended to    
    output = PdfFileWriter()
    
    for a in range(2,num): 
        
        # Appending two pdf-pages from two different files
        filename = file_name+'_'+str(a)+".pdf"
        
        pdf_path = upper_path+filename
        
        append_pdf(PdfFileReader(open(pdf_path,"rb")),output)
        
        # Writing all the collected pages to a file
    output.write(open(upper_path+"CombinedPages.pdf","wb"))
    
#mergeall(file_name="1",upper_path="C:/Users/Administrator/Desktop/ugot/a/",num=19)    