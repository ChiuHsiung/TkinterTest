# -*- coding : UTF-8 -*-
__author__ = 'admin'

from tkinter import *

root = Tk()
Label(root, text = "This is LABEL 1").pack(padx=10, pady=10)
t1 = Toplevel(root)
Label(t1, text = "This is LABEL 2").pack(padx=10, pady=10)
t2 = Toplevel(root)
Label(t2, text = "This is LABEL 3").pack(padx=10, pady=10)
t2.transient(root)
t3 = Toplevel(root, borderwidth=5, bg="blue")
Label(t3, text = "This is LABEL 4", bg="red", fg="white").pack(padx=10, pady=10)
t3.overrideredirect(1)
t3.geometry("700x150+600+150")

root.mainloop()


