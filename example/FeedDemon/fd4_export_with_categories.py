# -*- coding: cp950 -*-
'''

'''
from elementtree.ElementTree import parse
import apsw
import os
from datetime import datetime

FeedDemonPath = r'D:\tools\FeedDemon\FeedDemon-data\v1'

class ExportUrlWithFolder:
    def __init__(self, data_root):
        self.data_root = data_root

    def export(self, folder_name):
        feeds = self.export_feedid(folder_name)
        self.export_link( folder_name, feeds )

    def _getOpmlTree(self):
        opml = os.path.join(self.data_root, 'Subscriptions.opml')
        tree = parse(opml)
        return tree
    
    def export_feedid(self, folder_name):
        tree = self._getOpmlTree()
        url = []
        for e in tree.findall('/body/outline/outline'):
                if e.get('text') == folder_name:
                        for feed in e.findall('outline'):
                                url.append( feed.get('{http://www.bradsoft.com/feeddemon/xmlns/1.0/}feedId') )

        return url

    def export_link(self, folder_name, url):
       
        if len(url)>0:
            in_part = '"' + '","'.join( url ) + '"'            
            if len(url) == 1:
                in_part = ' = %s ' % in_part
            else:
                in_part = ' in (%s) ' % in_part

            filename = "%s_%s" % (folder_name, datetime.now().strftime("%Y%m%d%H%M%S"))
            fn = open(filename, 'w')
            sql = "select link from tbl_posts where fd_feedid %s and flagged = 1" % in_part
            db = apsw.Connection( os.path.join(self.data_root, 'feeds.fdb'))
            cur = db.cursor()
            cur.execute(sql)
            for row in cur:
                fn.write( row[0] )
                fn.write( '\n')    
            fn.close()    
            print 'export %s' % filename
            
            sql = "update tbl_posts set flagged = 0 where fd_feedid %s " % in_part
            #print sql
            print 'remove flag'
            cur.execute(sql)
            db.close()

if __name__ == '__main__':
    fd = ExportUrlWithFolder(r'D:\tools\FeedDemon\FeedDemon-data\v1')
    export_list = [u'軟體工具']
    for tag in export_list:
        print 'export %s...' % tag
        fd.export(tag)    
    
    print 'finish'    

