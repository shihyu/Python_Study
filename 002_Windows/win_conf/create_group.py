# -*- coding: cp950 -*-
'''
�إ� Windows �s��
'''

import win32com.client
def createGroup(computer_name, group_name):
    group = win32com.client.GetObject("WinNT://%s" % computer_name).Create("GROUP", group_name)
    group.SetInfo()

    
createGroup('CWC-FAMILY', 'xxyy')
print 'ok'        
