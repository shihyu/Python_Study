# -*- coding: cp950 -*-
'''
WMI 取得音效卡資訊
'''

import win32com.client
ret = win32com.client.GetObject("winmgmts:").ExecQuery("Select * from Win32_SoundDevice")
for v in ret:
	print v.SystemName
	print v.Manufacturer
	print v.ProductName
