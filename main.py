import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

a = Image.open('C:\\Users\\User\\Pictures\\영수증2.png')
result = pytesseract.image_to_string(a, lang='kor+eng')

print(type(result))
print(result)