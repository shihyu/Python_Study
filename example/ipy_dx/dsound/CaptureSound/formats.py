# -*- coding: utf-8 -*-
"""
Description: 錄音格式選取

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

def ConvertWaveFormatToString(format):
    #-----------------------------------------------------------------------------
    # Name: ConvertWaveFormatToString()
    # Desc: Converts a wave format to a text string
    #-----------------------------------------------------------------------------
    return '{0}  Hz, {1}-bit {2}'.format(format.SamplesPerSecond, \
        format.BitsPerSample, \
        ("Mono" if (format.Channels == 1) else "Stereo")) 
      
class FormatInfo(Object):
    def __init__(self):
        self._format = None;

    @property 
    def format(self): 
        return self._format 

    @format.setter 
    def format(self, value): 
        self._format = value 

    def ToString(self):
        return ConvertWaveFormatToString(self._format)
       
class FormatsForm(Form):
    def __init__(self, mf):
        self.InputFormatSupported = [False for i in range(20)]
        self.formats = []

        self.InitializeComponent()
        self.mf = mf

        self.ScanAvailableInputFormats()
        self.FillFormatListBox()
    def ScanAvailableInputFormats(self):
        #-----------------------------------------------------------------------------
		# Name: ScanAvailableInputFormats()
		# Desc: Tests to see if 20 different standard wave formats are supported by
		#       the capture device 
		#-----------------------------------------------------------------------------
        format = WaveFormat()
        dscheckboxd = CaptureBufferDescription()
        pDSCaptureBuffer = None

        # This might take a second or two, so throw up the hourglass
        self.Cursor = Cursors.WaitCursor

        format.FormatTag = WaveFormatTag.Pcm

        # Try 20 different standard formats to see if they are supported
        for iIndex in range(20):
            format = self.GetWaveFormatFromIndex(iIndex, format)

            # To test if a capture format is supported, try: to create a 
            # capture buffer using a specific format.  If it works
            # then the format is supported, otherwise not.
            dscheckboxd.BufferBytes = format.AverageBytesPerSecond
            dscheckboxd.Format = format

            try:                
                pDSCaptureBuffer = CaptureBuffer(dscheckboxd, self.mf.applicationDevice)
                self.InputFormatSupported[ iIndex ] = True            
            except:
                self.InputFormatSupported[ iIndex ] = False

            if (not pDSCaptureBuffer is None):
                pDSCaptureBuffer.Dispose()
		
		self.Cursor = Cursors.Default  

    def GetWaveFormatFromIndex(self, Index, format):         
		#-----------------------------------------------------------------------------
		# Name: GetWaveFormatFromIndex()
		# Desc: Returns 20 different wave formats based on Index
		#-----------------------------------------------------------------------------
        SampleRate = Index / 4
        iType = Index % 4

        format.SamplesPerSecond={
            0: 48000,
            1: 44100,
            2: 22050,
            3: 11025,
            4:  8000
        }[SampleRate]

        format.BitsPerSample, format.Channels ={
            0: (8, 1),
            1: (16, 1),
            2: (8, 2),
            3: (16, 2)
        }[iType]		

        format.BlockAlign = (format.Channels * (format.BitsPerSample / 8))
        format.AverageBytesPerSecond = format.BlockAlign * format.SamplesPerSecond
        return format

    def FillFormatListBox(self):
        #-----------------------------------------------------------------------------
        # Name: FillFormatListBox()
        # Desc: Fills the format list box based on the availible formats
        #-----------------------------------------------------------------------------

        strFormatName	= ''

        for iIndex in range( len(self.InputFormatSupported)):
            if (True == self.InputFormatSupported[iIndex]):
                # Turn the index into a WaveFormat then turn that into a
                # string and put the string in the listbox
                info   = FormatInfo()		
                format = WaveFormat()
                format = self.GetWaveFormatFromIndex(iIndex, format)

                info.format = format
                self.formats.append(info)
                    
        self.lbFormatsInputListbox.DataSource = self.formats		      


    def InitializeComponent(self):
        self.buttonOk = Button()
        self.buttonCancel = Button()
        self.lbFormatsInputListbox = ListBox()
        self.labelStatic = Label()
        self.SuspendLayout()
        # 
        # buttonOk
        # 
        self.buttonOk.Enabled = False
        self.buttonCancel.DialogResult = DialogResult.OK
        self.buttonOk.Location = Point(10, 128)
        self.buttonOk.Name = "buttonOk"
        self.buttonOk.TabIndex = 0
        self.buttonOk.Text = "OK"
        self.buttonOk.Click += self.buttonOk_Click
        # 
        # buttonCancel
        # 
        self.buttonCancel.DialogResult = DialogResult.Cancel
        self.buttonCancel.Location = Point(97, 128)
        self.buttonCancel.Name = "buttonCancel"
        self.buttonCancel.TabIndex = 1
        self.buttonCancel.Text = "Cancel"
        self.buttonCancel.Click += self.buttonCancel_Click
        # 
        # lbFormatsInputListbox
        # 
        self.lbFormatsInputListbox.Location = Point(10, 24)
        self.lbFormatsInputListbox.Name = "lbFormatsInputListbox"
        self.lbFormatsInputListbox.Size = Size(162, 95)
        self.lbFormatsInputListbox.TabIndex = 2
        self.lbFormatsInputListbox.SelectedIndexChanged += self.lbFormatsInputListbox_SelectedIndexChanged
        # 
        # labelStatic
        # 
        self.labelStatic.Location = Point(10, 11)
        self.labelStatic.Name = "labelStatic"
        self.labelStatic.Size = Size(75, 13)
        self.labelStatic.TabIndex = 3
        self.labelStatic.Text = "Input Format:"
        # 
        # FormatsForm
        # 
        self.AcceptButton = self.buttonOk
        self.CancelButton = self.buttonCancel
        self.ClientSize = Size(183, 170)
        self.Controls.AddRange(Array[Control] ([
          self.buttonOk,
          self.buttonCancel,
          self.lbFormatsInputListbox,
          self.labelStatic]))

        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.Name = "FormatsForm"
        self.Text = "Select Capture Format"
        self.ResumeLayout(False)

    def FormatsOK(self):
        #-----------------------------------------------------------------------------
        # Name: FormatsOK()
        # Desc: Stores the capture buffer format based on what was selected
        #-----------------------------------------------------------------------------

        self.mf.InputFormat = self.formats[self.lbFormatsInputListbox.SelectedIndex].format
        self.DialogResult = DialogResult.OK
        self.Close()

    def buttonOk_Click(self, sender, e):
        self.FormatsOK()
    def buttonCancel_Click(self, sender, e):
        self.Close()

    def lbFormatsInputListbox_SelectedIndexChanged(self, sender, e):
        self.buttonOk.Enabled = True

if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    class A():
        def __init__(self):
            self._InputFormat = None
            cdc = CaptureDevicesCollection()
            
            self._applicationDevice = Capture(cdc[0].DriverGuid)

        @property 
        def applicationDevice(self): 
            return self._applicationDevice 

        @property 
        def InputFormat(self): 
            return self._InputFormat 

        @InputFormat.setter 
        def InputFormat(self, value): 
            self._InputFormat = value 
    a = A()
    frm = FormatsForm(a)
    Application.Run(frm)

    print  a.InputFormat   