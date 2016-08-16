# -*- coding: cp950 -*-
'''
判別 Windows XP 是否已啟用

Supported on Windows XP , Windows Server 2003 , Not supported on Windows 2000
說明 ( 官方說法 ):
ActivationRequired
如果為 "1" , 系統的啟用 , 是由系統內 RemainingGracePeriod 參數所給的 "日期數" 來決定"啟用"
若為 "0", 則系統的啟用是不必要的, 在特定的週期內
IsNotificationOn
若不為 "0", 則產品的啟用是必要的 , 會顯示 "通知告示" 的訊息方塊及啟用圖示
在工作列的通告版 (Notification Tray) 上
若為 "0" , "通知告示","啟用圖示" 則不會出現
也可以從 [開始] -> [執行] , 輸入 oobe/msoobe /a , 再按 [確定]
來看 Windows 產品是否已啟動
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
