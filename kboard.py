import keyboard

def shortcut():
    print('start overlay')

def start_hotkey():
    keyboard.add_hotkey('alt + /', shortcut)
    keyboard.wait('esc')