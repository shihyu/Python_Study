# -*- coding: cp950 -*-
# 檢查音效卡
import win32com.client
def check_soundcard():
    mgr = win32com.client.GetObject("winmgmts:")
    mgr.InstancesOf("win32_sounddevice")
    scs = mgr.InstancesOf("win32_sounddevice")
    for sc in scs:
        status = sc.Properties_("Status")
        print "%s/%s" % (sc.Properties_("Name"), status)
        if status == 'OK':
            return True

    return False

if __name__ == '__main__':
    check_soundcard()

