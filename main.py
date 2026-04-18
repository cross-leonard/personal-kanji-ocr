import pyperclip
from manga_ocr import MangaOcr
import sct
from clearboxfeature import select_box




mocr = MangaOcr()
box = select_box()

if box is None:
	print("No selection made.")
	raise SystemExit(0)

screenshot_path = sct.sct(box)
text = mocr(screenshot_path)



pyperclip.copy(text)
print(text)


