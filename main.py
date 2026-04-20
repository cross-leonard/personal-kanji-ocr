import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

import os
import tkinter as tk

import keyboard
import pyperclip
from PIL import Image
from box_selector import BoxSelector
from manga_ocr import MangaOcr
from notification import send_notification
from sct import screenshot


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
    if box is None:
        return

    screenshot_path = screenshot(box)
    img = Image.open(screenshot_path)
    text = mocr(img)

    pyperclip.copy(text)
    # send_notification("Kanji Detected", "Kanji copied to clipboard")
    print(text)


keyboard.add_hotkey("alt+/", main)
keyboard.add_hotkey("alt+q", lambda: os._exit(0))
keyboard.wait()



