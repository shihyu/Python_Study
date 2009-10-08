#-*- coding: UTF-8 -*-
from win32api import *
import win32gui
from ctypes import *

def open_file_with_app(fn):
    ShellExecute(0, None, fn, None, "c:\\", True)

def win_top(title, e):
    """
    視窗設定為上層顯示
    """

    h=win32gui.FindWindow(None, title)
    if h==0:
        return
    if(e == True):
        windll.user32.SetWindowPos(h, -1,0,0,0,0,3)
    else:
        windll.user32.SetWindowPos(h, -2,0,0,0,0,3)
        
def win_size(title, w,h):
    """
    變更視窗的寬/高
    """
    handle=win32gui.FindWindow(None, title)
    if handle==0:
        return
    
    windll.user32.SetWindowPos(handle, 0, 0,0, w,h, 2)
    
def win_show(title, enable):
    """
    顯示/隱藏視窗
    """
    handle=win32gui.FindWindow(None, title)
    if handle==0:
        return
    
    if enable == True:
        windll.user32.SetWindowPos(handle, 0,0,0,0,0, 0x43)
    else:
        windll.user32.SetWindowPos(handle, 0,0,0,0,0,0x83)        


def win_list():
    """
    Windows 列表
    """
    def win_enum_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            results.append(hwnd)

    handles = []
    win32gui.EnumWindows(win_enum_callback, handles)
    print '\n'.join(['%d\t%s' % (h, win32gui.GetWindowText(h)) for h in handles])

def proc_list():
    """
    Process 列表
    """
    import win32pdh
    processinfo,processes=win32pdh.EnumObjectItems(None,None,"Process",-1)
    print "\n".join(processes)





