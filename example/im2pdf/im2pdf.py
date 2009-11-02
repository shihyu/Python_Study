# -*- coding: utf-8 -*-
"""
Description: 圖片合併成 PDF

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import warnings
warnings.simplefilter('ignore',DeprecationWarning)
import glob
import codecs
import Image
import os
import sys
from pyPdf import PdfFileWriter, PdfFileReader

def createPDF(output_pdf, fn_list):
    output = PdfFileWriter()
    
    outputStream = file(output_pdf, "wb")
    tmp_list = []
    pdf_i = 1
    for fn in fn_list:
        try:
            print "Converted " + fn        
            #轉PDF
            tmp_pdf = "tmp.pdf" 
            Image.open(fn).save(tmp_pdf)        

            #合併PDF
            f = file(tmp_pdf, "rb")
            input1 = PdfFileReader(f)
            output.addPage( input1.getPage(0) )
            output.write(outputStream)

        except IOError:
            print "Cannot convert" + fn



    outputStream.close()
    print 'Created: %s' % output_pdf

def parseConifg(fn):
    pdf = None
    fn_list = []
    for i,line in enumerate(codecs.open(fn, 'r', 'utf-8')     ):
        line = line.strip() 		
        if i == 0:
            pdf = line
	elif '*' in line:
	    for f in glob.glob(line):
		fn_list.append(f)
        else:
            fn_list.append(line)

    return fn_list, pdf
    
if __name__ == '__main__':
    if len(sys.argv)>1:
        fn = sys.argv[1]
        if os.path.exists(fn):
            fn_list, output_pdf = parseConifg( fn )
	    
            createPDF(output_pdf, fn_list)
        else:
            print 'file not exists'
    
