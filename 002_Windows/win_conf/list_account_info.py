# -*- coding: cp950 -*-
'''
List Windows Account Infomation

REF:
http://gallery.technet.microsoft.com/scriptcenter/zh-tw/40e0cbbb-42ca-435c-b3e6-90d42ca4a1bb
'''
import win32com.client

domain = 'PCEB-A10-026501'
user = 'Administrator'
User = win32com.client.GetObject(u'WinNT://%s/%s' % (domain, user))
print "Name: %s " % User.Name
print "FullName: %s " % User.FullName
print "Description: %s" % User.Description
print "Is Lock: %s" % User.IsAccountLocked 
print "Group Member: "
for prop in User.groups:
    print prop.Name

# unlock
#User.IsAccountLocked  = 0
#User.SetInfo()

# set password
#User.SetPassword('123')

# 強制更換密碼
#User.passwordexpired = 1 
#User.SetInfo 

