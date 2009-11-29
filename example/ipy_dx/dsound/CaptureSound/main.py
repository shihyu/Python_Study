# -*- coding: utf-8 -*-
"""
Description: DirectSound 特效測試

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
from System.Threading import *

from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *

import devices as D
import formats as F
        
class MainForm(Form):
    def __init__(self):
        self.applicationDevice = None
        self._InputFormat = None
        self.applicationNotify = None
        self.applicationBuffer = None
        self.NumberRecordNotifications = 16
        self.PositionNotify = []
        self.NotificationEvent=None
        self.CaptureDeviceGuid = None
        self.FileName = ''
        self.NotifyThread = None
        self.WaveFile = None
        self.Writer = None
        self.Path = ''
        self.CaptureBufferSize =0
        self.NextCaptureOffset =0
        self.Recording = False
        self.SampleCount = 0
        self.NotifySize = 0
        self.Capturing = False

        self.InitializeComponent()
        devices = D.DevicesForm(self)
        devices.ShowDialog(self)

        self.InitDirectSound()        

        if (None == self.applicationDevice):
            self.Close()
        else:
            formats = F.FormatsForm(self)
            if (formats.ShowDialog(self) == DialogResult.OK):		
                self.labelMainInputformatText.Text = "{0} Hz, {1}-bit {2}".format( self.InputFormat.SamplesPerSecond, \
                    self.InputFormat.BitsPerSample,\
                    ("Mono" if (1 == self.InputFormat.Channels) else "Stereo"))

                self.CreateCaptureBuffer()
            
            else:
                self.Close()

    @property 
    def InputFormat(self): 
        return self._InputFormat 

    @InputFormat.setter 
    def InputFormat(self, value): 
        self._InputFormat = value 
    def InitDirectSound(self):
        self.CaptureBufferSize = 0
        self.NotifySize = 0

        # Create DirectSound.Capture using the preferred capture device
        try:
            self.applicationDevice = Capture(self.CaptureDeviceGuid)		
        except: 
            pass

    def CreateCaptureBuffer(self):
        #-----------------------------------------------------------------------------
		# Name: CreateCaptureBuffer()
		# Desc: Creates a capture buffer and sets the format 
		#-----------------------------------------------------------------------------
		dscheckboxd = CaptureBufferDescription() 

		if (not None is self.applicationNotify):
			self.applicationNotify.Dispose()
			self.applicationNotify = None

		if (not None is self.applicationBuffer):
			self.applicationBuffer.Dispose()
			self.applicationBuffer = None

		if (0 == self.InputFormat.Channels):
			return

		# Set the notif:ication size
		self.NotifySize = 1024 if (1024 > self.InputFormat.AverageBytesPerSecond / 8) else (self.InputFormat.AverageBytesPerSecond / 8)
		self.NotifySize -= self.NotifySize % self.InputFormat.BlockAlign   

		# Set the buffer sizes
		self.CaptureBufferSize = self.NotifySize * self.NumberRecordNotifications

		# Create the capture buffer
		dscheckboxd.BufferBytes = self.CaptureBufferSize
		self.InputFormat.FormatTag = WaveFormatTag.Pcm
		dscheckboxd.Format = self.InputFormat # Set the format during creatation
		
		applicationBuffer = CaptureBuffer(dscheckboxd, self.applicationDevice)
		self.NextCaptureOffset = 0

		self.InitNotifications()

    def WaitThread(self):
        while(self.Capturing):
            #Sit here and wait for a message to arrive
            self.NotificationEvent.WaitOne(Timeout.Infinite, true);
            self.RecordCapturedData();

    def InitNotifications(self):
        #-----------------------------------------------------------------------------
        # Name: InitNotifications()
        # Desc: Inits the notifications on the capture buffer which are handled
        #       in the notify thread.
        #-----------------------------------------------------------------------------

        if (None is self.applicationBuffer):
            raise NullReferenceException()

        # Create a thread to monitor the notify events
        if (None == self.NotifyThread):
            self.NotifyThread = Thread(ThreadStart(self.WaitThread))
            self.Capturing = True
            self.NotifyThread.Start()

            # Create a notification event, for when the sound stops playing
            self.NotificationEvent = AutoResetEvent(False)



        # Setup the notification positions
        for i in range( NumberRecordNotifications):
            self.PositionNotify[i].Offset = (self.NotifySize * i) + self.NotifySize - 1
            self.PositionNotify[i].EventNotifyHandle = self.NotificationEvent.Handle


        self.applicationNotify = Notify(self.applicationBuffer)

        # Tell DirectSound when to notify the app. The notification will come in the from 
        # of signaled events that are handled in the notify thread.
        self.applicationNotify.SetNotificationPositions(self.PositionNotify, self.NumberRecordNotifications)

    def InitializeComponent(self):
        self.labelStatic = Label()
        self.labelMainInputformatText = Label()
        self.checkboxRecord = CheckBox()
        self.buttonSoundfile = Button()
        self.labelFilename = Label()
        self.SuspendLayout()
        # 
        # labelStatic
        # 
        self.labelStatic.Location = Point(10, 46)
        self.labelStatic.Name = "labelStatic"
        self.labelStatic.Size = Size(75, 13)
        self.labelStatic.TabIndex = 0
        self.labelStatic.Text = "Input Format:"
        # 
        # labelMainInputformatText
        # 
        self.labelMainInputformatText.Location = Point(90, 46)
        self.labelMainInputformatText.Name = "labelMainInputformatText"
        self.labelMainInputformatText.Size = Size(262, 13)
        self.labelMainInputformatText.TabIndex = 1
        # 
        # checkboxRecord
        # 
        self.checkboxRecord.Appearance = Appearance.Button
        self.checkboxRecord.Enabled = False
        self.checkboxRecord.FlatStyle = FlatStyle.System
        self.checkboxRecord.Location = Point(369, 40)
        self.checkboxRecord.Name = "checkboxRecord"
        self.checkboxRecord.Size = Size(75, 23)
        self.checkboxRecord.TabIndex = 2
        self.checkboxRecord.Text = "&Record"
        self.checkboxRecord.CheckedChanged += self.checkboxRecord_CheckedChanged
        # 
        # buttonSoundfile
        # 
        self.buttonSoundfile.Location = Point(10, 11)
        self.buttonSoundfile.Name = "buttonSoundfile"
        self.buttonSoundfile.Size = Size(78, 21)
        self.buttonSoundfile.TabIndex = 3
        self.buttonSoundfile.Text = "Sound &file..."
        self.buttonSoundfile.Click += self.buttonSoundfile_Click
        # 
        # labelFilename
        # 
        self.labelFilename.BorderStyle = BorderStyle.Fixed3D
        self.labelFilename.Location = Point(96, 11)
        self.labelFilename.Name = "labelFilename"
        self.labelFilename.Size = Size(348, 21)
        self.labelFilename.TabIndex = 4
        self.labelFilename.Text = "No file loaded."
        self.labelFilename.TextAlign = ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.AcceptButton = self.buttonSoundfile
        self.ClientSize = Size(454, 77)
        self.Controls.AddRange(Array[Control] ([
          self.labelStatic,
          self.labelMainInputformatText,
          self.checkboxRecord,
          self.buttonSoundfile,
          self.labelFilename]))

        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.Name = "MainForm"
        self.Text = "CaptureSound"
        self.Closing += CancelEventHandler(self.MainForm_Closing)
        self.ResumeLayout(False)

    def checkboxRecord_CheckedChanged(self, sender, e):
        pass


    def buttonSoundfile_Click(self, sender, e):
        pass


    def MainForm_Closing(self, sender, e):
        pass    
    def RecordCapturedData(self):
        pass




if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = MainForm()
    Application.Run(frm)