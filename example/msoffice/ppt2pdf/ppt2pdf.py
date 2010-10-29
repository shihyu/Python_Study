# -*- coding: cp950 -*-
"""
Description: ppt 轉 pdf
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import glob
import os
import win32com.client
import sys
import re
app = win32com.client.Dispatch("PowerPoint.Application")
app.DisplayAlerts = False
for fn in glob.glob(r"F:\CUDA\*.ppt"):
    doc = fn
    print '%s -- processing ' % doc
    path, name = os.path.split(fn)
    #print path, name
    name,ext = os.path.splitext(name)
    name = name + ".pdf"
    pdf = os.path.join(path, name)
    #print fn
    
    try:
       doc = app.Presentations.Open(FileName=doc)
       doc.SaveAs(FileName =pdf, FileFormat = 32)
       doc.Close()
    except:
       print '%s -- fail ' % doc 

app.Quit()

