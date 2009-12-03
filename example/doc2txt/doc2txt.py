# -*- coding: cp950 -*-
"""
Description: txt 轉 ppt

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import glob
import os
import win32com.client
import sys
import re
msword = win32com.client.Dispatch('Word.Application')
msword.DisplayAlerts = 0
for fn in glob.glob("H:\\其他詩歌\\*.doc"):
    doc = fn
    print '%s -- processing ' % doc
    path, name = os.path.split(fn)
    #print path, name
    name,ext = os.path.splitext(name)
    name = name + ".txt"
    txt = os.path.join(path, name)
    #print fn
    
    try:
        doc 	= msword.Documents.Open(FileName=doc)
        doc.SaveAs(FileName =txt, FileFormat = 2)
    except:
        print '%s -- fail ' % doc 

msword.Quit()

