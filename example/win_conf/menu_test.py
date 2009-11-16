#-*- coding: UTF-8 -*-
"""
Description: 執行其他應用程式的選單命令

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"
from ctypes import windll

class CMenu():
    def __init__(self, handle):
        self._h = handle
        self.menu_handle = windll.user32.GetMenu( self._h )        
        self.submenu = {}
        
    def get_menu_id(self, menu_id, item_id):
        if self.submenu.has_key( menu_id):
            submenu_handle = self.submenu[menu_id]
        else:
            submenu_handle = windll.user32.GetSubMenu(self.menu_handle, menu_id)
            self.submenu[menu_id] = submenu_handle
            
        item_handle = windll.user32.GetMenuItemID( submenu_handle, item_id)

        return item_handle

if __name__ == '__main__':
    h=windll.user32.FindWindowW(u'Notepad', None)
    if h== 0:
        print 'not found window'
    else:
        menu = CMenu(h)
        create_new = menu.get_menu_id(0, 0)
        
        # 執行, WM_COMMAND = 0x0111
        print windll.user32.PostMessageW(h, 0x0111, create_new, 0);
        
        
