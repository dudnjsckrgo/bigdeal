# -*- coding: utf-8 -*-
from PIL import Image

from googletrans import Translator
import pytesseract

import os

import cv2

import  imutils
path= 'C:/Users/yyw/Downloads/taobao/a/TB24c7ls_lYBeNjSszcXXbwhFXa_!!2871484755.jpg'
img = cv2.imread(path)
mask = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)[1][:,:,0]

dst = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)

cv2.imshow("input image",dst)
cv2.waitKey(0)