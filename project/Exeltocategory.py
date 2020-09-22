# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:48:23 2019

@author: Administrator
"""
from excel import Excel
from smartstore import Naver, Itemscout
import os
if __name__ == "__main__":
    excel = Excel()
    excel_path ='/Users/Administrator/Desktop/sky/온라인판매20190726(2).xlsx'
    upper_path="C:/Users/Administrator/Desktop/ugot/a/m/"
    sheet='Sheet1'
    excel.get_execel(excel_path)
    excel.get_sheet(sheet)
    item = Itemscout()
    
    for i in range(11,190):
        excel.get_A_excel_data(i)
        
        excel.get_B_excel_data(i)
        
        item_name='['+excel.str_a+']'+excel.str_b
        address="C:/Users/Administrator/Desktop/ugot/a/m/"+item_name
        tumb_img=item_name+"_1.jpg"      
        file=address+'/'+tumb_img
        
        if not os.path.exists(file):
            continue
        
        if '64AUDIO'==excel.str_a:
            excel.str_a="64오디오"
        elif 'audiotechnica' == excel.str_a:
            excel.str_a='오디오테크니카'
        elif 'AUKEY' == excel.str_a:
            excel.str_a='아오키'   
        elif 'BeyerDynamic' == excel.str_a:
            excel.str_a='베이어다이나믹'
        elif 'ETYMOTIC' == excel.str_a:
            excel.str_a='에티모틱'
        elif 'KAISTER' == excel.str_a:
            excel.str_a='카이스터'   
        elif 'SENNHEISER' == excel.str_a:
            excel.str_a='젠하이저'   
        elif 'ULTRASONE' == excel.str_a:
            excel.str_a='울트라손'   
        else:
            pass
        item_name='['+excel.str_a+'] '+excel.str_b
        
        
        stock='99'
        address="C:/Users/Administrator/Desktop/ugot/a/m/"+item_name
        tumb_img=item_name+"_1.jpg"
        brand_name=excel.str_a
        model_name=excel.str_b
        
         
        file=address+'/'+tumb_img
        
        if os.path.exists(file):
            continue
        
        item.get_excel_position(excel_path,sheet,i,11)
        item.get_item_name(item_name)
        item.get_category()
        category=item.return_category()
        excel.edit_excel_data(i,10,category)
        excel.save_excel_data()
        
