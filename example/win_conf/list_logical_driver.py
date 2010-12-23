# -*- coding: cp950 -*-
'''
如何列舉目前電腦中所有的邏輯磁碟機
'''

def method_1():
    import win32api
    print win32api.GetLogicalDriveStrings().split('\0')[:-1]

    
def method_2():
    import win32file
    for v in xrange(65,81):
	label = chr(v) + ':\\'
	if win32file.GetDriveType( label) > 1:
		print label    

def method_3():
    import win32com.client
    fs=win32com.client.Dispatch('Scripting.FileSystemObject')
    for v in fs.Drives:
	print v + ':\\'   

