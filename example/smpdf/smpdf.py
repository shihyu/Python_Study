#-*- coding: UTF-8 -*-
"""
Description: 利用描述檔分割與合併PDF檔案

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

def convert(plain):
    output = PdfFileWriter()

    fn = ''
    infn = ''
    plain_f = codecs.open(plain, 'r', 'utf-8')    
    for i,line in enumerate(plain_f):
        if i == 0:
            infn = line = line.strip()
            print 'input: %s' % line
            input1 = PdfFileReader(file(line, "rb"))
            total = input1.getNumPages()
            continue
        elif i==1:
            fn = line.strip();
            if infn == fn:
                raise ValueError, 'file not the same'
            print 'output: %s' % fn
            continue
        
        if len(line)>0:
            if line.count('-')>0:
                begin, end=re.split('-', line)
                begin = int(begin)-1
                end = int(end)
                for i in range(begin, end):
                    if i>=total:
                        continue
                    print 'Processing Page #%d' % (i+1)
                    output.addPage(input1.getPage(i))
            else:
                if i>=total:
                    continue                
                line = int(line)-1
                print 'Processing Page #%d' % (line+1)
                output.addPage(input1.getPage( line ))

    print 'save to file...'
    outputStream = file(fn, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == '__main__':
    fn = sys.argv[1]
    if os.path.exists(fn):
        convert(fn)
    else:
        print 'file not exists'

        

#    
