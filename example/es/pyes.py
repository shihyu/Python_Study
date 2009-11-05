# -*- coding: cp950 -*-
"""
Description: 利用 Everything Search Engine 找尋重複檔案

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"


import os
import sys
import hashlib
import view
import codecs

def md5_for_file(fn, block_size=2**20):
    md5 = hashlib.md5()
    with open(fn, 'rb') as f:    
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
        return md5.digest()

def match_md5(size_table):
    md5_table = {}
    for a in size_table:
        if len(size_table[a])>1:                
            for fn in size_table[a]:
                md5_code= md5_for_file(fn)
                if md5_table.has_key(md5_code):
                    md5_table[md5_code].append(fn)
                else:
                    md5_table[md5_code] = [fn]    

    return md5_table

def match_size(table):
    size_table = {}
    for fn in table:
        size = os.stat(fn).st_size
        if size_table.has_key(size):
            size_table[size].append(fn)
        else:
            size_table[size] = [fn]
    return size_table



cmd = 'es.exe %s'

def dup(filter, match_name=True, mode='console'):
    """
    找出重複檔案
    """
    #table = parse_exec_result(filter)
    print 'reading search result...'
    p = os.popen( cmd % filter)
    
    if match_name == True:
        print 'check file name ...'
        table = {}
        for line in p:
            line = line.strip()
            fn = line.split('\\')[-1]

            #檔名比對        
            if table.has_key(fn):
                table[fn].append( line )
            else:
                table[fn] = [line]

        print 'check file attribute ...'                     
        result = []
        for item in table:        
            if len(table[item])>1:
                # FileSize 比對            
                size_table = match_size( table[item] )

                # md5 比對
                md5_table = match_md5(size_table)

                # 顯示結果                        
                for a in md5_table:
                    if len(md5_table[a])>1:
                        if mode == 'console':                            
                            print item
                            print '\r\n'.join( md5_table[a] )                
                            print
                        else:
                            child_item = u''
                            for b in md5_table[a]:
                                child_item += u'<item id="{0}" />\r\n'.format( str.decode(b, 'big5') )
                                
                            result.append( u'<name id="{0}">{1}</name>'.format( item.decode('big5'), child_item ) )

                    
        
        if mode == 'win':
            import view
            print 'wait for result ...'
            xml = u'<list id="Result">{0}</list>'.format( u'\r\n'.join(result) )
            view.view_result( xml.encode('utf-8') )
        elif mode == 'xml':
            codecs.open('result.xml', 'w', 'utf-8').write( u'<list id="Result">{0}</list>'.format( u'\r\n'.join(result) ).encode('utf-8')
            pass
        
    else:
        pass
        """
        table = []        
        for line in p:
            line = line.strip()
            table.append(line)
            
            # FileSize 比對            
            size_table = match_size( table )
                
            # md5 比對
            md5_table = match_md5(size_table)        
        
            print '\r\n'.join( md5_table )                
            print
        """
        
if __name__ == '__main__':
    if len(sys.argv)>1:
        dup(sys.argv[1], mode='win')
        #print 'Search finish...'
    else:
        #dup('*.pdf')
        pass

    
