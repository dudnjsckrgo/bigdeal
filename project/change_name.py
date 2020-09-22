# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:59:29 2019

@author: Administrator
"""
from excel import Excel
from multiupdate import Change
if __name__ == "__main__":
    change=Change()
    excel = Excel()
    exel_path ='/Users/Administrator/Desktop/sky/온라인판매20190726(2).xlsx'
    upper_path="C:/Users/Administrator/Desktop/ugot/a/m/"
    excel.get_execel(exel_path)
    
    excel.get_sheet("Sheet1")    
    for i in range(6,189):
        excel.get_A_excel_data(i)
    
        change.get_name(excel.str_a)
        change.change_name()
        excel.edit_excel_data(i,13,change.str_name)
        excel.save_excel_data()
