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
import sys
import gdata.sites.client
import gdata.sites.data
import glob
import codecs
import docimport
   
class DocsImportScrapbook(docimport.DocsImport):
  """
  批次匯入
  """
   
  def doIt(self, src, parent_name = None):
    print src
    parent = None


    if not parent_name is None:
      # 取得上層 feed
      feed = self.client.GetContentFeed('https://sites.google.com/feeds/content/%s/%s?path=%s' %(self.dn, self.sn, parent_name))
      if len(feed.entry)>0:
        parent = feed.entry[0]        

    for f in glob.glob(src + '\\*'):      
        print f
        fn = f.split('\\')[-1]        
        name = fn.split('.')[0]
        try:
          f = f+'\\index.html'
          content=codecs.open(f, 'r', 'cp950').read()
        except IOError:
          print '%s =>open file fail' % name          
          self.log.info('open fail=>' +name)
          continue;
        except UnicodeDecodeError, error:
          try:
            content=codecs.open(f, 'r', 'utf-8').read()            
          except UnicodeDecodeError, error:            
            print '%s =>open file fail, encode invalid' % name
            self.log.info(name)
            continue
  
        self._import( name.decode('cp950'), ('<pre>%s</pre>' %content), parent )


def printHelp():
    print """python docimport-scrapbook.py --name [gmail username]
                                    --pwd [gmail passowrd]
                                    --src [import path]
                                    --site [googlde site url]

            example:
            python docimport-scrapbook.py --name myid --pwd 1234 --src c:\temp --site https://sites.google.com/site/pythonzhishiku/1148
          """
    sys.exit(2)
    
if __name__ == '__main__':
  name, pwd, src, sn, dn, pn = docimport.parseArgs()
   
  a = DocsImportScrapbook(site_name=sn, domain=dn)
  a.login(name, pwd)
  a.doIt(src, pn) 
  print 'finish'
