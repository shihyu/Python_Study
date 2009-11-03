# -*- coding: cp950 -*-
"""
Description: 利用 Everything Search Engine 找尋重複檔案

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"


import os
cmd = 'es.exe %s'
p = os.popen( cmd % "*.pdf")
table = {}
for line in p:
    line = line.strip()
    fn = line.split('\\')[-1]
    if table.has_key(fn):
        table[fn].append( line )
    else:
        table[fn] = [line]

for item in table:
    if len(table[item])>1:
        # FileSize 比對
        print item        
        for fn in table[item]:
            print fn
        
        # md5 比對


