from PIL import Image
import pytesseract
import cv2
img= cv2.imread('C:/Users/Administrator/Desktop/taobao/a/102.jpg')
tex = pytesseract.image_to_string(Image.open('C:/Users/Administrator/Desktop/taobao/a/131.jpg'),lang='chi_sim')
print(pytesseract.image_to_string(Image.open('C:/Users/Administrator/Desktop/taobao/a/131.jpg'),lang='chi_sim'))
cv2.namedWindow("Input image")
cv2.imshow("input image",img)
cv2.waitKey(0)
cv2.destroyWindow("Test")
cv2.destroyWindow("Main")
      
