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
import threading, time, Queue

THREAD_LIMIT = 10
jobs = Queue.Queue(0)
g_lock = threading.Lock()
g_total = 0
g_i = 0
g_writer = None
result = []

def md5_for_file(fn, block_size=2**20):
    md5 = hashlib.md5()
    try:
        with open(fn, 'rb') as f:    
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
            return md5.digest()
    except IOError:
        return None
        
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
        try:
            size = os.stat(fn).st_size
        except WindowsError:
            continue
        if size_table.has_key(size):
            size_table[size].append(fn)
        else:
            size_table[size] = [fn]

            
    return size_table

class console_writer:
    def write(self, item, dataset):
        print item
        print '\r\n'.join( dataset )                
        print        
        pass
    def close(self):
        pass

class xml_writer:
    def write(self, item, dataset):
        child_item = u''
        for b in dataset:
            b = b.replace('&', '&amp;')
            child_item += u'<item id="{0}" />\r\n'.format( str.decode(b, 'big5') )
        item = item.replace('&', '&amp;')

        global result
        result.append( u'<name id="{0}">{1}</name>'.format( item.decode('big5'), child_item ) )        
    def close(self):
        global result
        xml = u'<list id="Result">{0}</list>'.format( u'\r\n'.join(result) )
        codecs.open('result.xml', 'w', 'utf-8').write( xml  )

class view_writer(xml_writer):
    def close(self):
        import view
        xml = u'<list id="Result">{0}</list>'.format( u'\r\n'.join(result) )
        #TODO: id 含有 & 無法正常呈現
        try:
            view.view_result( xml.encode('utf-8') )
        except:
            print 'view result fail, save result to fail.xml'
        finally:
            codecs.open('result.xml', 'w', 'utf-8').write( xml  )
            print 'saved'
            
def thread_worker():    
    while True: # forever
        try:
            mode, item, dataset = jobs.get()

            # 顯示進度
            g_lock.acquire()
            global g_total, g_i
            print '(%d/%d)' % (g_i, g_total)
            g_i += 1            
            g_lock.release()            
            
            # FileSize 比對            
            size_table = match_size( dataset )

            # md5 比對
            md5_table = match_md5(size_table)

            # 顯示結果                        
            for a in md5_table:
                if len(md5_table[a])>1:
                    g_lock.acquire()
                    g_writer.write( item, md5_table[a])
                    g_lock.release()

            
            jobs.task_done()
            
        except Queue.Empty:
            return


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
        global g_total, g_i, result, g_writer

        # 生成 Writer
        if mode == 'win':
             g_writer = view_writer()
        elif mode == 'xml':
             g_writer = xml_writer()
        else:
            g_writer = console_writer()

        # 產生 thread job
        g_i = 1
        for item in table:
            if len(table[item])>1:
                jobs.put( [mode, item, table[item] ] )
                           
        g_total = jobs.qsize()
        
        for n in xrange(THREAD_LIMIT):
            t = threading.Thread(target=thread_worker)
            t.setDaemon(True)
            t.start()
            
        jobs.join()

    print 'wait for result ...'                    
    g_writer.close()
    print 'finish'
        
if __name__ == '__main__':
    if len(sys.argv)>1:
        dup(sys.argv[1], mode='win')
        #print 'Search finish...'
    else:
        dup('*.pdf')
        pass

    
