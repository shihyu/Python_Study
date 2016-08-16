#-*- coding: UTF-8 -*-
"""
Description: 透過 WMI 取得系統資訊

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import wmi

class OSInfo():
    def __init__(self):
        self._w = wmi.WMI()

    def dump_cpu(self):        
        """
        CPU 資訊
        也可以用 query
        for item in w.query("select * from Win32_Processor"):
            print item.DeviceID
        """
        for processor in self._w.Win32_Processor():
          print "Processor ID: %s" % processor.DeviceID
          print "Process Name: %s" % processor.Name.strip()
          print "Loading: %s" % processor.LoadPercentage
          print '最大頻率: %s' % processor.MaxClockSpeed
          print '目前頻率: %s' % processor.CurrentClockSpeed
          print '目前電壓: %s' % processor.CurrentVoltage
          print '位元: %s' % processor.DataWidth
          print '外頻: %s' % processor.ExtClock
          print u'Socket描述: %s' % processor.SocketDesignation
          print
    def dump_memory(self):
        """
        記憶體資訊
        等同於
        ELECT Capacity FROM Win32_PhysicalMemory
        """
        totalMemSize = 0
        for memModule in self._w.Win32_PhysicalMemory():
          totalMemSize += int(memModule.Capacity)
        print "Memory Capacity: %.2fMB" % self.byte_to_mb(totalMemSize)


    def dump_LogicalDisk(self):
        """
        邏輯磁碟資訊
        """
        for item in self._w.query("SELECT * FROM Win32_LogicalDisk"):
            print 'Disk Name: %s' %item.Name
            size = 0 if item.Size == None else int(item.Size)
            free_size = 0 if item.FreeSpace == None else int(item.FreeSpace)            
                
            print 'Disk Space: %.2f/%.2fMB' % (self.byte_to_mb(size), self.byte_to_mb(free_size) )
            print

    def dump_hdd(self):
        """
        實體硬碟資訊
        """
        for item in self._w.query("SELECT * FROM Win32_DiskDrive"):
            print 'HDD id: %s' %item.Model
            #size = 0 if item.Size == None else int(item.Size)
            #free_size = 0 if item.FreeSpace == None else int(item.FreeSpace)            
                
            #print 'Disk Space: %.2f/%.2fMB' % (self.byte_to_mb(size), self.byte_to_mb(free_size) )
            print

    def dump_BIOS(self):
        """
        BIOS 資訊
        Reference:
        [1] http://msdn.microsoft.com/en-us/library/aa394077%28VS.85%29.aspx
        """
        for item in self._w.query('SELECT * FROM Win32_BIOS'):
            print item.name
            print
            
    def dump_NetworkAdapter(self):
        """
        Reference:
        [1] http://msdn.microsoft.com/en-us/library/aa394217%28VS.85%29.aspx
        """
        for item in self._w.query("SELECT * FROM Win32_NetworkAdapterConfiguration"):
            print item.IPEnabled
            print "網卡編號: %s" % item.MacAddress
            print 

    def dump_SerialPort(self):
        """
        Serial Port 資訊
        Reference:
        [1] http://msdn.microsoft.com/en-us/library/aa394414%28VS.85%29.aspx
        """
        for item in self._w.query('SELECT * FROM Win32_SerialPortConfiguration'):
            print item.Name
            print
        
    def byte_to_mb(self, v):
        return (v+1048575)/1048576

    def dump_cpu_temperature():
        """
        CPU 溫度
        """
        for item in self._w.query("Select * From MSAcpi_ThermalZoneTemperature"):
           print item.CurrentTemperature
           
"""
列出所有的行程
Select * From Win32_Process 

列出所有系統服務
Select * From Win32_Service 

Select * From Cim_DataFile 
Where Drive = "C:" 
And Path = "\\Scripts\\" 

Associators Of {Win32_NetworkAdapter.DeviceId=1} 

Associators Of {Win32_NetworkAdapter.DeviceId=1} 
Where ResultClass = Win32_NetworkAdapterConfiguration 

Associators Of {Win32_NetworkAdapter.DeviceId=1} 
Where AssocClass = Win32_NetworkAdapterSetting 

References Of {Win32_NetworkAdapter.DeviceId=1} 

Select * From __InstanceCreationEvent 
Within 5 
Where TargetInstance Isa "Win32_Process"

ref
[1] http://www.codeproject.com/KB/system/WQLByExample.aspx
"""
if __name__ == '__main__':
    oi = OSInfo()
    oi.dump_SerialPort()

    



