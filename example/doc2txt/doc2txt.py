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

msword = Dispatch('Word.Application')
msword.DisplayAlerts = 0
doc 	= msword.Documents.Open(FileName="xxx.doc")
wc = win32com.client.constants
doc.SaveAs(FileName ='xxx.doc', FileFormat = wc.wdFormatHTML)
msword.Quit()