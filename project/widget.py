# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:48:35 2019

@author: Administrator
"""
import imgcrawl
import mergepdf
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import imgscrawl
import pdftotext
CalUI='./_uiFiles/project.ui'
class ExWindow(QDialog):
 
    def __init__(self):
        super().__init__()
        uic.loadUi(CalUI,self)
        
        self.init_ui()
        
    def init_ui(self):
        self.q_lineEdit_1.setText("C:/Users/Administrator/Desktop/ugot/a/")
        self.q_lineEdit_2.setText("jpg")
        self.q_lineEdit_3.setText("item")
        self.q_lineEdit_4.setText("CombinedPages_OCR")
        self.q_lineEdit_5.setText("item_url")
        self.q_lineEdit_6.setText("chi_sim")
        
        self.pushButton.clicked.connect(self.imgtopdf)
        self.pushButton_1.clicked.connect(self.imgtranslate)
        self.pushButton_2.clicked.connect(self.pdfmerge)
        self.pushButton_3.clicked.connect(self.imgcrawl)
        self.pushButton_4.clicked.connect(self.oneforall)
        self.pushButton_5.clicked.connect(self.imgresizing)
        self.pushButton_6.clicked.connect(self.pdftoimg)
        
        self.reset_pushButton.clicked.connect(self.Reset)
        self.reset_pushButton_1.clicked.connect(lambda state,num=self.q_lineEdit_1: self.Delete(state,num))
        self.reset_pushButton_2.clicked.connect(lambda state,num=self.q_lineEdit_2: self.Delete(state,num))
        self.reset_pushButton_3.clicked.connect(lambda state,num=self.q_lineEdit_3: self.Delete(state,num))
        self.reset_pushButton_4.clicked.connect(lambda state,num=self.q_lineEdit_4: self.Delete(state,num))
        self.reset_pushButton_5.clicked.connect(lambda state,num=self.q_lineEdit_5: self.Delete(state,num))
        self.reset_pushButton_6.clicked.connect(lambda state,num=self.q_lineEdit_6: self.Delete(state,num))
        self.show()
        
    def imgtopdf(self):

        upper_path = self.q_lineEdit_1.text()
        model = self.q_lineEdit_2.text()
        num=self.succounter
        num= num+1
        searchterm = self.q_lineEdit_3.text()
        imgcrawl.img2pdf1(file_name=searchterm,upper_path=upper_path,model=model,num=num)
        self.a_lineEdit.setText("이미지를 pdf로")

    def imgtranslate(self):

        upper_path = self.q_lineEdit_1.text()
        model = self.q_lineEdit_2.text()
        searchterm = self.q_lineEdit_3.text()    
        num=self.succounter
        num= num+1
        lang= self.q_lineEdit_6.text()
        imgcrawl.imgocr(file_name=searchterm,lang=lang,upper_path=upper_path,model=model,num=num,text_name=searchterm)
        self.a_lineEdit.setText("이미지에서 텍스트 추출")

        
    def pdfmerge(self):
        
        upper_path = self.q_lineEdit_1.text()
        num=self.succounter
        num= num+1
        searchterm = self.q_lineEdit_3.text()
        mergepdf.mergeall(file_name=searchterm,upper_path=upper_path,num=num)
        self.a_lineEdit.setText("pdf 합성 완료")
        
    def imgcrawl(self):
        
        upper_path = self.q_lineEdit_1.text()
        searchterm = self.q_lineEdit_3.text()
        item_url = self.q_lineEdit_5.text()
        self.succounter=imgscrawl.imgcrawl(searchterm=searchterm,upper_path=upper_path,item_url=item_url)
        self.a_lineEdit.setText("이미지 크롤 완료")
        upper_path=upper_path+searchterm+'/'
        self.q_lineEdit_1.setText(upper_path)
        
        
    
    def Reset(self):
        self.q_lineEdit_3.clear()
        self.q_lineEdit_4.clear()
        self.q_lineEdit_5.clear()
        

    def Delete(self,state,num):
        num.clear()
    def pdftoimg(self):
        PDF_file_path = "/Users/Administrator/Desktop/ugot/combinepage/"
        upper_path = self.q_lineEdit_1.text() 
        pdf_file_name=self.q_lineEdit_4.text()
        searchterm = self.q_lineEdit_3.text()
        upper_path=upper_path+searchterm+'/'
        pdftotext.pdftoimg(PDF_file_path,pdf_file_name,upper_path,item_name=searchterm)
        self.a_lineEdit.setText(upper_path + '에 들어가 있어요')
        
    def oneforall(self):
        
        upper_path = self.q_lineEdit_1.text()
        searchterm = self.q_lineEdit_3.text()
        item_url = self.q_lineEdit_5.text()
        lang= self.q_lineEdit_6.text()
        num = imgscrawl.imgcrawl(searchterm,upper_path,item_url=item_url)     
        num =num+1
        self.a_lineEdit.setText("이미지 크롤 완료")
        upper_path=upper_path+searchterm+'/'
        model = self.q_lineEdit_2.text()
        imgcrawl.imgresize(file_name=searchterm,upper_path=upper_path,model=model,num=num)
        self.a_lineEdit.setText("이미지를 리사이징")
        imgcrawl.img2pdf1(file_name=searchterm,upper_path=upper_path,model=model,num=num)
        self.a_lineEdit.setText("이미지를 pdf로")
        mergepdf.mergeall(file_name=searchterm,upper_path=upper_path,num=num)
        self.a_lineEdit.setText("pdf 합성 완료")
        imgcrawl.imgocr(file_name=searchterm,lang=lang,upper_path=upper_path,model=model,num=num,text_name=searchterm)
        self.a_lineEdit.setText("이미지에서 텍스트 추출")
        
        self.a_lineEdit.setText("끝")
        
    def imgresizing(self):
        
        upper_path = self.q_lineEdit_1.text()
        model = self.q_lineEdit_2.text()
        num=self.succounter
        num= num+1
        searchterm = self.q_lineEdit_3.text()
        imgcrawl.imgresize(file_name=searchterm,upper_path=upper_path,model=model,num=num)
        self.a_lineEdit.setText("이미지를 리사이징")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())

