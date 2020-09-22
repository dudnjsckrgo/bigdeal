# -*- coding: utf-8 -*-
from PIL import Image

import pytesseract

import os

import cv2

import  imutils
 

#실행 이미지 설정

path= 'D:/python/1.jpg'

#실행 언어 설정

lang1= 'chi_sim'



# Read the image file
image = cv2.imread(path)

# Resize the image - change width to 500
image = imutils.resize(image, width=500)

# Display the original image
cv2.imshow("Original Image", image)

# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1 - Grayscale Conversion", gray)


# Noise removal with iterative bilateral filter(removes noise while preserving edges)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2 - Bilateral Filter", gray)


# Find Edges of the grayscale image
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("4 - Canny Edges", edged)




tex = pytesseract.image_to_string(Image.open(edged),lang=lang1)

print(tex)

cv2.namedWindow("Input image")

cv2.imshow("input image",img)

cv2.waitKey(0)

cv2.destroyWindow("Test")

cv2.destroyWindow("Main")