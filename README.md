# Manga OCR Screen Reader

## Description
A small Windows tool that lets you draw a box around Japanese text on your screen, runs OCR on that area, copies the result to your clipboard, and shows a notification.

## Demo
<img width="1349" height="779" alt="kanji_ocr_gif" src="https://github.com/user-attachments/assets/9fbdf156-b476-4e56-913c-03cbca056fe2" />

## How It Works
1. Press `Alt + /` to start.
2. A transparent fullscreen overlay appears.
3. Click and drag to draw a box around the text.
4. Press `Enter` to confirm, or `Escape` to cancel.
5. The selected area is captured, OCR runs, and the text is copied to your clipboard.

## Hotkeys
- `Alt + /` start OCR from a screen selection
- `Alt + Q` quit the app

## Installation
Install the Python packages used by the project:

```bash
pip install manga-ocr pyperclip mss pillow keyboard plyer
```

## How to Run
```bash
python main.py
```

## Notes
- This project is intended for Windows.
- `keyboard` and `ctypes` are used for global hotkeys and DPI awareness.

## Technologies Used
- Python
- manga-ocr
- Tkinter
- mss
- pyperclip
- keyboard
- plyer
- ctypes

## Author
Cross Leonard
