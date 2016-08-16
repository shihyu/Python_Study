# -*- coding: cp950 -*-
'''
快速建立 1GB 檔案
'''
import win32file

h = win32file.CreateFile(r'd:\\a.g', win32file.GENERIC_WRITE, 0, None, win32file.CREATE_ALWAYS,0x80,0)
win32file.SetFilePointer(h, 1024000000-1, win32file.FILE_BEGIN)
win32file.WriteFile(h, chr(0), None)
win32file.CloseHandle(h)
