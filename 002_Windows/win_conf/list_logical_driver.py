# -*- coding: cp950 -*-
'''
�p��C�|�ثe�q�����Ҧ����޿�Ϻо�
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

