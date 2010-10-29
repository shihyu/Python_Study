# -*- coding: cp950 -*-
"""
Description: doc 轉 pdf
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
for fn in glob.glob("F:\\upload\\*.doc"):
    doc = fn
    print '%s -- processing ' % doc
    path, name = os.path.split(fn)
    #print path, name
    name,ext = os.path.splitext(name)
    name = name + ".pdf"
    pdf = os.path.join(path, name)
    #print fn
    
    try:
        doc 	= msword.Documents.Open(FileName=doc)
        doc.SaveAs(FileName =pdf, FileFormat = 17)
    except:
        print '%s -- fail ' % doc 

msword.Quit()

