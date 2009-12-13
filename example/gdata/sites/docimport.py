# -*- coding: cp950 -*-
"""
Description: 批次匯入文章到 Google Sites

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

import time, random, hashlib            
def uuid( *args ): 
  t = long( time.time() * 1000 )
  r = long( random.random()*100000000000000000L )
  try:
    a = socket.gethostbyname( socket.gethostname() )
  except:
    # if we can't get a network address, just imagine one
    a = random.random()*100000000000000000L
  data = str(t)+' '+str(r)+' '+str(a)+' '+str(args)
  data = hashlib.md5( data ).hexdigest() 
  return data


SOURCE_APP_NAME = 'googleInc-GoogleSitesAPIPythonLibSample-v1.0'
class DocsImport():
  """
  批次匯入
  """
  def __init__(self, site_name='wmdn', domain='sunnet.twbbs.org'):
    self.dn = domain
    self.sn = site_name
    self.client = gdata.sites.client.SitesClient(source=SOURCE_APP_NAME, site=site_name, domain=domain)
    self.client.http_client.debug = False
    self.client.ssl = True

  def login(self,name, password):
    """
    登入
    """
    try:
      self.client.client_login(name, password, source=SOURCE_APP_NAME, service=self.client.auth_service)
    except gdata.client.BadAuthentication:
      exit('Invalid user credentials given.')
    except gdata.client.Error, error:
      print error
      exit('Login Error')    

  def _import(self, title, content, parent= None):
    """
    匯入
    """    
    try:
      # 文件標題
      # 內文
      # url
      new_entry = self.client.CreatePage('webpage', title, content, uuid(), parent=parent)
      if new_entry.GetAlternateLink():
        print '%s => %s' % (title, new_entry.GetAlternateLink().href)         
    except gdata.client.RequestError, error:
      print '%s =>fail' % title
      print error
    except KeyboardInterrupt:
      return
    
  def doIt(self, src, parent_name = None):
    print src
    parent = None    
    if not parent_name is None:
      # 取得上層 feed
      feed = self.client.GetContentFeed('https://sites.google.com/feeds/content/%s/%s?path=%s' %(self.dn, self.sn, parent_name))
      if len(feed.entry)>0:
        parent = feed.entry[0]
        

    for f in glob.glob(src):
        fn = f.split('\\')[-1]
        name = fn.split('.')[0]
        try:
          content=codecs.open(f, 'r', 'cp950').read()
        except UnicodeDecodeError, error:
          try:
            content=codecs.open(f, 'r', 'utf-8').read()            
          except UnicodeDecodeError, error:            
            print '%s =>open file fail, encode invalid' % name
            continue
          
        self._import( name.decode('cp950'), ('<pre>%s</pre>' %content), parent )


def printHelp():
    print """python docimport.py --name [gmail username]
                                    --pwd [gmail passowrd]
                                    --src [import path]
                                    --dn [domain]
                                    --sn [site name]
            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\*.txt

            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\*.txt -sn chuiwenchiu

            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\*.txt -sn chuiwenchiu  -dn site

            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\*.txt -sn wmdn  -dn sunnet.twbbs.org            
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
  a = DocsImport(site_name=sn, domain=dn)
  a.login(name, pwd)
  a.doIt(src, pn) 
  print 'finish'
