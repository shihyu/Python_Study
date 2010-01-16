# -*- coding: cp950 -*-
"""
Description: 字典檔破解 RAR

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import os
import time
import ctypes.wintypes
import random

# Low level interface - see UnRARDLL\UNRARDLL.TXT
ERAR_END_ARCHIVE = 10
ERAR_NO_MEMORY = 11
ERAR_BAD_DATA = 12
ERAR_BAD_ARCHIVE = 13
ERAR_UNKNOWN_FORMAT = 14
ERAR_EOPEN = 15
ERAR_ECREATE = 16
ERAR_ECLOSE = 17
ERAR_EREAD = 18
ERAR_EWRITE = 19
ERAR_SMALL_BUF = 20
ERAR_UNKNOWN = 21

RAR_OM_LIST = 0
RAR_OM_EXTRACT = 1

RAR_SKIP = 0
RAR_TEST = 1
RAR_EXTRACT = 2

RAR_VOL_ASK = 0
RAR_VOL_NOTIFY = 1

RAR_DLL_VERSION = 3

# enum UNRARCALLBACK_MESSAGES
UCM_CHANGEVOLUME = 0
UCM_PROCESSDATA = 1
UCM_NEEDPASSWORD = 2

unrar = ctypes.WinDLL('unrar.dll')

class RAROpenArchiveData(ctypes.Structure):
    def __init__(self, ArcName=None, OpenMode=RAR_OM_LIST):
        self.CmtBuf = ctypes.c_buffer(64*1024)
        ctypes.Structure.__init__(self, ArcName=ArcName, OpenMode=OpenMode, _CmtBuf=ctypes.addressof(self.CmtBuf), CmtBufSize=ctypes.sizeof(self.CmtBuf))

    _fields_ = [
                ('ArcName', ctypes.c_char_p),
                ('OpenMode', ctypes.c_uint),
                ('OpenResult', ctypes.c_uint),
                ('_CmtBuf', ctypes.c_voidp),
                ('CmtBufSize', ctypes.c_uint),
                ('CmtSize', ctypes.c_uint),
                ('CmtState', ctypes.c_uint),
               ]

class RAROpenArchiveDataEx(ctypes.Structure):
    def __init__(self, ArcName=None, ArcNameW=u'', OpenMode=RAR_OM_LIST):
        self.CmtBuf = ctypes.c_buffer(64*1024)
        ctypes.Structure.__init__(self, ArcName=ArcName, ArcNameW=ArcNameW, OpenMode=OpenMode, _CmtBuf=ctypes.addressof(self.CmtBuf), CmtBufSize=ctypes.sizeof(self.CmtBuf))

    _fields_ = [
                ('ArcName', ctypes.c_char_p),
                ('ArcNameW', ctypes.c_wchar_p),
                ('OpenMode', ctypes.c_uint),
                ('OpenResult', ctypes.c_uint),
                ('_CmtBuf', ctypes.c_voidp),
                ('CmtBufSize', ctypes.c_uint),
                ('CmtSize', ctypes.c_uint),
                ('CmtState', ctypes.c_uint),
                ('Flags', ctypes.c_uint),
                ('Reserved', ctypes.c_uint*32),
               ]

class RARHeaderData(ctypes.Structure):
    def __init__(self):
        self.CmtBuf = ctypes.c_buffer(64*1024)
        ctypes.Structure.__init__(self, _CmtBuf=ctypes.addressof(self.CmtBuf), CmtBufSize=ctypes.sizeof(self.CmtBuf))

    _fields_ = [
                ('ArcName', ctypes.c_char*260),
                ('FileName', ctypes.c_char*260),
                ('Flags', ctypes.c_uint),
                ('PackSize', ctypes.c_uint),
                ('UnpSize', ctypes.c_uint),
                ('HostOS', ctypes.c_uint),
                ('FileCRC', ctypes.c_uint),
                ('FileTime', ctypes.c_uint),
                ('UnpVer', ctypes.c_uint),
                ('Method', ctypes.c_uint),
                ('FileAttr', ctypes.c_uint),
                ('_CmtBuf', ctypes.c_voidp),
                ('CmtBufSize', ctypes.c_uint),
                ('CmtSize', ctypes.c_uint),
                ('CmtState', ctypes.c_uint),
               ]

class RARHeaderDataEx(ctypes.Structure):
    def __init__(self):
        self.CmtBuf = ctypes.c_buffer(64*1024)
        ctypes.Structure.__init__(self, _CmtBuf=ctypes.addressof(self.CmtBuf), CmtBufSize=ctypes.sizeof(self.CmtBuf))

    _fields_ = [
                ('ArcName', ctypes.c_char*1024),
                ('ArcNameW', ctypes.c_wchar*1024),
                ('FileName', ctypes.c_char*1024),
                ('FileNameW', ctypes.c_wchar*1024),
                ('Flags', ctypes.c_uint),
                ('PackSize', ctypes.c_uint),
                ('PackSizeHigh', ctypes.c_uint),
                ('UnpSize', ctypes.c_uint),
                ('UnpSizeHigh', ctypes.c_uint),
                ('HostOS', ctypes.c_uint),
                ('FileCRC', ctypes.c_uint),
                ('FileTime', ctypes.c_uint),
                ('UnpVer', ctypes.c_uint),
                ('Method', ctypes.c_uint),
                ('FileAttr', ctypes.c_uint),
                ('_CmtBuf', ctypes.c_voidp),
                ('CmtBufSize', ctypes.c_uint),
                ('CmtSize', ctypes.c_uint),
                ('CmtState', ctypes.c_uint),
                ('Reserved', ctypes.c_uint*1024),
               ]

def DosDateTimeToTimeTuple(dosDateTime):
    """Convert an MS-DOS format date time to a Python time tuple.
    """
    dosDate = dosDateTime >> 16
    dosTime = dosDateTime & 0xffff
    day = dosDate & 0x1f
    month = (dosDate >> 5) & 0xf
    year = 1980 + (dosDate >> 9)
    second = 2*(dosTime & 0x1f)
    minute = (dosTime >> 5) & 0x3f
    hour = dosTime >> 11
    return time.localtime(time.mktime((year, month, day, hour, minute, second, 0, 1, -1)))

def _wrap(restype, function, argtypes):
    result = function
    result.argtypes = argtypes
    result.restype = restype
    return result

RARGetDllVersion = _wrap(ctypes.c_int, unrar.RARGetDllVersion, [])

RAROpenArchive = _wrap(ctypes.wintypes.HANDLE, unrar.RAROpenArchive, [ctypes.POINTER(RAROpenArchiveData)])
RAROpenArchiveEx = _wrap(ctypes.wintypes.HANDLE, unrar.RAROpenArchiveEx, [ctypes.POINTER(RAROpenArchiveDataEx)])

RARReadHeader = _wrap(ctypes.c_int, unrar.RARReadHeader, [ctypes.wintypes.HANDLE, ctypes.POINTER(RARHeaderData)])
RARReadHeaderEx = _wrap(ctypes.c_int, unrar.RARReadHeaderEx, [ctypes.wintypes.HANDLE, ctypes.POINTER(RARHeaderDataEx)])

_RARSetPassword = _wrap(ctypes.c_int, unrar.RARSetPassword, [ctypes.wintypes.HANDLE, ctypes.c_char_p])
def RARSetPassword(*args, **kwargs):
    _RARSetPassword(*args, **kwargs)

RARProcessFile = _wrap(ctypes.c_int, unrar.RARProcessFile, [ctypes.wintypes.HANDLE, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p])

RARCloseArchive = _wrap(ctypes.c_int, unrar.RARCloseArchive, [ctypes.wintypes.HANDLE])

UNRARCALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_uint, ctypes.c_long, ctypes.c_long, ctypes.c_long)
_RARSetCallback = _wrap(ctypes.c_int, unrar.RARSetCallback, [ctypes.wintypes.HANDLE, UNRARCALLBACK, ctypes.c_long])
def RARSetCallback(*args, **kwargs):
    _RARSetCallback(*args, **kwargs)


# Higher level interface

class ArchiveHeaderBroken(Exception): pass
class InvalidRARArchive(Exception): pass
class FileOpenError(Exception): pass

RARExceptions = {
                 ERAR_NO_MEMORY : MemoryError,
                 ERAR_BAD_DATA : ArchiveHeaderBroken,
                 ERAR_BAD_ARCHIVE : InvalidRARArchive,
                 ERAR_EOPEN : FileOpenError,
                }

class RARFile:
    def __init__(self, RAR, headerData):
        self.RAR = RAR

    def extract(self, filename=None):
        """Extract the file to the file system."""

        self._extracted = True
        RARProcessFile(self.RAR._handle, RAR_EXTRACT, None, filename)

class Archive:
    """Open and operate on an archive."""

    def __init__(self, archiveName, password=None):
        self.archiveName = archiveName
        archiveData = RAROpenArchiveDataEx(ArcNameW=self.archiveName, OpenMode=RAR_OM_EXTRACT)
        self._handle = RAROpenArchiveEx(ctypes.byref(archiveData))

        if archiveData.OpenResult != 0:
            raise RARExceptions[archiveData.OpenResult]

        if archiveData.CmtState == 1:
            self.comment = archiveData.CmtBuf.value
        else:
            self.comment = None

        if password:
            RARSetPassword(self._handle, password)

    def __del__(self):
        if self._handle and RARCloseArchive:
            RARCloseArchive(self._handle)
            
    def check(self):
        headerData = RARHeaderDataEx()
        if not 0 == RARReadHeaderEx(self._handle, ctypes.byref(headerData)):
            return False
        
        rarFile = RARFile(self, headerData)
        fn = str(random.random()).replace('.', '_')
        rarFile.extract(fn)
        
        if not os.path.exists(fn):
            return False
        
        os.remove(fn)
                
        return True

    def close(self):
        if self._handle and RARCloseArchive:
            RARCloseArchive(self._handle)

def dic_check(dic_fn, rar_fn):
    valid_pwd = None
    for f in file(dic_fn):
        pwd =  f.rstrip() 
        r=Archive(rar_fn, pwd)
        try:
            if r.check():
                valid_pwd = pwd
                break
        finally:
            r = None
            
    if valid_pwd is None:
        print 'not found'
    else:
        print 'password=' + valid_pwd
    
if __name__ == '__main__':
    import sys
    dic_fn = sys.argv[1]
    rar_fn = sys.argv[2]
    dic_check(dic_fn, rar_fn)
