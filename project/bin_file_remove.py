# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:04:18 2019

@author: Administrator
"""
from excel import Excel
from os import path
import shutil
if __name__ == "__main__":
    excel = Excel()
    exel_path ='/Users/Administrator/Desktop/sky/온라인판매20190726(2).xlsx'
    upper_path="C:/Users/Administrator/Desktop/ugot/a/m/"
    excel.get_execel(exel_path)
    excel.get_sheet("Sheet1")

    for i in range(6,190):
        excel.get_A_excel_data(i)
        excel.get_E_excel_data(i)
        excel.get_B_excel_data(i)
        
        item_name='['+excel.str_a+']'+excel.str_b
        price=excel.str_e
        stock='99'
        address="C:/Users/Administrator/Desktop/ugot/a/m/"+item_name
        tumb_img=item_name+"_1.jpg"
        brand_name=excel.str_a
        model_name=excel.str_b
        
        
        file=address+'/'+tumb_img
        #path.abspath(file)
        if not path.exists(file):
            shutil.rmtree(path.dirname(file),ignore_errors=True)