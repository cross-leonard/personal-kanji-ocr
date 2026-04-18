import pyperclip
from manga_ocr import MangaOcr
import sct
import box_selector

mocr = MangaOcr()
box = select_box()

screenshot_path = sct.sct(box)
text = mocr(screenshot_path)

pyperclip.copy(text)
print(text)


