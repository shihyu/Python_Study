# -*- coding: cp950 -*-
'''
�N [�ϥΪ�] �[�J [�s��]
�`�N : �s�դΨϥΪ̥����w�g�s�b
'''

import win32com.client

def addToGroup(computer_name, group_name, user_name):    
    win32com.client.GetObject("WinNT://%s/%s,GROUP" % (computer_name, group_name) ).Add( "WinNT://%s/%s,USER" %(computer_name, user_name) )

addToGroup('CWC-FAMILY', 'HelpServicesGroup', 'cwchiu')    
