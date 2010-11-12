# CheckDiskSpace.py
# 
# A script to check disk space on all database servers.  

import getpass,string,sys,win32com.client
from win32com.client import DispatchBaseClass

#ListOfServers='c:\\MyDir\\AFewServers.txt'
ListOfServers='c:\\MyDir\\AllServers.txt'

uid = 'rdameron'

# take your pick: HTML or Excel
#htmfile = open('c:\\MyDir\\SQLChkSpaceLog.htm','w')
htmfile = open('c:\\MyDir\\SQLChkSpaceLog.xls','w')

htmfile.write('<TITLE>SQL Server Space Report</TITLE>\n')

for line in open(ListOfServers,'r').readlines():
  if line[0]<>'#':
     servers = string.split(string.strip(line),'\n')
     svr=servers [0]
     print svr
     htmfile.write('<TABLE WIDTH=100% CELLPADDING=2 BORDER=2>\n')
     htmfile.write('<TR>\n')
     htmfile.write('<TD BGCOLOR=aqua ALIGN=CENTER VALIGN=top WIDTH=20%><B><FONT FACE="ARIAL" SIZE=2>' + svr + '</FONT></B></TD>\n')
     htmfile.write('<TD BGCOLOR=aqua ALIGN=CENTER VALIGN=top WIDTH=80%><B><FONT FACE="ARIAL" SIZE=2>Free Space Report</FONT></B></TD>\n')
     htmfile.write('</TR>\n')
     htmfile.write('<TD BGCOLOR=aqua ALIGN=LEFT VALIGN=top WIDTH=10%><B><FONT FACE="ARIAL" SIZE=2>Drive</FONT></B></TD>\n')
     htmfile.write('<TD BGCOLOR=aqua ALIGN=LEFT VALIGN=top WIDTH=20%><B><FONT FACE="ARIAL" SIZE=2>MB Free</FONT></B></TD>\n')            
     htmfile.write('</TR>\n')

     adoConn = win32com.client.Dispatch('ADODB.Connection')

     connect  = "Provider=SQLOLEDB.1;Data Source=%s;Initial Catalog=master;Integrated Security=SSPI;" % (svr)

     sql = '

        SET NOCOUNT ON

EXEC master.dbo.xp_fixeddrives

'

     adoConn.Open(connect)
     
     query = adoConn.Execute(sql)

     while not query[0].EOF:
        drive=query[0].Fields(0).Value
        free=query[0].Fields(1).Value
        htmfile.write('<TR>\n')
        htmfile.write('<TD VALIGN=top><FONT FACE="COURIER" SIZE=2>%s</FONT></TD>\n' % (drive))
        htmfile.write('<TD VALIGN=top><FONT FACE="COURIER" SIZE=2>%s</FONT></TD>\n' % (free))
        htmfile.write('</TR>\n')
        query [0].MoveNext()
     
     htmfile.write('</TABLE>\n')

htmfile.close()
adoConn = None