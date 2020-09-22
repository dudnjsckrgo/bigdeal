# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:39:46 2019

@author: Administrator
"""
from wand.image import Image
filename1="/Users/Administrator/Downloads/tutorial.pdf"

with(Image(filename="/Users/Administrator/Downloads/tutorial.pdf", resolution=120)) as source: 
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        n = i + 1
        newfilename = filename1[:-4] + str(n) + '.jpeg'
        Image(images[i]).save(filename=newfilename)
