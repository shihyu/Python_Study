# -*- coding: cp950 -*-
'''
�]�w�t�ιw�]�L���
'''

def with_com(printer_name):
    '''
    @example with_com('PDFCreator')
    '''
    import win32com.client
    wsh = win32com.client.Dispatch('WScript.Network')
    wsh.SetDefaultPrinter(printer_name)

def with_wmi():
    pass

def with_win32():
    pass
