# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:03:12 2019

@author: Administrator
"""
from excel import Excel
from smartstore import Naver
import os

class Change:
    def get_name(self,str_name):
        self.str_name=str_name
    def change_name(self):

        if '64AUDIO'==self.str_name:
            self.str_name="64오디오"
        elif 'audiotechnica' == self.str_name:
            self.str_name='오디오테크니카'
        elif 'AUKEY' == self.str_name:
            self.str_name='아오키'   
        elif 'BeyerDynamic' == self.str_name:
            self.str_name='베이어다이나믹'
        elif 'ETYMOTIC' == self.str_name:
            self.str_name='에티모틱'
        elif 'KAISTER' == self.str_name:
            self.str_name='카이스터'   
        elif 'SENNHEISER' == self.str_name:
            self.str_name='젠하이저'   
        elif 'ULTRASONE' == self.str_name:
            self.str_name='울트라손'
        
            
if __name__ == "__main__":
    excel = Excel()
    exel_path ='/Users/Administrator/Desktop/sky/온라인판매20190726(2).xlsx'
    upper_path="C:/Users/Administrator/Desktop/ugot/a/m/"
    excel.get_execel(exel_path)
    
    excel.get_sheet("Sheet1")
    change= Change()
    
    smart = Naver()
    for i in range(35,190): #이 부분을 고치시오
        excel.get_A_excel_data(i)
        excel.get_E_excel_data(i)
        excel.get_B_excel_data(i)
        excel.get_M_excel_data(i)
        excel.get_J_excel_data(i)
        
        
        category=excel.str_j
        print("카테고리는 {}입니다.".format(category))
        if None ==category:
            continue
        else:
            item_name='['+excel.str_a+']'+excel.str_b
            
        
            price=excel.str_e
            print('가격은 {}원입니다.'.format(price))
            stock='99'
            address="C:/Users/Administrator/Desktop/ugot/a/m/"+item_name+'/'
            tumb_img=item_name+"_1.jpg"
            brand_name=excel.str_a
            model_name=excel.str_b
    
            
            file=address+'/'+tumb_img
            print(os.path.exists(file))
        if not os.path.exists(file):
            continue  
        else:    
            item_name='['+excel.str_m+'] '+excel.str_b
            print(item_name)
    
            
            
            smart.smartstore()
            smart.get_item_name(item_name)
            smart.get_category(category)
            smart.edit_category()
            
            smart.get_brand_name(brand_name)
            
            smart.get_model_name(model_name)
            smart.edit_item_name()
            
            smart.get_price(price)
            smart.edit_price()
            
            smart.get_stock(stock)
            smart.edit_stock()
            
            smart.get_address_from_img(address)
            smart.get_tumb_img(tumb_img)
            
            smart.edit_tumbnail()
            
            smart.go_detail()
            num=2
            m=1
            address[2:]
            #next(os.walk('/home/mkblog/test'))[2]
            
            file_count=len(next(os.walk(address[2:]))[2])
            while True:
                file=address+'/'+tumb_img[:-5]+str(num)+'.jpg'
                if not os.path.exists(file):
                    if m ==file_count:
                        break
                    num = num+1
                else:
                    if m ==file_count:
                        break
                    else:
                        smart.add_img(num)
                        m+=1
                        num = num+1
            print('나가기')    
            smart.exit_detail()
            
            smart.item_info()
            
            smart.nation_delivery_info()
            smart.nation_return_info()
            smart.AS_info()
            smart.Tag_setting()
            smart.view_info()
            smart.save()
            
            print('{}번째꺼 완료 되었습니다.'.format(i))
 #   nike = Naver()