#-*- coding: UTF-8 -*-
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import re
def version(fname):
    """
    取得 PDF 版本
    """
    f=file(fname)
    c = f.readline()
    f.close()
    ver, = re.search('%PDF-([\d\.]+)', c).groups()
    return ver

if __name__ == '__main__':
    print version('d:\\d.pdf')
