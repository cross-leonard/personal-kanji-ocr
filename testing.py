from manga_ocr import MangaOcr
import pyperclip
from PIL import Image

mocr = MangaOcr()
img = Image.open("kanji.png")  # open the image file
text = mocr(img)

pyperclip.copy(text)
print(text)