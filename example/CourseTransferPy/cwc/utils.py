#-*- coding: UTF-8 -*-
import os
import tempfile
import threading
import shutil
import csv
import string
from cwc.fs import *

class Logger():
    def __init__(self):
        self.fn = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    def close(self):
        self.fn.close()
    def append(self, msg):
        self.fn.writelines('%s\r\n' % msg)
    def __getattr__(self, name):
        if(name=='name'):
            return self.fn.name

class Worker(threading.Thread):
    def __init__ (self,dlg):
        self.dlg = dlg
        threading.Thread.__init__(self,name='ct')
        
    def run(self):
        log = self.dlg.log
        dlg = self.dlg
        log.append(dlg.src)
        log.append(dlg.dst)

        c = CSV2XML(dlg.src, dlg.dst)
        log.append('Transfer main.csv')
        c.ConvertItemCsv()
        dlg.pb.SetValue(10)
        log.append('Transfer main.csv -- finish')

        log.append('Transfer item.csv')
        c.ConvertItemCsv()
        dlg.pb.SetValue(40)
        log.append('Transfer item.csv -- finish')

        log.append('Transfer main.csv')
        c.ConvertMainCsv()
        dlg.pb.SetValue(60)
        log.append('Transfer main.csv -- finish')

        log.append('Transfer glossary.csv')       
        c.ConvertGlossaryCsv()
        dlg.pb.SetValue(80)
        log.append('Transfer glossary.csv -- finish')        

        #log.append('Transfer exam.csv')
        #TODO: exam.csv to html
        #log.append('Transfer exam.csv -- finish')        
#        for x in range(1, 100):
#            dlg.pb.SetValue(x)
#            time.sleep(0.01)

        dlg.pb.Show(False)
        dlg.btnViewLog.Show(True)
        log.close()


class CSV2XML():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
            
    def ConvertItemCsv(self):
        fn = '%s\\item.csv' % self.src
        r = csv.reader(open(fn), delimiter=',', quotechar='"')
        r.next()
        ch = {}
        for row in r:
            if( ch.has_key( row[0] ) == False ):
                ch[row[0]] = {}
            if( ch[row[0]].has_key(row[1]) == False):
                ch[row[0]][row[1]] = {}

            obj = ch[row[0]][row[1]]
            tag = string.lower(row[2])
            if(tag == 'root' ):
                obj['root'] = {'type': row[3], "fly": row[7] }                
            elif (tag == 'slide' ):
                if(obj.has_key('slide')==False):
                    obj['slide'] = []
                obj['slide'].append( {"cue":row[4], "label":row[5], "url":row[6], "aside_url":row[8]} )
                
        for elem in ch:
            ch_item = ch[elem]    
            fd = '%s\\%s' % (self.dst, elem)
            CreateDir( fd )

            # copy item*.txt
            txt_dst = '%s\\txt' % fd
            CreateDir( txt_dst )

            txt = '%s\\txt\\%s' % (self.src, elem)            
            for fn in os.listdir(txt):
                item_fn = '%s\\%s' % (txt, fn)
                item_fn_dst = '%s\\%s' % (txt_dst, fn)
                shutil.copy (item_fn, item_fn_dst)
                
            for item_elem in ch[elem]:
                xml_fn = '%s\\%s' % (fd, item_elem)
                xml = '<?xml version="1.0" encoding="utf-8"?>\r\n'
                root = ch[elem][item_elem]['root']
                xml += '<root type="%s" flv="%s">\r\n\t<list>\r\n' % (root['type'], root['fly'])
                
                for side in ch[elem][item_elem]['slide']:
                    xml += """<side cue="%s" label="%s" url="%s">
      <aside url="%s" />
    </side>""" % (side['cue'], side['label'], side['url'], side['aside_url'])
                    
                xml += '\t</list>\r\n</root>'
                file_put_contents(xml_fn, xml)
                
        
    def ConvertMainCsv(self):
        fn = '%s\\main.csv' % self.src
        r = csv.reader(open(fn), delimiter=',', quotechar='"')
        r.next()
        ch = {}
        for row in r:
            if( ch.has_key( row[0] ) == False ):
                ch[row[0]] = {}                

            obj = ch[row[0]]
            tag = string.lower(row[1])
            if(tag == 'root' ):
                obj['root'] = {'id': row[2], "label": row[4] }                
            elif (tag == 'item' ):
                if(obj.has_key('item')==False):
                    obj['item'] = []
                obj['item'].append( {"id":row[2], "label":row[4], "url":row[5].strip(), "type":row[3]} )                
            elif (tag == 'pretest' ):
                obj['pretest'] = {"id":row[2], "label":row[4], "url":row[5].strip(), "type":row[3]}

        for elem in ch:
            ch_item = ch[elem]    
            fd = '%s\\%s' % (self.dst, elem)
            CreateDir( fd )

            xml_fn = '%s\\Main.xml' % fd

            xml = '<?xml version="1.0" encoding="utf-8"?>\r\n'
            xml += '<root id="%s" label="%s">\r\n' % (ch_item['root']['id'], ch_item['root']['label'])
            
            if(ch[elem].has_key('pretest')):                
                preTest = ch[elem]['pretest']
                xml += '\t<preTest id="%s" type="%s" label="%s" url="%s" />\r\n' % (preTest['id'], preTest['type'], preTest['label'], preTest['url'])
                
            for item in ch[elem]['item']:
                xml += '\t<item id="%s" type="%s" label="%s" url="%s" />\r\n' % (item['id'], item['type'], item['label'], item['url'])
            xml += '</root>'
            file_put_contents(xml_fn, xml)
    
    def ConvertGlossaryCsv(self):
        fn = '%s\\glossary.csv' % self.src        
        r = csv.reader(open(fn), delimiter=',', quotechar='"')
        r.next()
        ch = {}
        for row in r:
            if( ch.has_key( row[0] ) == False ):
                ch[row[0]] = []                

            obj = ch[row[0]]
            tag = string.lower(row[1])
            if(tag == 'item' ):
                obj.append( {'key': row[2], "note": row[3] }  )               
                
        for elem in ch:
            ch_item = ch[elem]    
            fd = '%s\\%s' % (self.dst, elem)
            CreateDir( fd )
	
            xml_fn = '%s\\Glossary.xml' % fd

            xml = '<?xml version="1.0" encoding="utf-8"?>\r\n'
            xml += '<Txts>\r\n'            
                    
            for item in ch[elem]:
                xml += '\t<item key="%s">%s</item>\r\n' % (item['key'], item['note'])
                
            xml += '</Txts>'                
            file_put_contents(xml_fn, xml)
