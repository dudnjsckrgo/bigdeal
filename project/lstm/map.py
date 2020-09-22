# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:30:58 2019

@author: yyw
"""
from excel import Excel
import folium
def f(x):
    return{0:'blue',1:'red',2:'yellow',3:'green',4:'purple',5:"orange",6:"white",7:"black",8:"gray",9:"brown",10:"blue",11:"green"}[x]
class Plot:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homepluscenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        self.excel1=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/resulthomeplus.xlsx'
        self.excel1.get_execel(path)
        self.excel1.get_sheet('Sheet1')        
        self.y=1
        self.z=[]
        self.v=[]
        self.map_2 = folium.Map(location=[37.509668, 126.887726],zoom_start=7)
        
    def dataset2(self):    
        self.excel1.get_G_excel_data(self.y)
        self.excel1.get_A_excel_data(self.y)
        self.x1=[]
        self.x1=self.excel1.str_g.split(',')
        print(self.excel1.str_g.split(','))
        folium.RegularPolygonMarker([self.x1[0], self.x1[1]],popup='{}'.format(self.excel1.str_a),radius=3).add_to(self.map_2)
        self.y+=1
    def dataset(self):
        self.excel.get_G_excel_data(self.y)
        self.excel.get_A_excel_data(self.y)
        
        # Change the line plot below to a scatter plot
        
        self.x=[]
        self.x=self.excel.str_g.split(',')
        print(self.excel.str_g.split(','))
        folium.Marker([self.x[0], self.x[1]],popup='{}'.format(self.excel.str_a),radius=6).add_to(self.map_2)
        
        #self.z.append(self.x[0])
        #self.v.append(self.x[1])
        self.y+=1
    def datasetresult(self):
        self.excel1.get_B_excel_data(self.y)
        self.excel1.get_C_excel_data(self.y)
        self.excel1.get_D_excel_data(self.y)
         
        folium.RegularPolygonMarker([self.excel1.str_b, self.excel1.str_c],radius=3,color=f(self.excel1.str_d)).add_to(self.map_2)
        self.y+=1
    def show(self):
        
        self.map_2.save('./indexhomeplus.html')
if __name__=="__main__":
    plot=Plot()
    plot.init()
    n=1
    while n<500:
        try:
            plot.datasetresult()
            n+=1
             
        except:
            plot.y+=1
            n+=1    
    n=1 
    plot.y=1       
    while n<500:
        try:
            plot.dataset()
            n+=1
             
        except:
            plot.y+=1
            n+=1        
    print('생성중') 
          
    plot.show()        