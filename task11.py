from PIL import Image
from pytesseract import image_to_string
image = Image.open('hh.png')
text=image_to_string(image, lang='eng')
print(text)