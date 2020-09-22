import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
pdf=wi(filename='C:/Users/Administrator/Desktop/taobao/a/-l.pdf',resolution=300)
pdfImg = pdf.convert('jpeg')
imgBlobs =[]

for img in pdfImg.sequence:
    page =wi(image= img)
    imgBlobs.append(page.make_blob('jpeg'))

extracted_text =[]

for imgBlob in imgBlobs:
    im = image.open(io.BytesIO(imgBlob))
    text= pytesseract.image_to_string(im, lang='eng')
    extracted_text.append(text)

print(extracted_text[0])