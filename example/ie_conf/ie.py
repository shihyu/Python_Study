# -*- coding: cp950 -*-
"""
Description: 讀取IE 組態資訊

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import _winreg

def showProxySetting():
    # Proxy Server 設定
    key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")

    proxy_server = ''
    try:
        proxy_server =_winreg.QueryValueEx(key, "ProxyServer")[0]
    except:
        pass
    
    proxy_override = 'N'
    try:
        proxy_override = _winreg.QueryValueEx(key, "ProxyOverride")[0]
        if proxy_override == '<local>':
            proxy_override = 'Y'
    except:
        pass

    proxy_enable = 'N'
    try:
        proxy_enable = _winreg.QueryValueEx(key, "ProxyEnable")[0]
        if proxy_enable == 1:
            proxy_enable = 'Y'
    except:
        pass

    print '啟動 Proxy: %s' % proxy_enable
    print 'Proxy Server: %s' % proxy_server
    print '近端網址不使用 Proxy: %s' % proxy_override

def setProxy(server, local_enable = None):
    key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")
    _winreg.SetValueEx(key, 'ProxyEnable', 0, _winreg.REG_DWORD, 1)
    if local_enable == True:        
        _winreg.SetValueEx(key, "ProxyOverride", 0, _winreg.REG_SZ, '<local>')
    else:
        try:
            winreg.DeleteKey(key, "ProxyOverride")
        except:
            pass
    _winreg.SetValueEx(key, "ProxyServer", 0, _winreg.REG_SZ, server)
        
if __name__ == '__main__':
    setProxy('www.hinet.net', True)
    showProxySetting()
