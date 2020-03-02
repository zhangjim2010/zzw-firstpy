import sys
from tkinter import *

makemodal = (len(sys.argv) > 1)


def dialog():
    win = Toplevel()
    Label(win, text='Dialog custom').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('dialog exit')


root = Tk()
Button(root, text='弹出窗口', command=dialog).pack()
root.mainloop()
