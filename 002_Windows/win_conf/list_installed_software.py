# -*- coding: cp950 -*-
'''
List All Installed Software

REF:
http://gallery.technet.microsoft.com/scriptcenter/zh-tw/8035d5a9-dc92-436d-a60c-67d381da15a3
'''
import _winreg

strEntry1a = "DisplayName" 
strEntry1b = "QuietDisplayName" 
strEntry2 = "InstallDate" 
strEntry3 = "VersionMajor" 
strEntry4 = "VersionMinor" 
strEntry5 = "EstimatedSize"
strEntry5 = "UninstallString"  # 反安裝

root = _winreg.HKEY_LOCAL_MACHINE
key = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
subkey = _winreg.OpenKey(root, key)


idx = 0
soft_guid = []
while True:
    try:
        kn = _winreg.EnumKey(subkey, idx)
        soft_guid.append( kn )        
        idx += 1
    except WindowsError as e:
        print e
        break
_winreg.CloseKey(subkey)

for soft in soft_guid:
    try:
        key2 =  "%s\\%s" % (key, soft)
        #print key2
        subkey2 = _winreg.OpenKey(root, key2)        
        name,_ = _winreg.QueryValueEx(subkey2, strEntry1a)
        print 'Display Name: %s' %name
        print 
        _winreg.CloseKey(subkey2)
    except WindowsError:
        pass
