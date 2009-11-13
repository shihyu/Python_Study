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
    state = data['state']
    state = not state
    data['state'] = state
    if state:
        windll.user32.SetWindowPos(h, -1,0,0,0,0,3)
    else:
        windll.user32.SetWindowPos(h, -2,0,0,0,0,3)

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
