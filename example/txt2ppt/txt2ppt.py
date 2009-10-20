# -*- coding: cp950 -*-
"""
Description: txt �� ppt

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

path = r'H:\�ֺq�`��\�ֺq�`��\�ֺq���\�s�F³�ֿ�\*.txt'

def extractData(fn):
    f=open(fn)
    f_title = False
    data = False
    data_list = []
    for line in f:
        if data == True:
            data_list.append(line + "\r\n")
        elif len(line)==1 and line=='\n':
            data = True
        elif f_title == False and line.count('��')>0:
            cols = re.split('[ \t]', line)            
            id = cols[-2]
            title = cols[0].replace('��', '')
            f_title = True

        # Data    
        #print '%s => %d' % (line, len(line))
    content= ''.join( data_list)
    return id, title, content

Application = win32com.client.Dispatch("PowerPoint.Application")

for fn in glob.glob(path):
    #fn=r'H:\�ֺq�`��\�ֺq�`��\�ֺq���\�s�F³�ֿ�\001�aģ�k�P�̰���.txt'
    # ���ͷs�����ɦW
    path,fname= os.path.split(fn)
    name,ext= os.path.splitext(fname)
#    target = path + name + '.ppt'
    target = "d:\\" + name + '.ppt'    
    print target
    # txt �� ppt
    id, title, content=extractData(fn)
    #print "%s-%s" % (id,title)
    #print content
    #print name
    title,=re.search('\d*(.*)', name).groups()
    if len(title)==0:
        title=name

    Presentation = Application.Presentations.Add()
    Slide = Presentation.Slides.Add(1, 2)
    Shape = Slide.Shapes[0]
    Shape.TextFrame.TextRange.Text = title #u"���D"
    Shape = Slide.Shapes[1]
    Shape.TextFrame.TextRange.Paragraphs(Start=1, Length=1).ParagraphFormat.Bullet.Visible = False
    Shape.TextFrame.TextRange.Text = content #u"����"

    #�s��
    Presentation.SaveAs( target )

    #����
    Presentation.Close()


#Application.Quit()
