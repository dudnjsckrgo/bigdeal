 # -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:03:40 2019

@author: yyw

"""
from excel import Excel
class Plot:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homepluscenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.y=1
        self.total=0
        self.i=0
    def dataset(self):
        self.excel.get_I_excel_data(self.y)
        
        print(self.excel.str_i[:-2])
        self.excel.edit_excel_data(self.i+1,9,self.excel.str_i[:-2])
        self.i+=1
        self.excel.save_excel_data()
        '''
        self.excel.get_L_excel_data(self.y)
        if self.excel.str_j=='PVC(Polyvinyl Chloride)':
            self.total+=self.excel.str_l
        '''
        self.y+=1    
    def dataset1(self):
        self.excel.get_I_excel_data(self.y)
        self.excel.get_L_excel_data(self.y)
        if self.excel.str_j=='PVC(Polyvinyl Chloride)':
            self.total+=self.excel.str_l
        self.y+=1
    def SUM(self):
        self.excel.get_A_excel_data(self.y)
        self.total+=self.excel.str_a
        print(self.total)
        self.y+=1
    def show(self):
        print(self.total)
if __name__=="__main__":
    plot=Plot()
    plot.init()
    
    while True:
        try:    
            plot.dataset()
        except:
            plot.i+=1
            plot.y+=1
    
        