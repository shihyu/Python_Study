#-*- coding: UTF-8 -*-
from Tkinter import *
import win32gui
from ctypes import windll

def clear_listbox(lst):
    lst.delete(0, END)

def append(lst, item):
    lst.insert(END, item)

def lst_ondblclick(e):
    idx, = lst.curselection()
    data = handles[int(idx)]
    h = data['data']

    ch = windll.user32.GetSystemMenu(h, 0)
    # 不能改變大小 
    windll.user32.RemoveMenu(ch, 0xF000, 0x0)
    # 視窗不能移動 
    windll.user32.RemoveMenu(ch, 0xF010, 0x0)
    # 不能最小化
    windll.user32.RemoveMenu(ch, 0xF020, 0x0)
    # 不能最大化 
    windll.user32.RemoveMenu(ch, 0xF030, 0x0)
    # Disable X鈕 
    windll.user32.RemoveMenu(ch, 0xF060, 0x0)
    # 關閉垂直捲軸 
    windll.user32.RemoveMenu(ch, 0xF070, 0x0)
    # 關閉水平捲軸 
    windll.user32.RemoveMenu(ch, 0xF080, 0x0)

    # 移除第一個主選單，第一個主項目下的第一個子項目
    mm = windll.user32.GetMenu(h)
    print mm
    sm = windll.user32.GetSubMenu(mm, 0)
    print sm
    mid = windll.user32.GetMenuItemID(sm, 0)
    print mid
    windll.user32.RemoveMenu(sm, mid, 0x0)

def win_enum_callback(hwnd, results):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        results.append({'state': False, 'data':hwnd, 'name': win32gui.GetWindowText(hwnd) })

def btnRefresh_click(e):
    global handles
    clear_listbox(lst)
    handles = []
    fill_win_list()
    
def fill_win_list():    
    win32gui.EnumWindows(win_enum_callback, handles)

    for item in handles:
        append(lst, item['name'].decode('big5') )

if __name__ == '__main__':
    handles = []        
    win = Tk()
    win.title("Top Level Window")
    win.geometry('500x500')
    frame = Frame(win, width=400)

    lst = Listbox(frame)
    fill_win_list()

    lst.bind("<Double-Button-1>", lst_ondblclick)
    lst.pack(expand=1, fill="both", side=LEFT)

    btn = Button(win, text="Refresh")
    btn.bind("<ButtonRelease-1>", btnRefresh_click)
    btn.pack(side=TOP)

    frame.pack(expand=1, fill="both")
    win.mainloop()
