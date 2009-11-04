# -*- coding: cp950 -*-
"""
Description: �Q�� Everything Search Engine ��M�����ɮ�

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"


import os
#import md5
import hashlib
def md5_file(fn):
    with open(fn, 'rb') as f:
        m = hashlib.md5()
        m.update(f.read())
        s = m.hexdigest()
        #s = md5.new(f.read()).hexdigest()


    return s

def match_md5(size_table):
    md5_table = {}
    for a in size_table:
        if len(size_table[a])>1:                
            for fn in size_table[a]:
                md5_code= md5_file(fn)
                if md5_table.has_key(md5_code):
                    md5_table[md5_code].append(fn)
                else:
                    md5_table[md5_code] = [fn]    

    return md5_table

def match_size(table):
    size_table = {}
    for fn in table:
        print fn
        size = os.stat(fn).st_size
        if size_table.has_key(size):
            size_table[size].append(fn)
        else:
            size_table[size] = [fn]
    return size_table



cmd = 'es.exe %s'

def dup(filter, match_name=True):
    """
    ��X�����ɮ�
    """
    #table = parse_exec_result(filter)

    p = os.popen( cmd % filter)
    
    if match_name == True:
        table = {}
        for line in p:
            line = line.strip()
            fn = line.split('\\')[-1]

            #�ɦW���        
            if table.has_key(fn):
                table[fn].append( line )
            else:
                table[fn] = [line]
                
        for item in table:        
            if len(table[item])>1:
                # FileSize ���            
                size_table = match_size( table[item] )
                    
                # md5 ���
                md5_table = match_md5(size_table)

                # ��ܵ��G                        
                for a in md5_table:
                    if len(md5_table[a])>1:
                        print item
                        print '\r\n'.join( md5_table[a] )                
                        print
    else:
        pass
        """
        table = []        
        for line in p:
            line = line.strip()
            table.append(line)
            
            # FileSize ���            
            size_table = match_size( table )
                
            # md5 ���
            md5_table = match_md5(size_table)        
        
            print '\r\n'.join( md5_table )                
            print
        """            
if __name__ == '__main__':
    dup("*.jpg")
