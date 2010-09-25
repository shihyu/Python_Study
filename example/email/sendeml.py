# -*- coding: utf-8 -*-
"""
Description: CDO 發送 *.eml 檔案

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import win32com
from win32com.client import Dispatch
import glob
import getopt, sys

class SendEML:
    def __init__(self, uid, pwd, server='smtp.mail.yahoo.com', port=25):
        self.oMsg= win32com.client.Dispatch('CDO.Message')        
        iConfg= self.oMsg.Configuration.Fields
        iConfg['http://schemas.microsoft.com/cdo/configuration/sendusing'].Value=2
        iConfg['http://schemas.microsoft.com/cdo/configuration/smtpserverport'].Value=port
        iConfg['http://schemas.microsoft.com/cdo/configuration/smtpserver'].Value=server
        iConfg['http://schemas.microsoft.com/cdo/configuration/sendusername'].Value=uid
        iConfg['http://schemas.microsoft.com/cdo/configuration/sendpassword'].Value=pwd
        iConfg['http://schemas.microsoft.com/cdo/configuration/smtpauthenticate'].Value=1
        iConfg['http://schemas.microsoft.com/cdo/configuration/smtpusessl'].Value=True

    def send(self, to, eml):
        stm = win32com.client.Dispatch('ADODB.Stream')
        stm.Open(Mode= 0, Options=1)
        stm.Type = 1
        stm.LoadFromFile(eml)
        self.oMsg.DataSource.OpenObject(stm, "_stream")
        stm.Close()
        
        self.oMsg.From="unknown@gmail.com"
        self.oMsg.To=to        
        self.oMsg.Send()

def printHelp():
    print """python sendeml.py --yuid [yahoo username]
                                    --ypwd [yahoo email passowrd]
                                    --path [*.eml path]
                                    --to [send to email address]

            example:
            python sendeml.py --yuid your@yahoo.com --ypwd *** --path c:\eml --to friend@gmail.com
          """
    sys.exit(2)

if __name__ == '__main__':

  try:
    opts, args = getopt.getopt(sys.argv[1:], '',
                               ['yuid=', 'ypwd=', 'path=', 'to='])
  except getopt.error, msg:
    printHelp()


  yuid = None
  ypwd = None
  path = None
  to = None
  for option, arg in opts:
    if option == '--yuid':
      yuid = arg
    elif option == '--ypwd':
      ypwd = arg
    elif option == '--path':
      path = arg
    elif option == '--to':
      to = arg
      
  if yuid is None or ypwd is None or path is None or to is None:
    printHelp()
    
  obj = SendEML(yuid, ypwd)
  for eml in glob.glob( '%s\*.eml' % path):
      print eml
      obj.send(to, eml)




