# -*- coding: cp950 -*-
'''
�P�O Windows XP �O�_�w�ҥ�

Supported on Windows XP , Windows Server 2003 , Not supported on Windows 2000
���� ( �x�軡�k ):
ActivationRequired
�p�G�� "1" , �t�Ϊ��ҥ� , �O�Ѩt�Τ� RemainingGracePeriod �ѼƩҵ��� "�����" �ӨM�w"�ҥ�"
�Y�� "0", �h�t�Ϊ��ҥάO�����n��, �b�S�w���g����
IsNotificationOn
�Y���� "0", �h���~���ҥάO���n�� , �|��� "�q���i��" ���T������αҥιϥ�
�b�u�@�C���q�i�� (Notification Tray) �W
�Y�� "0" , "�q���i��","�ҥιϥ�" �h���|�X�{
�]�i�H�q [�}�l] -> [����] , ��J oobe/msoobe /a , �A�� [�T�w]
�Ӭ� Windows ���~�O�_�w�Ұ�
( OOBE : Out of Box Experience )
'''
import win32com.client
wpa = win32com.client.GetObject("winmgmts:root/cimv2").ExecQuery("Select * From Win32_WindowsProductActivation")
for v in wpa:
    print "Activation Required: %s" % v.ActivationRequired
    print "IsNotificationOn : %s" % v.IsNotificationOn
    print "Description: %s" % v.Description
    print "Product ID: %s" % v.ProductID
    print "Remaining Evaluation Period: %s" % v.RemainingEvaluationPeriod
    print "Remaining Grace Period: %s" % v.RemainingGracePeriod
    print "Server Name: %s" % v.ServerName
    print "SeetingID : %s" % v.SettingID
