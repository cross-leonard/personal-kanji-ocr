from tkinter import *
from tkinter import ttk

start_pt = None
end_pt = None

def click(event):
    global start_pt
    start_pt = (event.x, event.y)

def release(event):
    global end_pt
    end_pt (event.x, event.y)

# setup window
root = Tk()
root.resizable(False, False)
root.attributes(fullscreen=True)
root.attributes(alpha=0.01)

# window action listeners
start_pt = root.bind("<Button-1>", click)
end_pt = root.bind("<ButtonRelease>", release)
root.bind("<B1-Motion>")


print(start_pt, end_pt)

root.mainloop()


