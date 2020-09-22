# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:48:35 2019

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import *
 
class ExWindow(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.init_ui()
     
 
    def init_ui(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Main Window')
        self.lineEdit = QLineEdit(self)
        self.pushButton = QPushButton(self)
        self.pushButton.move(0,100)
        self.show()
        
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())

