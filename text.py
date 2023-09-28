import pytesseract as pt

pt.pytesseract.tesseract_cmd = r"D:\Tesserract\tesseract.exe"
from PIL import Image

# import cv2

img = Image.open("test6.jpg")
text = pt.image_to_string(img)

# pt.pytesseract.tesseract_cmd = "D:\\Tesserract\\tesseract.exe"

# text = pt.image_to_string(img)

print(text)
