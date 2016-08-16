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
import logging

import time, random, hashlib            

import re

SOURCE_APP_NAME = 'googleInc-GoogleSitesAPIPythonLibSample-v1.0'
class DocsDel():
  """
  批次匯入
  """
  def __init__(self, src):
    print src
    self.dn, self.sn, self.src = re.search('http[s]{0,1}://sites.google.com/([0-9a-z]+)/([0-9a-z]+)(/.*)', src).groups()

    #self.dn = domain
    #self.sn = site_name
    self.client = gdata.sites.client.SitesClient(source=SOURCE_APP_NAME, site=self.sn, domain=self.dn)
    self.client.http_client.debug = False
    self.client.ssl = True
    log = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    h = logging.FileHandler('fail.log')
    h.setFormatter(formatter)
    log.addHandler(h)
    log.setLevel(logging.INFO)    
    self.log = log

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

   
  def doIt(self):
      uri = '%s?path=%s' % (self.client.MakeContentFeedUri(), self.src)
      feed= self.client.GetContentFeed(uri=uri)
      #print feed.entry[0]
      print self.client.Delete(feed.entry[0])

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
                               ['name=', 'pwd=', 'src='])
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


      
  if src is None or sn is None:
    printHelp()
    
  if name is None:
    name = raw_input('username: ')

  if pwd is None:
    pwd = raw_input('password: ')
    
  
  a = DocsDel(src)
  a.login(name, pwd)
  a.doIt() 
  print 'finish'
