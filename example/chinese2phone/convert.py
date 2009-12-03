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

class phone:
    def __init__(self):
        """
        phone.cin.utf8 轉換成 SQLite

        """
        f=codecs.open("phone.cin.utf8", 'r', 'utf-8')
        step = 0
        self.keyname = {}
        self.chardef = {}
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
                self.keyname[code] = phone.strip()
            elif step == 2:
                #單字拼音
                code, word=line.split('\t')
                word=word.strip()        
                self.chardef[word]=code
                
    def parse(self, word):        
        code = self.chardef[word]
        return ''.join( [self.keyname[c] for c in code] )


if __name__ == '__main__' :
    p = phone()
    print p.parse(u'邱'),  p.parse(u'垂'), p.parse(u'汶')                       

