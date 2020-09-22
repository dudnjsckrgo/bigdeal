# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 23:14:44 2019

@author: Administrator
"""

import imgcrawl
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

CalUI='./_uiFiles/main.ui'
class ExWindow(QMainWindow):
 
    def __init__(self):
        super().__init__()
        uic.loadUi(CalUI,self)
        
 
        self.init_ui()
    def init_ui(self):
        self.statusBar()
        self.statusBar().showMessage('이미지 크롤링,이미지를 pdf로 변환,pdf 병합.')
        
        menu = self.menuBar()               #메뉴바 생성
        menu_file = menu.addMenu('file')    #그룹생성
        menu_edit = menu.addMenu('edit')    #그룹생성
        
        file_exit = QAction('EXit',self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 빠이빠이")
        new_txt = QAction('텍스트 파일',self)
        new_py = QAction("파이썬 파일",self)
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        
        file_new= QMenu('New',self)
        
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit) #메뉴 등록
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())

