# -*- coding: cp950 -*-
'''
字型資訊
'''

import _winreg
root = _winreg.HKEY_LOCAL_MACHINE
key = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts'
subkey = _winreg.OpenKey(root, key)

idx = 0
while True:
    try:
        kn, ttf, _ = _winreg.EnumValue(subkey, idx)
        print '%s = %s' % (str(ttf), str(kn))
        idx += 1
    except WindowsError as e:
        break
