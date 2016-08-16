# -*- coding: cp950 -*-
from ctypes import *

def check_dotnet():
    """
    檢查是否安裝 .NET Fx Functime
    """
    try:
        h = windll.kernel32.LoadLibraryA("mscoree")
        if h == 0:
            return False
                                         
        func_GetCORVersion = windll.kernel32.GetProcAddress(h, "GetCORVersion")
        if func_GetCORVersion == 0:
            return False
        proto = WINFUNCTYPE(None)
        func = proto(func_GetCORVersion)
        print func()
        return True
    finally:
        if not h == 0:
            windll.kernel32.FreeLibrary(h)

                                                                                                                   
print check_dotnet()
