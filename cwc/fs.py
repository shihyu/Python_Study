#-*- coding: UTF-8 -*-
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import os

def CreateDir(fd):
    if(not os.path.exists(fd)):
        os.makedirs( fd )
        
def file_put_contents(fn, content):
    f = open(fn, "w")
    f.write(content)
    f.close()

def file_get_contenst(fn):
    f = open(fn, "r")
    c = f.read()
    f.close()
    return c