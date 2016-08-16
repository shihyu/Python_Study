# -*- coding: cp950 -*-
'''
建立 Windows 群組
'''

import win32com.client
def createGroup(computer_name, group_name):
    group = win32com.client.GetObject("WinNT://%s" % computer_name).Create("GROUP", group_name)
    group.SetInfo()

    
createGroup('CWC-FAMILY', 'xxyy')
print 'ok'        
