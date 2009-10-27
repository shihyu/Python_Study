# -*- coding: utf-8 -*-
"""
Description: 攔截目前滑鼠座標

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""


__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import threading
import win32gui
from Tkinter import *
#win = Toplevel()
win = Tk()
win.title(string="滑鼠座標")
win.wm_attributes("-topmost", 1)
x,y=win32gui.GetCursorPos()
lbl = Label(win, text=("%d,%d"%(x,y)))
lbl.pack()


def update_pos():    
    x,y=win32gui.GetCursorPos()   
    lbl.config(text=("%d,%d"%(x,y)))
    win.after(100, update_pos)

update_pos()

win.mainloop()


