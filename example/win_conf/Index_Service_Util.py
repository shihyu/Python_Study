# -*- coding: cp950 -*-
'''
控制索引服務 (Indexing Service) 啟動,停止,暫停,繼續
'''
import win32com.client

class IndexService:
    def __init__(self):
        self.objAdminIS = win32com.client.Dispatch("Microsoft.ISAdm")
    def start(self):
        self.objAdminIS.start()
    def stop(self):
        self.objAdminIS.stop()        
    def pause(self):
        self.objAdminIS.pause()        
    def continue(self):
        self.objAdminIS.continue()
