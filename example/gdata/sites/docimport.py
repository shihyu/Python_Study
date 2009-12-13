# -*- coding: cp950 -*-
import getopt

import os.path
import sys
import gdata.sites.client
import gdata.sites.data
import glob
import codecs

import time, random, hashlib            
def uuid( *args ):
  """
    Generates a universally unique ID.
    Any arguments only create more randomness.
  """
  
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
    
  def doIt(self, src):
    print src
    # 取得暫存文件 feed
    feed = self.client.GetContentFeed('https://sites.google.com/feeds/content/sunnet.twbbs.org/wmdn?path=/zan-cun')
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
            
        self._import( name.decode('cp950'), ('<pre>%s</pre>' %content), parent )

        
if __name__ == '__main__':

  try:
    opts, args = getopt.getopt(sys.argv[1:], '',
                               ['name=', 'pwd=', 'src='])
  except getopt.error, msg:
    print """python docimport.py --name [gmail username]
                                    --pwd [gmail passowrd]
                                    --src [import path]
            example:
            python docunoirt.py --name myid --pwd 1234 --src c:\*.txt
          """

    sys.exit(2)

  name = None
  pwd = None
  src = None
  
  for option, arg in opts:
    if option == '--name':
      name = arg
    elif option == '--pwd':
      pwd = arg
    elif option == '--src':
      src = arg

  if src is None:
    exit('source is null')
    
  if name is None:
    name = raw_input('username: ')

  if pwd is None:
    pwd = raw_input('password: ')

  print name, pwd, src      
  a = DocsImport()
  a.login(name, pwd)
  a.doIt(src) # "F:\\MyExample\\*.txt"
  print 'finish'
