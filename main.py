import cv2
import pyperclip
from PIL import Image
from manga_ocr import MangaOcr
from mss import mss, tools
import sct
import tkinter




mocr = MangaOcr()
sct.sct()
text = mocr("screenshot.png")



pyperclip.copy(text)
print(text)


