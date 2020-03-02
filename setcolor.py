from tkinter import *
from tkinter.colorchooser import askcolor


def setBgcolor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(triple, hexstr)
        push.config(bg=hexstr)


root = Tk()
push = Button(root, text='设置背景色', command=setBgcolor)
push.config(height=3, font=('courier', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()
