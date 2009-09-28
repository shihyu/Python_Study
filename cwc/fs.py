#-*- coding: UTF-8 -*-
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