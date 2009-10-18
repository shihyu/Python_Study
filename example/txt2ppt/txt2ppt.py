#-*- coding: UTF-8 -*-
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

path = 'd:\\*.txt'

Application = win32com.client.Dispatch("PowerPoint.Application")
for fn in glob.glob(path):
    # 產生新的副檔名
    path,fname= os.path.split(fn)
    name,ext= os.path.splitext(fname)
    target = path + name + '.ppt'

    # txt 轉 ppt
    """
    套版
    Presentation = Application.Presentations.Open(target)
    
    # 建立新的投影片
    Presentation = Application.Presentations.Add()
    # 建立新的空白頁面
    Slide = Presentation.Slides.Add(1, 12)
    Presentation.SaveAs( target )
    """
    pass
    
Application.Quit()
