# -*- coding: utf-8 -*-
import cv2
import numpy as np
import  imutils
#from matploylib import pyplot as plt
imgFile1 ='C:/Users/yyw/.spyder-py3/Car_Image_1.jpg'
imgFile2 ='C:/Users/yyw/.spyder-py3/car2.jpg'
img1= cv2.imread(imgFile1);
img2= cv2.imread(imgFile2);
img1= imutils.resize(img1, width=500)
img2= imutils.resize(img2, width=500)
addv = np.vstack((img1,img2))
cv2.imshow('imgv',addv)
cv2.waitKey(0)