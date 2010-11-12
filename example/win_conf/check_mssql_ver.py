#
# A script to check the SQL Server version and service pack on multiple servers
# Writes output to a text file.
#
import string,sys,win32com.client
from win32com.client import DispatchBaseClass

ListOfServers='c:\\MyDir\\AllServers.txt'
uid = 'rdameron'
txtfile = open('c:\\MyDir\\SQLVersions.txt','w')

for line in open(ListOfServers,'r').readlines():
  if line[0]<>'#':
     servers = string.split(string.strip(line),'\n')
     svr=servers[0]
     print svr
     sql = None
     txtfile.write('\n')
     txtfile.write( svr + ':  \n')
     adoConn = win32com.client.Dispatch('ADODB.Connection')
     connect = "Provider=SQLOLEDB.1;Data Source=%s;Initial Catalog=UMRdb;Integrated Security=SSPI;" % (svr)
     sql = "SELECT SERVERPROPERTY('ProductVersion') AS Version, SERVERPROPERTY('ProductLevel') as SP"
     #print sql
     adoConn.Open(connect)
     alog = adoConn.Execute(sql)
     while not alog[0].EOF:
        version=alog[0].Fields(0).Value
        sp=alog[0].Fields(1).Value
        txtfile.write('Version: ' +  version + '\n')
        txtfile.write('ServicePack: ' + sp + ' \n')
        alog[0].MoveNext()
txtfile.close()
adoConn = None