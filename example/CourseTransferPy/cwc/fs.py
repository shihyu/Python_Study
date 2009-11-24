#-*- coding: UTF-8 -*-
import os

def CreateDir(fd):
    if(not os.path.exists(fd)):
        os.makedirs( fd )
        
def file_put_contents(fn, content):
    f = open(fn, "w")
    f.write(content)
    f.close()
