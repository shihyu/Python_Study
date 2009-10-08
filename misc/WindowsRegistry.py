#!/usr/bin/env python
"""
Description: A wrapper class to provide dict-like access for Windows registry.

This class works like a normal dict object. However, the key is a 
path which splitted by backslash. This path is used to point to the location
of registry. It should be started from one of the following root key.

    'HKEY_LOCAL_MACHINE'
    'HKEY_CLASSES_ROOT' 
    'HKEY_CURRENT_USER'
    'HKEY_USERS'
    'HKEY_CURRENT_CONFIG'
    'HKEY_PERFORMANCE_DATA'
    'HKEY_DYN_DATA'

For example, if you like to execute a program when window start:

    reg = WindowsRegistry()
    reg[r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\MyProgram'] = (ur'c:\Program Files\MyFolder\MyProgram.exe', _winreg.REG_SZ)
    print reg[r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\MyProgram']
    
If you like to delete it from registry, use:

    del reg[r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\MyProgram']
    
When reading data from registry and the last character in path is a backslash, it 
return the content of the specified subkey. For example, if you like to know what program
will be executed when Windows start, you can use

    print reg[r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\\']

Author: Gary W. Lee <garywlee@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""
import UserDict
import re
import _winreg

class WindowsRegistry(UserDict.DictMixin):
    """
    A wrapper class for Win32 registry.
    """
    def __init__(self):
        """Constructor."""
        self._curPath = None
        self._curKey = None
        self._rootKey = _winreg.HKEY_LOCAL_MACHINE
        self._reRedundantBackslash = re.compile(r'\\+')
        
    def __del__(self):
        """Destructor."""
        self.CloseKey()
        
    def CloseKey(self):
        """Close Key"""
        if not self._curKey:
            _winreg.CloseKey(self._curKey)
            self._curKey = None
            self._curPath = None
        
    def GetRootKey(self, path):
        """Convert the string to its root Key."""
        path = path.upper()
        rootKeys = (
            'HKEY_LOCAL_MACHINE', 
            'HKEY_CLASSES_ROOT', 
            'HKEY_CURRENT_USER', 
            'HKEY_USERS', 
            'HKEY_CURRENT_CONFIG', 
            'HKEY_PERFORMANCE_DATA', 
            'HKEY_DYN_DATA')
        
        if path not in rootKeys:
            return None
        return _winreg.__getattribute__(path)

    def NormalizePath(self, path):
        """ """
        normalPath = self._reRedundantBackslash.sub(r'\\', path)
        if normalPath.startswith('\\'):
            normalPath = path[1:]
        return normalPath
        
    def SplitPath(self, path):
        return self.NormalizePath(path).split('\\')
        
    def OpenKey(self, items):
        """Open Specified Key"""
        idx = 0
        key = self.GetRootKey(items[idx])
        if key:
            self._rootKey = key
            idx += 1

        key = _winreg.CreateKey(self._rootKey, items[idx])
        idx += 1
        for i in items[idx:]:
            tmp = key
            key = _winreg.CreateKey(key, i)
            _winreg.CloseKey(tmp)
        self._curKey = key

    def __getitem__(self, path):
        """Get item of registry. The key is the registry path."""
        items = self.SplitPath(path)
        if self._curPath != path:
            self.OpenKey(items[:-1])            
            self._curPath = path
        if len(items[-1]) == 0:
            info = _winreg.QueryInfoKey(self._curKey)
            subkeys = []
            values = []
            for i in xrange(info[0]):
                subkeys.append(_winreg.EnumKey(self._curKey, i))
            for i in xrange(info[1]):
                values.append(_winreg.EnumValue(self._curKey, i))
            return (subkeys, values)                
        return _winreg.QueryValueEx(self._curKey, items[-1])
        
    def __setitem__(self, path, value):
        """Set item of registry. The key is the registry path."""
        items = self.SplitPath(path)
        if self._curPath != path:
            self.OpenKey(items[:-1])            
            self._curPath = path
        _winreg.SetValueEx(self._curKey, items[-1], 0, value[1], value[0])
        
    def __delitem__(self, path):
        """Set item of registry. The key is the registry path."""
        items = self.SplitPath(path)
        if len(items[-1]) == 0:
            self.OpenKey(items[:-2])
            self._curPath = None
            _winreg.DeleteKey(self._curKey, items[-2])
        else:           
            self.OpenKey(items[:-1])            
            self._curPath = path
            _winreg.DeleteValue(self._curKey, items[-1])

# EOF.
