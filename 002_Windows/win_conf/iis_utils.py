# -*- coding: cp950 -*-
# IIS 操作
import win32com.client




class IIS:
    """
    IIS 5.x
    """
    def __init__(self):
        self.iis = win32com.client.GetObject("IIS://LocalHost/W3svc/1")
    def start(self):
        """
        網站啟動
        """        
        self.iis.start()
    def stop(self):
        """
        網站停止
        """        
        self.iis.stop()        
    def pause(self):
        """
        網站暫停
        """
        self.iis.pause()
    def mkVDir(self, computer, webname, vDirName, physicalPath):
        """
        建立虛擬目錄
        mkwebdir.vbs
        """
        webSite = IIS.findVDir(computer, webname)
        if webSite == None:
            return False
        print webSite.ADsPath    
        vRoot = webSite.GetObject("IIsWebVirtualDir", "Root")
        vDir = vRoot.Create("IIsWebVirtualDir",vDirName)

        # 設定權限        
        vDir.AccessRead = True
        vDir.Path = physicalPath
        vDir.AppFriendlyName = vDirName
        vDir.AccessScript = True
        vDir.AppRoot = vRoot.ADsPath.replace('IIS://LocalHost', 'LM')
        # 確定新增
        vDir.SetInfo()

        return True;
    def mkFtpVDir(self):
        """
        建立 FTP 虛擬目錄
        mkftpdir.vbs
        """
        pass
    @staticmethod
    def modifyNodePermission(webpath = "IIS://LocalHost/W3svc/1/Root", read=-1, write=-1, script=-1, execute=-1, browser=-1):
        """
        變更存取權限
        chaccess.vbs
        0=關閉
        1=啟動
        -1=未使用

        @example
        IIS.modifyNodePermission("IIS://LocalHost/W3svc/1/Root/abc", browser=0)
        """
        oAdmin = win32com.client.GetObject(webpath)
        if read == 0:
            oAdmin.Put('AccessRead', False)  
        elif read == 1:
            oAdmin.Put('AccessRead', True)  

        if write == 0:
            oAdmin.Put('AccessWrite', False)  
        elif write == 1:
            oAdmin.Put('AccessWrite', True)

        if script == 0:
            oAdmin.Put('AccessScript', False)  
        elif script == 1:
            oAdmin.Put('AccessScript', True)

        if execute == 0:
            oAdmin.Put('AccessExecute', False)  
        elif execute == 1:
            oAdmin.Put('AccessExecute', True)

        if browser == 0:
            oAdmin.Put('EnableDirBrowsing', False)  
        elif browser == 1:
            oAdmin.Put('EnableDirBrowsing', True)
            
        oAdmin.SetInfo()
        
    @staticmethod
    def showInfo(root_path = 'IIS://LocalHost', no_recursive = False):
        """
        顯示整個資訊樹狀結構

        @example
        IIS.showInfo()
        """
        oFirstNode = win32com.client.GetObject(root_path)
        IIS.__displayTree(oFirstNode, 0, no_recursive)
    @staticmethod    
    def __displayTree(FirstObj, Level, no_recursive):
        if FirstObj.Class in ["IIsWebServer", "IIsFtpServer"]:
            print "%s%s - %s (%s)" % (' '* (Level*2), FirstObj.Name,  FirstObj.ServerComment, FirstObj.Class)	
        else:
            print "%s%s (%s)" % (' '* (Level*2), FirstObj.Name, FirstObj.Class)	
	

	# Only recurse if so specified.
        if (Level == 0) or (not no_recursive):
            for CurrentObj in FirstObj:
                IIS.__displayTree(CurrentObj, Level + 1, no_recursive)
    @staticmethod		
    def showNodeInfo(AdsPath='IIS://LocalHost/w3svc'):
        """
        檢視特定節點資訊

        @example
        IIS.showNodeInfo()
        """
        AdminObject = win32com.client.GetObject(AdsPath)
        print "Name: %s" % AdminObject.Name 
        print "Class: %s" % AdminObject.Class
        print "Schema: %s" % AdminObject.Schema
        print "GUID: %s" % AdminObject.GUID
        print "Parent: %s" % AdminObject.Parent
        print "Path: %s" % AdminObject.AdsPath
        print

        def __ServerState(StateVal):
            tbl = {
                1: 'Starting',
                2: 'Started',
                3: 'Stopping',
                4: 'Stopped',
                5: 'Pausing',
                6: 'Paused',
                7: 'Continuing'
            }
            if StateVal in tbl:
                return tbl[StateVal]
            else:
                return 'Unknown'


        if (AdminObject.Class == "IIsComputer"): 
                print "Memory Cache Size: %s" % AdminObject.MemoryCacheSize
                print "Max Bandwidth: %s" % AdminObject.MaxBandWidth
        
        if (AdminObject.Class == "IIsWebService"):
                print "Directory Browsing: %s" % AdminObject.EnableDirBrowsing
                print "Default Document: %s" % AdminObject.DefaultDoc
                print "Script Access: %s" % AdminObject.AccessScript
                print "Execute Access: %s" % AdminObject.AccessExecute
        
        if (AdminObject.Class == "IIsFtpService"):
                print "Enable Port Attack: %s" % AdminObject.EnablePortAttack
                print "Lower Case Files: %s" % AdminObject.LowerCaseFiles

        
        if (AdminObject.Class == "IIsWebServer"):
                print "1st Binding: %s" % AdminObject.ServerBindings[0]
                print "State: %s" % __ServerState(AdminObject.ServerState)
                print "Key Type: %s" % AdminObject.KeyType
        
        if (AdminObject.Class == "IIsFtpServer"):
                print "State:%s" % __ServerState(AdminObject.ServerState)
                print "Greeting Message: %s" % AdminObject.GreetingMessage
                print "Exit Message: %s" % AdminObject.ExitMessage
                print "Max Clients Message: %s" % AdminObject.MaxClientsMessage
                print "Anonymous Only: %s" % AdminObject.AnonymousOnly
        
        if (AdminObject.Class == "IIsWebVirtualDir"):
                print "Path: %s" % AdminObject.path
                print "Default document: %s" % AdminObject.DefaultDoc
                print "UNC User Name: %s" % AdminObject.UNCUserName
                print "Directory browsing is %s" % AdminObject.EnableDirBrowsing
                print "Read Access is %s" % AdminObject.AccessRead
                print "Write Access is %s" % AdminObject.AccessWrite
        
        if (AdminObject.Class == "IIsFtpVirtualDir"):
                print "Path: %s" % AdminObject.path
                print "UNC User Name: %s" % AdminObject.UNCUserName
                print "Read Access is %s" % AdminObject.AccessRead
                print "Write Access is %s" % AdminObject.AccessWrite
        
        if AdminObject.Class in ["IIsWebService","IIsFTPService","IIsWebServer","IIsFTPServer"]:
                print "Server Comment: %s" % AdminObject.ServerComment
                print "Anonymous User: %s" % AdminObject.AnonymousUserName
                print "Default Logon Domain: %s" % AdminObject.DefaultLogonDomain
                print "Max Connections: %s" % AdminObject.MaxConnections
                print "Connection Timeout: %s" % AdminObject.ConnectionTimeout
                print "Read Access: %s" % AdminObject.AccessRead
                print "Write Access: %s" % AdminObject.AccessWrite
                print "Log: %s" % (not AdminObject.DontLog)
        	



    @staticmethod
    def findVDir(computer, webname):
         """
         尋找虛擬目錄
         @param computer string
         @param webname string
         @example
         print IIS.findVDir('LocalHost', u'預設的網站')
         """
         websvc = win32com.client.GetObject("IIS://%s/W3svc" % computer)
         #print (websvc.GetObject)
         #print IIS.showNodeInfo()
         try:
             #site = websvc.GetObject("IIsWebServer", webname)         
             #if not site == None:             
             #    if site.Class == "IIsWebServer":
             #        return site
                    
             for site in websvc:
                 if site.Class == "IIsWebServer":
                         if site.ServerComment == webname:                         
                             return site

                #print site.ServerComment
                #print site.ServerBindings()
         except :
             print 'err'
             pass
            
         return None

class Metabase:
    @staticmethod
    def Backup(BuName="SampleBackup", BuVersion=0xFFFFFFFF, BuFlags=0):
        """
        Metabase Backup
        error code = 80070050 (檔案已經存在)
        @param string 備份檔名
        @param int 版本號，FFFFFFFF=自動遞增
        @param int BuFlags 0 or 1
        """
        CompObj = win32com.client.GetObject("IIS://Localhost")
        CompObj.Backup(BuName, BuVersion, BuFlags)
        CompObj = None
    @staticmethod
    def Restore(BuName="SampleBackup", BuVersion=0xFFFFFFFF, BuFlags=0):
        CompObj = win32com.client.GetObject("IIS://Localhost")
        CompObj.Restore(BuName, BuVersion, BuFlags)
        CompObj = None
    
o = IIS()
print o.mkVDir('LocalHost', u'預設的網站', 'xxyy2', 'c:\\a')
#IIS.showNodeInfo('IIS://LocalHost/W3svc/1/Root/NVMS')
#IIS.showInfo();


