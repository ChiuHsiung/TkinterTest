# -*- coding : UTF-8 -*-
__author__ = 'admin'

from tkinter import *

root = Tk()
root.title('Frames')
for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth=2, relief=relief)
    f.pack(side=LEFT, padx=5, pady=5)
    Label(f, text=relief, width=10).pack(side=LEFT)


root.mainloop()
