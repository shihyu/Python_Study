#-*- coding: UTF-8 -*-
from win32api import *

def open_file_with_app(fn):
    ShellExecute(0, None, fn, None, "c:\\", True)