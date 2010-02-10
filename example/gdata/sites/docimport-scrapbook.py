# -*- coding: cp950 -*-
"""
Description: 批次匯入 Scrapbook 導出文章到 Google Sites，不支援圖片

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
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
import logging
   

class DocsImportScrapbook(docimport.DocsImport):
  """
  批次匯入
  """
   
  def doIt(self, src, parent_name = None):
    print src
    parent = None
    log = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    h = logging.FileHandler('fail.log')
    h.setFormatter(formatter)
    log.addHandler(h)
    log.setLevel(logging.INFO)

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
        except UnicodeDecodeError, error:
          try:
            content=codecs.open(f, 'r', 'utf-8').read()            
          except UnicodeDecodeError, error:            
            print '%s =>open file fail, encode invalid' % name
            logl.info(name)
            continue
          
        self._import( name.decode('cp950'), ('<pre>%s</pre>' %content), parent )


def printHelp():
    print """python docimport-scrapbook.py --name [gmail username]
                                    --pwd [gmail passowrd]
                                    --src [import path]
                                    --dn [domain]
                                    --sn [site name]
                                    --pn [parent node]

            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\temp --sn wmdn  --dn sunnet.twbbs.org --pn /
          """
    sys.exit(2)
    
if __name__ == '__main__':

  try:
    opts, args = getopt.getopt(sys.argv[1:], '',
                               ['name=', 'pwd=', 'src=', 'sn=', 'dn=', 'pn='])
  except getopt.error, msg:
    printHelp()


  name = None
  pwd = None
  src = None
  sn = 'wmdn'
  dn = 'sunnet.twbbs.org' # or 'site'
  pn = None
  for option, arg in opts:
    if option == '--name':
      name = arg
    elif option == '--pwd':
      pwd = arg
    elif option == '--src':
      src = arg
    elif option == '--sn':
      sn = arg
    elif option == '--dn':
      dn = arg
    elif option == '--pn':
      pn = arg
      
  if src is None or sn is None:
    printHelp()
    
  if name is None:
    name = raw_input('username: ')

  if pwd is None:
    pwd = raw_input('password: ')
    
  print name, pwd, src      
  a = DocsImportScrapbook(site_name=sn, domain=dn)
  a.login(name, pwd)
  a.doIt(src, pn) 
  print 'finish'
