# -*- coding: utf-8 -*-
"""
Description: 批次匯入 Scrapbook 導出文章到 Google Sites，不支援圖片

已知問題
1. 遇到 » 會發生錯誤
2. 不支援簡體中文
3. 不支援圖片
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"
import getopt

import os.path
import glob
import re, codecs, sys,time
from datetime import datetime

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

    
if __name__ == '__main__':
	src = r'F:\upload\ToCopy\web'
	log_fn = datetime.now().strftime("%Y%m%d%H%M%S")
	handle = codecs.open(log_fn, 'w', 'utf-8') 

	for f in glob.glob(src + '\\*'):
            fn = f.split('\\')[-1]
            name = fn.split('.')[0]
            f = f+'\\index.dat'
            try:
                content=open(safe_str(f), 'r').read()
                handle.write( re.search('source\t(.*)', content).groups()[0])
                handle.write('\n')
                
            except IOError:
                pass
            #if 'jQuery' in content:
            #    print fn
	print 'copy to %s' % log_fn
	handle.close()
