import keyboard 



def shortcut():
    print('start overlay')
keyboard.add_hotkey('alt + /', shortcut)

keyboard.wait('esc')