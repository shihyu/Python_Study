# -*- coding: cp950 -*-
'''
RunAs

REF:
http://gallery.technet.microsoft.com/scriptcenter/zh-tw/9bda53d7-ec2e-4bc2-8e97-4487233bc55b
'''
import win32com.client
import time
WshShell = win32com.client.Dispatch("WScript.Shell") 
WshShell.run( "runas /user:domain\user %comspec%"   )
time.sleep( 1 )
WshShell.SendKeys("{CTRL}{ENTER}"   ) 
WshShell.SendKeys("13579xp") #send password   
WshShell.SendKeys("{ENTER}"   ) 
time.sleep( 1 )

#Open IE 
WshShell.SendKeys( '"C:\PROGRAM FILES\INTERNET EXPLORER\IEXPLORE.EXE"' )
WshShell.SendKeys( "{ENTER}" )
 
WshShell.SendKeys( "exit")  #Close command prompt 
WshShell.SendKeys( "{ENTER}" )
time.sleep( 1 )
 
WshShell.SendKeys( "{TAB}" )
WshShell.SendKeys( "http://www.microsoft.com") # 'Send internet page to open to IE 
WshShell.SendKeys( "{ENTER}" )
