# -*- coding : UTF-8 -*-
__author__ = 'admin'

from tkinter import *

root = Tk()

root.title('Buttons')
f = Frame(root, width=300, height=110)
xf = Frame(f, relief=GROOVE, borderwidth=2)
Label(xf, text="You shot him!").pack(pady=10)
Button(xf, text="He's dead!", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(xf, text="He's completely dead!", command=root.quit).pack(side=RIGHT,
                                                                 padx=5, pady=8)
#可将anchor看作是原点的位置
xf.place(relx=0.1, rely=0.125, anchor=NW)
Label(f, text='Self-defence against fruit').place(relx=0.06, rely=0.125,
                                                  anchor=W)
f.pack()
root.mainloop()