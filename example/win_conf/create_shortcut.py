# -*- coding: cp950 -*-
'''
建立捷徑
'''
import win32com.client

wsh = win32com.client.Dispatch('WScript.Shell')
lnk = wsh.CreateShortCut(r'c:\\a.lnk')
lnk.TargetPath  = r'c:\windows\wmprfCHT.prx'
lnk.WorkingDirectory  = r'c:\windows'
lnk.Description = '記事本'
lnk.WindowStyle  = 4
lnk.TargetPath  = r'c:\windows\notepad.exe'
lnk.IconLocation = r'c:\windows\notepad.exe,0'
lnk.Save()
