# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:43:56 2019

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
df = pd.DataFrame(columns=('x','y'))
df.loc[0]=[7,1]
display(df)