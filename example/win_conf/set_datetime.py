# -*- coding: cp950 -*-
'''
變更系統時間
'''

import win32com.client
oShell = win32com.client.Dispatch("WScript.Shell")
oShell.Run("%comspec% /c  date 2008.12.29")
oShell.Run("%comspec% /c  time 12:00:00")
