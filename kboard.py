import keyboard


def run_ocr():
    print('running ocr \n')

while True:
    event = keyboard.read_event()
    keyboard.add_hotkey('alt+/', run_ocr)