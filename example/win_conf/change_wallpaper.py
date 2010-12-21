# -*- coding: cp950 -*-
'''
變更桌布
'''
import win32com.client
import time
class Wallpaper:
    def __init__(self):
        self.oShell = win32com.client.Dispatch("WScript.Shell")
        self.oSHApp =win32com.client.Dispatch("Shell.Application")
        
    def ApplyWallPaper(self, fn):
        '''
        套用桌布
        '''
        self.oShell.RegWrite( r"HKCU\Control Panel\Desktop\Wallpaper", fn)

    def RefreshScreen(self):
        '''
        更新畫面

        @TODO: 改用 win32 api
        '''
        self.oSHApp.ControlPanelItem("desk.cpl") 
        #Tabs: Themes(5), Desktop(0), Screen Saver(1), Appearance (2), Settings(3) 


        #Wait until Display Properites is active.
        idx =1 
        while not self.oShell.AppActivate("顯示 內容"):
            time.sleep( 2 )
            print idx
            print self.oShell.AppActivate("Display Properties")
            idx += 1
            pass
        
        print 'pass'
        self.oShell.SendKeys ("%T") # 'Jump to Them: Apply changes 
        time.sleep( 2 )
        self.oShell.SendKeys ("{DOWN}{UP}" )
        time.sleep( 2 )
        self.oShell.SendKeys( "+{TAB}{RIGHT}") # 'Shift & TAB 
        time.sleep( 2 )
        self.oShell.SendKeys( "%PS") # 'Jump to Position: Stretch wallpaper 
        time.sleep( 2 )
        self.oShell.SendKeys( "{TAB}{TAB}{TAB}{ENTER}"                         )
        time.sleep( 2)
            
if __name__ == '__main__':
    w = Wallpaper()
    w.ApplyWallPaper(r"c:\programmers-life-cartoon.gif")
    w.RefreshScreen()
