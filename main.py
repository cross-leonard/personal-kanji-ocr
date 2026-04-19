import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

import pyperclip
from manga_ocr import MangaOcr
from sct import screenshot
from box_selector import BoxSelector
import tkinter as tk
from PIL import Image
import keyboard


def select_box() -> tuple[int, int, int, int] | None:
        root = tk.Tk()
        root.title("Draw Selection Box")
        root.attributes("-fullscreen", True)
        root.attributes("-alpha", 0.25)
        root.configure(bg="black")

        selector = BoxSelector(root)
        root.mainloop()

        if selector.cancelled:
            return None

        x1, y1, x2, y2 = selector.get_box()
        if x1 == x2 or y1 == y2:
            return None

        return (x1, y1, x2, y2)


mocr = MangaOcr()

def main():

    box = select_box()
    screenshot_path = screenshot(box)
    img = Image.open(screenshot_path)
    text = mocr(img)

    pyperclip.copy(text)
    print(text)


keyboard.add_hotkey('alt+/', main)
keyboard.wait()



