# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:19:23 2019

@author: Administrator
"""
from smartstore import Itemscout
path="C:/Users/Administrator/Desktop/ugot/a/d/Book1.xlsx"
sheet='Sheet1'
item=Itemscout()
while True:
    item.find_item_source_first_step_into_page()
    item.find_item_source_second_step_category_1()
    item.find_item_source_second_step_category_2()
    item.find_item_source_second_step_category_3()
    item.find_item_source_third_step_get_data()
    item.find_item_source_fourth_step_edit_excel(path,sheet)
