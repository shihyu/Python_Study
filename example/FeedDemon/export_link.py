# -*- coding: cp950 -*-
from elementtree.ElementTree import parse
from fd4_export_with_categories import ExportUrlWithFolder
import os

class ExportUrlWithName(ExportUrlWithFolder):
    def export_feedid(self, folder_name):
        tree = self._getOpmlTree()
        url = []
        for feed in tree.findall('//outline'):
            if feed.get('text') == folder_name:
                url.append( feed.get('{http://www.bradsoft.com/feeddemon/xmlns/1.0/}feedId') )

        return url

if __name__ == '__main__':
    fd = ExportUrlWithName(r'E:\FeedDemon-data\v1')
    export_list = [u'Yahoo!奇摩新聞-即時新聞']
    for tag in export_list:
        print 'export %s...' % tag
        fd.export(tag)    
    
    print 'finish'    
