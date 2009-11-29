# -*- coding: utf-8 -*-
"""
Description: 錄音裝置選取

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import clr
# WinForm 必要參考
clr.AddReference("System")
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

# DirectX 參考
clr.AddReferenceByName("Microsoft.DirectX, Version=1.0.2902.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" )
clr.AddReferenceByName("Microsoft.DirectX.DirectSound, Version=1.0.2902.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" )

from System import *
from System.IO import *
from System.Collections import *
from System.ComponentModel import *
from System.Windows.Forms import *
from System.Drawing import *
from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *
       
class DevicesForm(Form):
    def __init__(self, mf):
        self.InitializeComponent()

        self.mf = mf
        self.devices = CaptureDevicesCollection()
        for info in self.devices:
			self.comboboxCaptureDeviceCombo.Items.Add(info.Description)

        self.comboboxCaptureDeviceCombo.SelectedIndex = 0

    def InitializeComponent(self):
        self.buttonOk = Button()
        self.buttonCancel = Button()
        self.labelStatic = Label()
        self.comboboxCaptureDeviceCombo = ComboBox()
        self.SuspendLayout()
        # 
        # buttonOk
        # 
        self.buttonOk.Location = Point(10, 41)
        self.buttonOk.Name = "buttonOk"
        self.buttonOk.TabIndex = 0
        self.buttonOk.Text = "OK"
        self.buttonOk.Click += self.buttonOk_Click
        # 
        # buttonCancel
        # 
        self.buttonCancel.DialogResult = DialogResult.Cancel
        self.buttonCancel.Location = Point(231, 41)
        self.buttonCancel.Name = "buttonCancel"
        self.buttonCancel.TabIndex = 1
        self.buttonCancel.Text = "Cancel"
        self.buttonCancel.Click += self.buttonCancel_Click
        # 
        # labelStatic
        # 
        self.labelStatic.Location = Point(0, 14)
        self.labelStatic.Name = "labelStatic"
        self.labelStatic.Size = Size(88, 13)
        self.labelStatic.TabIndex = 2
        self.labelStatic.Text = "Capture Device:"
        # 
        # comboboxCaptureDeviceCombo
        # 
        self.comboboxCaptureDeviceCombo.DropDownStyle = ComboBoxStyle.DropDownList
        self.comboboxCaptureDeviceCombo.Location = Point(93, 11)
        self.comboboxCaptureDeviceCombo.Name = "comboboxCaptureDeviceCombo"
        self.comboboxCaptureDeviceCombo.Size = Size(213, 21)
        self.comboboxCaptureDeviceCombo.Sorted = True
        self.comboboxCaptureDeviceCombo.TabIndex = 3
        # 
        # DevicesForm
        # 
        self.AcceptButton = self.buttonOk
        self.CancelButton = self.buttonCancel
        self.ClientSize = Size(316, 79)
        self.Controls.Add(self.buttonOk)
        self.Controls.Add(self.buttonCancel)
        self.Controls.Add(self.labelStatic)
        self.Controls.Add(self.comboboxCaptureDeviceCombo)
        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.Name = "DevicesForm"
        self.Text = "Select Capture Device"
        self.ResumeLayout(False)

    def buttonOk_Click(self, sender, e):
    	if (0 < self.comboboxCaptureDeviceCombo.Items.Count):
            self.mf.CaptureDeviceGuid = self.devices[0].DriverGuid
		
        self.Close()

    def buttonCancel_Click(self, sender, e):
        self.Close()

if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = DevicesForm(None)
    Application.Run(frm)