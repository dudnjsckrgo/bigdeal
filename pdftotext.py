# -*- coding: utf-8 -*-

from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
  
# Path of the pdf 
PDF_file = '/Users/yyw/Desktop/study/water/2 Wastewater Characteristics.pdf'#"/Users/yyw/.spyder-py3/python_pdf/L9.pdf" '/Users/yyw/Desktop/공부/화학적수처리'
upper_path='/Users/yyw/Desktop/ugot'  
 
#Part #1 : Converting PDF to images 

def pdftoimg(PDF_file,upper_path): 
    # Store all the pages of the PDF in a variable 
    pages = convert_from_path(PDF_file) 
      
    # Counter to store images of each page of PDF to image 
    image_counter = 1
      
    # Iterate through all the pages stored above 
    for page in pages: 
      
        # Declaring filename for each page of PDF as JPG 
        # For each page, filename will be: 
        # PDF page 1 -> page_1.jpg 
        # PDF page 2 -> page_2.jpg 
        # PDF page 3 -> page_3.jpg 
        # .... 
        # PDF page n -> page_n.jpg 
        filename = "page_"+str(image_counter)+".jpg"
        file_path=upper_path+filename
        # Save the image of the page in system
        if not os.path.exists(file_path):
            page.save(file_path, 'JPEG') 
          
            # Increment the counter to update filename 
            image_counter = image_counter + 1
        else:
            mage_counter = image_counter + 1
            pass
     
#Part #2 - Recognizing text from the images using OCR 

def pagestotext(upper_path,image_counter):  
# Variable to get count of total number of pages 
    filelimit = image_counter
      
    # Creating a text file to write the output 
    outfile = "out_text.txt"
      
    # Open the file in append mode so that  
    # All contents of all images are added to the same file 
    f = open(upper_path+outfile,'a+',encoding ='utf-8') 
      
    # Iterate from 1 to total number of pages 
    for i in range(1, filelimit + 1): 
      
        # Set filename to recognize text from 
        # Again, these files will be: 
        # page_1.jpg 
        # page_2.jpg 
        # .... 
        # page_n.jpg 
        filename = "page_"+str(i)+".jpg"
        file_path=upper_path+filename      
        # Recognize the text as string in image using pytesserct 
        text = pytesseract.image_to_string(Image.open(file_path))
        print(text)
      
        # The recognized text is stored in variable text 
        # Any string processing may be applied on text 
        # Here, basic formatting has been done: 
        # In many PDFs, at line ending, if a word can't 
        # be written fully, a 'hyphen' is added. 
        # The rest of the word is written in the next line 
        # Eg: This is a sample text this word here GeeksF- 
        # orGeeks is half on first line, remaining on next. 
        # To remove this, we replace every '-\n' to ''. 
        text = text.replace('-\n', '')     
      
        # Finally, write the processed text to the file. 
        f.write(text) 
      
    # Close the file after writing all the text. 
    f.close()
pdftoimg(PDF_file,upper_path)    
 