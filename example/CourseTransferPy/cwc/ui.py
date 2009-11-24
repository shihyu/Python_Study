#-*- coding: utf-8 -*-
import wx
from win32api import *
import time
import os
import string
from cwc.utils import *

class MainFrame(wx.Frame):
    def __init__(self):        
        wx.Frame.__init__(self, None, -1, "Course Transfer", size=(400, 300))        
        panel=wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Source:", pos=(10,12))
        self.txtSrc = wx.TextCtrl(panel, -1, "d:\\result\\src", pos=(60,10), size=(200, 20))


        self.btnSource = wx.Button(panel, label="...", pos=(280, 10), size=(40,20))
        self.Bind(wx.EVT_BUTTON, self.OnBrowserFile, self.btnSource)
        
        wx.StaticText(panel, -1, "Target:", pos=(10,42))
        self.txtDst = wx.TextCtrl(panel, -1, "d:\\result\\dst", pos=(60,40), size=(200,20))        
        self.btnTarget = wx.Button(panel, label="...", pos=(280, 40), size=(40,20))
        self.Bind(wx.EVT_BUTTON, self.OnBrowserFile, self.btnTarget)

        btnConvert = wx.Button(panel, label="Go", pos=(180, 100), size=(40,20))
        self.Bind(wx.EVT_BUTTON, self.OnConvert, btnConvert)

        
    def OnConvert(self, event):
        src = self.txtSrc.GetValue()
        dst = self.txtDst.GetValue()
        f = SubFrame(src, dst)
        f.ShowModal()
        f.Destroy()
        
    def OnBrowserFile(self, event):
        dlg = wx.DirDialog(None)
        if(dlg.ShowModal() == wx.ID_OK):
            path= dlg.GetPath()
            if( event.GetId() == self.btnSource.GetId()):
                self.txtSrc.SetValue(path)
            else:
                self.txtDst.SetValue(path)

        dlg.Destroy()
        
        
class SubFrame(wx.Dialog):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.log = Logger()
        
        wx.Dialog.__init__(self, None, -1, "Course Transfer", size=(300, 150) )        
        panel=wx.Panel(self, -1)
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.pb = wx.Gauge(panel, pos=(50, 50), size=(200,20))

        
        self.btnViewLog = wx.Button(panel, label="View Log", pos=(110, 100), size=(80,20))
        self.btnViewLog.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnViewLog, self.btnViewLog)
        
        self.OnRun()
        
    def OnRun(self):
        worker = Worker(self)
        worker.start()   
        
    def OnViewLog(self, event):
        ShellExecute(0, None, self.log.name, None, "c:\\", True)
