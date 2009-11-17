#-*- coding: UTF-8 -*-
"""
Description: 檔案分割與合併

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import os

block_size = 1024
"""
3.5"  = 1457664
1M    =  1048576
zip   = 98078*1024 = 100431872
cd700 = 700 *1024*1024 = 734003200
dvd+r = 4481 *1024*1024 
"""


def split_file(fin, split_size = 1048576):
    """
    檔案分割
    """
    fo = open(fin, 'rb')
    ofn = os.path.basename(fin)
    i = 1
    total = os.path.getsize(fin)
    progress = 0.0
    cur_size = 0
    ofn_part = open('%s.%03d' % (ofn, i), 'wb')
    while True:
        if split_size-cur_size >= block_size:
            data = fo.read(block_size)
            read_size = len(data)
            if read_size == 0:
                break;
            ofn_part.write(data)        
            cur_size += read_size
            if read_size < block_size:
                ofn_part.close()
                break        
        else:        
            data = fo.read(split_size-cur_size)
            ofn_part.write(data)
            ofn_part.close()
            i+=1
            cur_size = 0
            ofn_part = open('%s.%03d' % (ofn, i), 'wb')
            continue
           
        progress += read_size
        print round(progress/total *100, 0)        
    print 'finish'

def merge_file(fin):
    """
    檔案合併
    """
    fout = '.'.join( os.path.basename(fin).split('.')[0:2] )    
    if fin.split('.')[-1] == '001' :
        serial = int( fin.split('.')[-1] )        
        fout_h = open(fout, 'wb')
        while True:
            fin = '%s.%03d' % (fout, serial)            
            if not os.path.exists(fin):
                fout_h.close()
                break;
            
            print 'merge: %s' % fin
            
            fin_h = open(fin, 'rb')
            while True:
                data = fin_h.read( block_size )
                if len(data) == 0:
                    break
                fout_h.write(data)
            fin_h.close()
            
            serial+=1
            
        print 'finish'            
    else:
        print 'not found split part'
    
if __name__ == '__main__':
    split_file( 'd:\\t21f.pptx' )
    #merge_file(r'D:\MyProject\cwcpylib\example\split_file\t21f.pptx.001')

