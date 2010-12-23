# -*- coding: cp950 -*-
'''
將 [使用者] 加入 [群組]
注意 : 群組及使用者必須已經存在
'''

import win32com.client

def addToGroup(computer_name, group_name, user_name):    
    win32com.client.GetObject("WinNT://%s/%s,GROUP" % (computer_name, group_name) ).Add( "WinNT://%s/%s,USER" %(computer_name, user_name) )

addToGroup('CWC-FAMILY', 'HelpServicesGroup', 'cwchiu')    
