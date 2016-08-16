# A script to find all occurrences of a database on multiple servers.
# Also, demonstrates passing arguments from the command line and error handling
# Writes output to a text file.
# 
# Usage: finddb.py DatabaseName

import string,sys,win32com.client
from win32com.client import DispatchBaseClass


# Python automatically stores the command-line arguments as a list of strings in the argv variable of the sys module.
# If you want to see the list of command-line arguments, remove the # in column 1 to uncomment the line - print sys.argv.
# sys.argv[0] always contains the name of the script.
#print sys.argv  

# Accept command-line argument for name of database to search for.
dbname = sys.argv[1]

#ListOfServers='c:\\MyDir\\AllServers.txt'
ListOfServers='c:\\ MyDir\\AFewServers.txt'

txtfile = open('C:\\MyDir\\FindDB.txt','w')
txtfile.write('Looking for database:  '+ dbname + '\n')
txtfile.write('\n')

for line in  open(ListOfServers,'r').readlines():
  if line[0]<>'#':
     servers = string.split(string.strip(line),',')
     svr=servers[0]
     print svr
     sql = None
     txtfile.write(svr + ': \n')
     adoConn = win32com.client.Dispatch('ADODB.Connection')
     connect = "Provider=SQLOLEDB.1;Data Source=%s;Initial Catalog=UMRdb;Integrated Security=SSPI;" % (svr)
     sql = "SELECT name FROM master..sysdatabases WHERE name = '" + dbname + "'"
     
     try:   # Python uses 'try ¡V except' to do error handling
        adoConn.Open( connect)
     except: 
        txtfile.write('\t' + "Oops, I wasn't able to connect to " + svr 
                      + ".  Make sure the server name is correct. \n")
        continue
        
     qry = adoConn.Execute(sql)
     
     if qry[0].EOF:  #database was not found 
        txtfile.write('\t' + 'Not here!' + '\n')
        
     while not qry[0].EOF:  #database was found
        db=qry[0].Fields(0).Value
        txtfile.write('\t' + 'Found it! ')
        txtfile.write('\t' + db + '\n')
         qry[0].MoveNext()
        
txtfile.close()
adoConn = None