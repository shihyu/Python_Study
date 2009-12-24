#-*- encoding:UTF-8 -*-
'''
用python寫的查詢ascii的小工具，按下鍵盤上的按鍵，可以將對應的八進制、十六進制、十進制用顏色標出來。

'''

import wx
import wx.grid

data = [ "nul", "soh", "stx", "etx", "eot", "enq", "ack", "bel",  "bs",  "ht",  "nl",  "vt","ff",  "er",  "so",  "si", "dle", "dc1", "dc2", "dc3", 
         "dc4", "nak", "syn", "etb", "can",  "em", "sub", "esc",  "fs",  "gs", 
          "re",  "us",  "sp",                                                  
           "!",  "\"",  "\#",   "$",   "%",   "&", "`",   "(",   ")",   "*", 
           "+",   ",",   "-",   ".",   "/",                                   
             0,    1,   2,     3,     4,    5,     6,     7,     8,     9, 
           ":",   ";", "<",   "=",   ">",   "?",   "@",                      
           "A",   "B",   "C",   "D",   "E",   "F",   "G",   "H",   "I",   "J", 
           "K",   "L",   "M",   "N",   "O",   "P",   "Q",   "R",   "S",   "T", 
           "U",   "V",   "W",   "X",   "Y",   "Z",                             
           "[",  "\\",   "]",   "^",   "_",  "'",                             
           "a",   "b",   "c",   "d",   "e",   "f",   "g",   "h",   "i",   "j", 
           "k",   "l",   "m",   "n",   "o",   "p",   "q",   "r",   "s",   "t", 
           "u",   "v",   "w",   "x",   "y",   "z",                             
           "{",   "|",   "}",   "~", "del"]
           
data2 = []
for i in xrange(32):
    data2.append([oct(i),         hex(i),        i,        data[i], 
                           oct(i + 32), hex(i + 32), i + 32, data[i + 32],
                           oct(i + 64), hex(i + 64), i + 64, data[i + 64],
                           oct(i + 96), hex(i + 96), i + 96, data[i + 96]])
     

colLabels = ["八進制", "十六進制", "十進制", "字符"] * 4

#這是wxpython in action上的例子，用來創建表格
class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels

    def GetNumberRows(self):
        print 'GetNumberRows', len(self.data)
        return len(self.data)

    def GetNumberCols(self):
        return len(self.colLabels)

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]

    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass

        
class ASCII(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "ASCII Grid",
                size=(803, 725))
        self.grid = grid = wx.grid.Grid(self)
        tableBase = GenericTable(data2, rowLabels=None, colLabels=colLabels)
        grid.SetTable(tableBase)
        grid.SetRowLabelSize(0)
        grid.AutoSize()
        self.old_row = 0
        self.old_col = 0
        grid.Bind(wx.EVT_CHAR, self.on_keydown,)

#清除按過的按鍵顏色
    def clear_oldkey(self):
        print 'clear_oldkey'
        for i in xrange(4):
            self.grid.SetCellBackgroundColour(self.old_row , self.old_col + i, (255,255,255,255))
            self.grid.SetCellTextColour(self.old_row , self.old_col + i, (0,0,0,255))
        self.grid.ForceRefresh()

#處理按鍵按下的事件，將對應的字段用顏色標出來        
    def on_keydown(self, event):
        self.clear_oldkey()
        key = event.GetKeyCode()
        print 'key=', key
        self.row = key % 32
        self.col = key /32 * 4
        for i in xrange(4):
            self.grid.SetCellBackgroundColour(self.row, self.col + i, 'black')
            self.grid.SetCellTextColour(self.row, self.col + i, 'green')
        self.old_row , self.old_col = self.row, self.col
        self.grid.ForceRefresh()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ASCII(None)
    frame.Show(True)
    app.MainLoop()
