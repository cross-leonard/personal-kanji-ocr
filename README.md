# Manga OCR Screen Reader

## Description
A desktop tool that lets you select any region of your screen, 
extracts Japanese text from it using OCR, and copies the result 
to your clipboard. Useful for reading manga or any Japanese text 
on screen without switching apps.

## Demo
<img width="1349" height="779" alt="kanji_ocr_gif" src="https://github.com/user-attachments/assets/9fbdf156-b476-4e56-913c-03cbca056fe2" />


## How It Works
1. A fullscreen transparent overlay appears
2. Click and drag to draw a box around the Japanese text
3. Press Enter to confirm the selection
4. The text is extracted and copied to your clipboard automatically
5. Press Escape to cancel at any time

## Installation
pip install manga-ocr pyperclip mss

## How to Run
python main.py

## Technologies Used
- Python
- manga-ocr (Japanese OCR model)
- Tkinter (GUI overlay)
- mss (screen capture)
- pyperclip (clipboard access)
- keyboard (key event handling)
- ctypes (Windows API for DPI awareness)

## Author
Cross Leonard
