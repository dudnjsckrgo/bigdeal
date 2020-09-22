# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:21:32 2019

@author: yyw
"""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from excel import Excel
import geopandas as gpd
import geoplot as gplt

from IPython.display import display
from sklearn.cluster import KMeans
class Plot:
    def init(self):
        self.excel=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homepluscenter.xlsx'
        self.excel.get_execel(path)
        self.excel.get_sheet('Sheet1')
        
        self.excel1=Excel()
        path='C:/Users/yyw/Desktop/study/환시스/homeplus.xlsx'
        self.excel1.get_execel(path)
        self.excel1.get_sheet('Sheet1')
        
        self.y=1
        self.y1=1
        self.df = pd.DataFrame(columns=('latitude','longitude'))
        self.df1 = pd.DataFrame(columns=('latitude','longitude'))
        self.n=0
        self.n1=0
    def dataset2(self):    
        self.excel1.get_G_excel_data(self.y1)
        self.excel1.get_A_excel_data(self.y1)
        self.x1=[]
        self.x1=self.excel1.str_g.split(',')
        
        self.df1.loc[self.n1]=[float(self.x1[0]),float(self.x1[1])]
        self.n1+=1
        self.y1+=1    
    def dataset(self):    
        self.excel.get_G_excel_data(self.y)
        self.excel.get_A_excel_data(self.y)
        self.x=[]
        # Change the line plot below to a scatter plot
        self.x=self.excel.str_g.split(',')
        
        self.df.loc[self.n]=[float(self.x[0]),float(self.x[1])]
        self.n+=1
        self.y+=1    
        
        #print(self.excel.str_g.split(','))
      
        
        
    def scatterplot(self):
        sns.lmplot('latitude','longitude',data=self.df, fit_reg=False, scatter_kws={'s':10})
        sns.lmplot('latitude','longitude',data=self.df1, fit_reg=False, scatter_kws={'s':10},hue="cluster_id")
        plt.title('kmean plot')
        plt.xlabel('latitude')
        plt.ylabel('longitude')
        self.df1.to_excel('/Users/yyw/Desktop/study/환시스/resulthomeplus.xlsx',sheet_name='Sheet1')
        #tick_val = ['1k','10k','100k']
        #tick_lab = ['1k','10k','100k']
        #plt.xticks(tick_val,tick_lab)
        # Put the x-axis on a logarithmic scale
        #plt.xscale('log')
        # Show plot
        
    def show(self):
        plt.show()
    def dataframe(self): 
        # 1. Create Pandas Dataframe
        #print(self.z,self.v)
        # Take a 2D array as input to your DataFrame 
      
        
        display(self.df)
    def dfconverttoarray(self):
        self.centroid_points=self.df.values
        self.data_points=self.df1.values
       
    def clustering(self):
        self.centroids= KMeans(n_clusters=5, init=self.centroid_points, n_init=1)
        self.centroids.fit(self.data_points)
        self.centroids.labels_
        
        self.df1['cluster_id']=self.centroids.labels_
        
if __name__=="__main__":
    plot= Plot()
    plot.init()
    n=1
    while n<400:
        try:
            plot.dataset2()
            n+=1
             
        except:
            plot.y1+=1
            n+=1
    n=1        
    while n<400:
        try:
            plot.dataset()
            n+=1
             
        except:
            plot.y+=1
            n+=1        
    plot.dataframe()
    plot.dfconverttoarray()
    plot.clustering()
    plot.scatterplot()
    
    