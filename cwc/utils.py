#-*- coding: UTF-8 -*-
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import tempfile

class Logger():
    def __init__(self):
        self.fn = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    def close(self):
        self.fn.close()
    def append(self, msg):
        self.fn.writelines('%s\r\n' % msg)
    def __getattr__(self, name):
        if(name=='name'):
            return self.fn.name
