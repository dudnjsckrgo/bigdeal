from PIL import Image
import pytesseract
import os
import cv2

#실행 이미지 설정
path= 'C:/Users/Administrator/Desktop/taobao/a/131.jpg'
#실행 언어 설정
lang1= 'chi_sim'

img= cv2.imread(path)
tex = pytesseract.image_to_string(Image.open(path),lang=lang1)
print(pytesseract.image_to_string(Image.open(path),lang=lang1))
cv2.namedWindow("Input image")
cv2.imshow("input image",img)
cv2.waitKey(0)
cv2.destroyWindow("Test")
cv2.destroyWindow("Main")
      
