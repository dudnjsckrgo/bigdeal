# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:59:53 2019

@author: Administrator
"""

import PyPDF2
pdf_file = open('C:/Users/Administrator/Downloads/tutorial.pdf','rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print(page_content)