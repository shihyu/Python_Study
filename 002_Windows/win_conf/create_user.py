# -*- coding: cp950 -*-
'''
建立 Windows 使用者
'''
import win32com.client
def createUser(computer_name, user_name, password):
    user = win32com.client.GetObject("WinNT://%s" % computer_name).Create("USER", user_name)
    user.SetPassword(password)
    user.SetInfo()
    
createUser('CWC-FAMILY', 'gyui', '1234')
print 'ok'
