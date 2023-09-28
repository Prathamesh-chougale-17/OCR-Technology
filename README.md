# Hii I am Prathamesh
## This is a text recognition project by OCR using pytesseract

To implement this project, you will need to install tessaract:
 1. You have to install the tesseract-ocr setup from the link given : https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe
 2. Later install it in local computer throught the tesseract installed setup.

 3. After installing the setup you have to install the pytesseract library using the command : 
 ```terminal
 pip install pytesseract
 ```
 1. copy the code present in the file text.py and paste it in your python file. But in pt.pytesseract.tesseract_cmd we have set the path of the tesseract.exe file. So you have to change the path according to your system.mostly the path will be like this : 
```
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
     

 1. After that you could run the code and see the output. Use py [python file name] to run the code. For example: 
```terminal
py test.py
```
