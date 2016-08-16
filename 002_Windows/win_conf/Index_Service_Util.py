# -*- coding: cp950 -*-
'''
������ުA�� (Indexing Service) �Ұ�,����,�Ȱ�,�~��
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
