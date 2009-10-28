# -*- coding: utf-8 -*-
"""
Description: 中文轉拼音

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
Reference:
[1] phone.cin.utf8(http://cle.linux.org.tw/trac/attachment/wiki/GcinTablesXcin01/phone.cin.utf8?format=raw)
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import codecs


"""
phone.cin.utf8 轉換成 SQLite

"""
f=codecs.open("d:\\phone.cin.utf8", 'r', 'utf-8')
step = 0
keyname = {}
chardef = {}
for i, line in enumerate(f):
    
    if '%keyname  begin' in line:
        step =1
        continue
    
    if '%keyname  end' in line:
        continue

    if '%chardef  begin' in line:
        step=2
        continue

    if '%chardef  end' in line:
        break

   
    if step == 0:
        continue



    if step ==1:
        #注音音符
        code,phone = line.split('  ')
        keyname[code] = phone.strip()
    elif step == 2:
        #單字拼音
        code, word=line.split('\t')
        word=word.strip()        
        chardef[word]=code

code = chardef[u'小']
print ''.join( [keyname[c] for c in code] )

code = chardef[u'邱']
print ''.join( [keyname[c] for c in code] )
