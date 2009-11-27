# -*- coding: utf-8 -*-
"""
Description: 列舉音訊裝置

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import clr

clr.AddReference("System")

# DirectX 參考
clr.AddReferenceByName("Microsoft.DirectX, Version=1.0.2902.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" )
clr.AddReferenceByName("Microsoft.DirectX.DirectSound, Version=1.0.2902.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" )


from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *

def displaySoundDevice():
    devicesCollection = DevicesCollection()
    for dev in devicesCollection:
        print '[%s]=>%s' % (dev.DriverGuid, dev.Description)

def displayCaptureDevice():
    captureCollection = CaptureDevicesCollection()
    for dev in captureCollection:
        print '[%s]=>%s' % (dev.DriverGuid, dev.Description)
        
if __name__ == '__main__':
    print '== Sound Device =='
    displaySoundDevice()

    print

    print '== Capture Device =='
    displayCaptureDevice()
    

