#-*- coding: UTF-8 -*-
"""
Description: 檢測 PDF 是否可以分割

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"


import warnings
warnings.simplefilter('ignore',DeprecationWarning)
import codecs
import re
from pyPdf import PdfFileWriter, PdfFileReader
import sys
import os
import glob

for fn in glob.glob(r"F:\MyBooks\_PDF\*.pdf"):
    try:
        output = PdfFileWriter()
        input1 = PdfFileReader(file(fn, "rb"))
        output.addPage(input1.getPage( 1 ))
        
        outputStream = file("d:\\t.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
    except:
        print fn
