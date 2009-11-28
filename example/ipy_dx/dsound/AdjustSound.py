# -*- coding: utf-8 -*-
"""
Description: DirectSound 音訊調整

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
from System.Timers import Timer as TimerControl
from System.Collections import *
from System.ComponentModel import *
from System.Windows.Forms import *
from System.Drawing import *
from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *

class EffectInfo():
    def __init__(self):
        self._description=EffectDescription()
        self._EffectSettings=None
        self._Effect=None

    @property 
    def Effect(self): 
        return self._Effect 

    @Effect.setter 
    def Effect(self, value): 
        self._Effect = value

    @property 
    def EffectSettings(self): 
        return self._EffectSettings 

    @EffectSettings.setter 
    def EffectSettings(self, value): 
        self._EffectSettings = value 

    @property 
    def description(self): 
        return self._description 

    @description.setter 
    def description(self, value): 
        self._description = value 
        
class MyForm(Form):
    def __init__(self):
        self.applicationDevice = None
        self.applicationBuffer = None
        self.path = ''
        self.fileName = ''

        self.applicationDevice = None
        self.applicationBuffer = None
        self.lastGoodFrequency = 0
        # The maximum frequency we'll allow this sample to support
        self.maxFrequency = 200000 

        self.InitializeComponent()

        try:
            #Initialize DirectSound
            self.applicationDevice = Device()
            self.applicationDevice.SetCooperativeLevel(self, CooperativeLevel.Priority)
        except:
            MessageBox.Show("Could not initialize DirectSound.  Sample will exit.", "Exiting...", MessageBoxButtons.OK, MessageBoxIcon.Error);
            self.Close();
            raise;


        # Now that we have a sound device object set the frequency sliders correctly
        self.tbarFreq.Minimum = 100
        self.tbarFreq.Maximum = self.maxFrequency
        self.lblMinFreq.Text = "{0} Hz".format(self.tbarFreq.Minimum)
        self.lblMaxFreq.Text = "{0} KHz".format(self.tbarFreq.Maximum/1000)

        self.UpdateBehaviorText()


    def InitializeComponent(self):
        self.radioDefault = RadioButton()
        self.tmrUpdate = TimerControl()
        self.checkLoop = CheckBox()
        self.textVolume = TextBox()
        self.label10 = Label()
        self.groupBox1 = GroupBox()
        self.groupBox4 = GroupBox()
        self.radioHardware = RadioButton()
        self.label12 = Label()
        self.radioSoftware = RadioButton()
        self.groupBox2 = GroupBox()
        self.radioSticky = RadioButton()
        self.label13 = Label()
        self.radioGlobal = RadioButton()
        self.radioNormal = RadioButton()
        self.textFile = TextBox()
        self.groupBox5 = GroupBox()
        self.lblBehavior = Label()
        self.buttonSound = Button()
        self.textStatus = TextBox()
        self.buttonPlay = Button()
        self.tbarPan = TrackBar()
        self.ofdFile = OpenFileDialog()
        self.buttonExit = Button()
        self.label11 = Label()
        self.tbarVolume = TrackBar()
        self.label8 = Label()
        self.label9 = Label()
        self.buttonStop = Button()
        self.lblMaxFreq = Label()
        self.label5 = Label()
        self.label6 = Label()
        self.label7 = Label()
        self.label1 = Label()
        self.label2 = Label()
        self.lblMinFreq = Label()
        self.textFreq = TextBox()
        self.tbarFreq = TrackBar()
        self.textPan = TextBox()
        self.tmrUpdate.BeginInit()
        self.groupBox1.SuspendLayout()
        self.groupBox4.SuspendLayout()
        self.groupBox2.SuspendLayout()
        self.groupBox5.SuspendLayout()
        self.tbarPan.BeginInit()
        self.tbarVolume.BeginInit()
        self.tbarFreq.BeginInit()
        self.SuspendLayout()
        # 
        # radioDefault
        # 
        self.radioDefault.Checked = True
        self.radioDefault.Location = Point(93, 16)
        self.radioDefault.Name = "radioDefault"
        self.radioDefault.Size = Size(79, 14)
        self.radioDefault.TabIndex = 3
        self.radioDefault.TabStop = True
        self.radioDefault.Text = "Default"
        self.radioDefault.CheckedChanged += self.RadioChecked
        # 
        # tmrUpdate
        # 
        self.tmrUpdate.Enabled = True
        self.tmrUpdate.SynchronizingObject = self
        self.tmrUpdate.Elapsed += self.tmrUpdate_Elapsed
        # 
        # checkLoop
        # 
        self.checkLoop.Location = Point(8, 399)
        self.checkLoop.Name = "checkLoop"
        self.checkLoop.Size = Size(151, 19)
        self.checkLoop.TabIndex = 3
        self.checkLoop.Text = "Loop Sound"
        # 
        # textVolume
        # 
        self.textVolume.Location = Point(85, 148)
        self.textVolume.Name = "textVolume"
        self.textVolume.ReadOnly = True
        self.textVolume.Size = Size(43, 20)
        self.textVolume.TabIndex = 1
        self.textVolume.Text = "0"
        # 
        # label10
        # 
        self.label10.Location = Point(6, 140)
        self.label10.Name = "label10"
        self.label10.Size = Size(73, 38)
        self.label10.TabIndex = 2
        self.label10.Text = "Volume"
        self.label10.TextAlign = ContentAlignment.MiddleCenter
        # 
        # groupBox1
        # 
        self.groupBox1.Controls.AddRange(Array[Control] ([self.groupBox4, self.groupBox2]))
        self.groupBox1.Location = Point(6, 181)
        self.groupBox1.Name = "groupBox1"
        self.groupBox1.Size = Size(437, 91)
        self.groupBox1.TabIndex = 5
        self.groupBox1.TabStop = False
        self.groupBox1.Text = "Buffer Settings"
        # 
        # groupBox4
        # 
        self.groupBox4.Controls.AddRange(Array[Control] ([
            self.radioHardware,
            self.label12,
            self.radioSoftware,
            self.radioDefault
        ]))
        self.groupBox4.Location = Point(8, 48)
        self.groupBox4.Name = "groupBox4"
        self.groupBox4.Size = Size(423, 36)
        self.groupBox4.TabIndex = 6
        self.groupBox4.TabStop = False
        # 
        # radioHardware
        # 
        self.radioHardware.Location = Point(173, 16)
        self.radioHardware.Name = "radioHardware"
        self.radioHardware.Size = Size(79, 14)
        self.radioHardware.TabIndex = 3
        self.radioHardware.Text = "Hardware"
        self.radioHardware.CheckedChanged += self.RadioChecked
        # 
        # label12
        # 
        self.label12.Location = Point(6, 13)
        self.label12.Name = "label12"
        self.label12.Size = Size(73, 15)
        self.label12.TabIndex = 2
        self.label12.Text = "Buffer Mixing"
        self.label12.TextAlign = ContentAlignment.MiddleCenter
        # 
        # radioSoftware
        # 
        self.radioSoftware.Location = Point(268, 17)
        self.radioSoftware.Name = "radioSoftware"
        self.radioSoftware.Size = Size(79, 14)
        self.radioSoftware.TabIndex = 3
        self.radioSoftware.Text = "Software"
        self.radioSoftware.CheckedChanged += self.RadioChecked
        # 
        # groupBox2
        # 
        self.groupBox2.Controls.AddRange(Array[Control] ([
            self.radioSticky,
            self.label13,
            self.radioGlobal,
            self.radioNormal
        ]))
        self.groupBox2.Location = Point(7, 11)
        self.groupBox2.Name = "groupBox2"
        self.groupBox2.Size = Size(423, 36)
        self.groupBox2.TabIndex = 6
        self.groupBox2.TabStop = False
        # 
        # radioSticky
        # 
        self.radioSticky.Location = Point(173, 16)
        self.radioSticky.Name = "radioSticky"
        self.radioSticky.Size = Size(79, 16)
        self.radioSticky.TabIndex = 3
        self.radioSticky.Text = "Sticky"
        self.radioSticky.CheckedChanged += self.RadioChecked
        # 
        # label13
        # 
        self.label13.Location = Point(6, 13)
        self.label13.Name = "label13"
        self.label13.Size = Size(73, 15)
        self.label13.TabIndex = 2
        self.label13.Text = "Focus"
        self.label13.TextAlign = ContentAlignment.MiddleCenter
        # 
        # radioGlobal
        # 
        self.radioGlobal.Location = Point(268, 17)
        self.radioGlobal.Name = "radioGlobal"
        self.radioGlobal.Size = Size(79, 14)
        self.radioGlobal.TabIndex = 3
        self.radioGlobal.Text = "Global"
        self.radioGlobal.CheckedChanged += self.RadioChecked
        # 
        # radioNormal
        # 
        self.radioNormal.Checked = True
        self.radioNormal.Location = Point(93, 16)
        self.radioNormal.Name = "radioNormal"
        self.radioNormal.Size = Size(79, 14)
        self.radioNormal.TabIndex = 3
        self.radioNormal.TabStop = True
        self.radioNormal.Text = "Normal"
        self.radioNormal.CheckedChanged += self.RadioChecked
        # 
        # textFile
        # 
        self.textFile.Location = Point(85, 6)
        self.textFile.Name = "textFile"
        self.textFile.ReadOnly = True
        self.textFile.Size = Size(350, 20)
        self.textFile.TabIndex = 1
        self.textFile.Text = ""
        # 
        # groupBox5
        # 
        self.groupBox5.Controls.AddRange(Array[Control] ([ self.lblBehavior] ))
        self.groupBox5.Location = Point(8, 278)
        self.groupBox5.Name = "groupBox5"
        self.groupBox5.Size = Size(431, 120)
        self.groupBox5.TabIndex = 6
        self.groupBox5.TabStop = False
        self.groupBox5.Text = "Expected Behavior"
        # 
        # lblBehavior
        # 
        self.lblBehavior.Location = Point(6, 16)
        self.lblBehavior.Name = "lblBehavior"
        self.lblBehavior.Size = Size(422, 100)
        self.lblBehavior.TabIndex = 0
        self.lblBehavior.TextAlign = ContentAlignment.MiddleCenter
        # 
        # buttonSound
        # 
        self.buttonSound.Location = Point(3, 6)
        self.buttonSound.Name = "buttonSound"
        self.buttonSound.Size = Size(74, 21)
        self.buttonSound.TabIndex = 0
        self.buttonSound.Text = "Sound File..."
        self.buttonSound.Click += self.buttonSound_Click
        # 
        # textStatus
        # 
        self.textStatus.Location = Point(85, 33)
        self.textStatus.Name = "textStatus"
        self.textStatus.ReadOnly = True
        self.textStatus.Size = Size(350, 20)
        self.textStatus.TabIndex = 1
        self.textStatus.Text = "No File Loaded."
        # 
        # buttonPlay
        # 
        self.buttonPlay.Enabled = False
        self.buttonPlay.Location = Point(7, 421)
        self.buttonPlay.Name = "buttonPlay"
        self.buttonPlay.Size = Size(74, 21)
        self.buttonPlay.TabIndex = 0
        self.buttonPlay.Text = "Play"
        self.buttonPlay.Click += self.buttonPlay_Click
        # 
        # tbarPan
        # 
        self.tbarPan.Location = Point(164, 97)
        self.tbarPan.Maximum = 20
        self.tbarPan.Minimum = -20
        self.tbarPan.Name = "tbarPan"
        self.tbarPan.Size = Size(236, 42)
        self.tbarPan.TabIndex = 4
        self.tbarPan.TickFrequency = 5
        self.tbarPan.Scroll += self.tbarPan_Scroll
        # 
        # ofdFile
        # 
        self.ofdFile.Filter = "Wave Files (*.wav)|*.wav|All Files (*.*)|*.*"
        self.ofdFile.Title = "Open Audio File"
        # 
        # buttonExit
        # 
        self.buttonExit.DialogResult = DialogResult.Cancel
        self.buttonExit.Location = Point(362, 421)
        self.buttonExit.Name = "buttonExit"
        self.buttonExit.Size = Size(74, 21)
        self.buttonExit.TabIndex = 0
        self.buttonExit.Text = "Exit"
        self.buttonExit.Click += self.buttonExit_Click
        # 
        # label11
        # 
        self.label11.Location = Point(6, 13)
        self.label11.Name = "label11"
        self.label11.Size = Size(73, 15)
        self.label11.TabIndex = 2
        self.label11.Text = "Focus"
        self.label11.TextAlign = ContentAlignment.MiddleCenter
        # 
        # tbarVolume
        # 
        self.tbarVolume.Location = Point(165, 140)
        self.tbarVolume.Maximum = 0
        self.tbarVolume.Minimum = -50
        self.tbarVolume.Name = "tbarVolume"
        self.tbarVolume.Size = Size(236, 42)
        self.tbarVolume.TabIndex = 4
        self.tbarVolume.Scroll += self.tbarVolume_Scroll
        # 
        # label8
        # 
        self.label8.Location = Point(131, 147)
        self.label8.Name = "label8"
        self.label8.Size = Size(41, 20)
        self.label8.TabIndex = 2
        self.label8.Text = "Low"
        self.label8.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self.label9.Location = Point(396, 149)
        self.label9.Name = "label9"
        self.label9.Size = Size(47, 20)
        self.label9.TabIndex = 2
        self.label9.Text = "High"
        self.label9.TextAlign = ContentAlignment.MiddleCenter
        # 
        # buttonStop
        # 
        self.buttonStop.Enabled = False
        self.buttonStop.Location = Point(87, 421)
        self.buttonStop.Name = "buttonStop"
        self.buttonStop.Size = Size(74, 21)
        self.buttonStop.TabIndex = 0
        self.buttonStop.Text = "Stop"
        self.buttonStop.Click += self.buttonStop_Click
        # 
        # lblMaxFreq
        # 
        self.lblMaxFreq.Location = Point(396, 68)
        self.lblMaxFreq.Name = "lblMaxFreq"
        self.lblMaxFreq.Size = Size(47, 20)
        self.lblMaxFreq.TabIndex = 2
        self.lblMaxFreq.Text = "100 KHz"
        self.lblMaxFreq.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self.label5.Location = Point(130, 104)
        self.label5.Name = "label5"
        self.label5.Size = Size(41, 20)
        self.label5.TabIndex = 2
        self.label5.Text = "Left"
        self.label5.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self.label6.Location = Point(395, 106)
        self.label6.Name = "label6"
        self.label6.Size = Size(47, 20)
        self.label6.TabIndex = 2
        self.label6.Text = "Right"
        self.label6.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self.label7.Location = Point(5, 97)
        self.label7.Name = "label7"
        self.label7.Size = Size(73, 38)
        self.label7.TabIndex = 2
        self.label7.Text = "Pan"
        self.label7.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self.label1.Location = Point(4, 33)
        self.label1.Name = "label1"
        self.label1.Size = Size(73, 20)
        self.label1.TabIndex = 2
        self.label1.Text = "Status"
        self.label1.TextAlign = ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self.label2.Location = Point(6, 59)
        self.label2.Name = "label2"
        self.label2.Size = Size(73, 38)
        self.label2.TabIndex = 2
        self.label2.Text = "Frequency"
        self.label2.TextAlign = ContentAlignment.MiddleCenter
        # 
        # lblMinFreq
        # 
        self.lblMinFreq.Location = Point(131, 66)
        self.lblMinFreq.Name = "lblMinFreq"
        self.lblMinFreq.Size = Size(41, 20)
        self.lblMinFreq.TabIndex = 2
        self.lblMinFreq.Text = "100 Hz"
        self.lblMinFreq.TextAlign = ContentAlignment.MiddleCenter
        # 
        # textFreq
        # 
        self.textFreq.Location = Point(85, 67)
        self.textFreq.Name = "textFreq"
        self.textFreq.ReadOnly = True
        self.textFreq.Size = Size(43, 20)
        self.textFreq.TabIndex = 1
        self.textFreq.Text = "0"
        # 
        # tbarFreq
        # 
        self.tbarFreq.LargeChange = 1000
        self.tbarFreq.Location = Point(165, 59)
        self.tbarFreq.Maximum = 100000
        self.tbarFreq.Minimum = 100
        self.tbarFreq.Name = "tbarFreq"
        self.tbarFreq.Size = Size(236, 42)
        self.tbarFreq.SmallChange = 100
        self.tbarFreq.TabIndex = 4
        self.tbarFreq.TickFrequency = 10000
        self.tbarFreq.Value = 100
        self.tbarFreq.Scroll += self.tbarFreq_Scroll
        # 
        # textPan
        # 
        self.textPan.Location = Point(85, 105)
        self.textPan.Name = "textPan"
        self.textPan.ReadOnly = True
        self.textPan.Size = Size(43, 20)
        self.textPan.TabIndex = 1
        self.textPan.Text = "0"
        # 
        # wfAdjust
        # 
        self.AcceptButton = self.buttonSound
        self.CancelButton = self.buttonExit
        self.ClientSize = Size(460, 448)
        self.Controls.AddRange(Array[Control] ([
          self.groupBox5,
          self.groupBox1,
          self.textVolume,
          self.label8,
          self.label9,
          self.label10,
          self.tbarVolume,
          self.label5,
          self.label6,
          self.tbarPan,
          self.textPan,
          self.label7,
          self.lblMaxFreq,
          self.lblMinFreq,
          self.textFreq,
          self.tbarFreq,
          self.label2,
          self.checkLoop,
          self.buttonStop,
          self.buttonPlay,
          self.buttonExit,
          self.label1,
          self.textStatus,
          self.textFile,
          self.buttonSound
        ]))
        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.MaximizeBox = False
        self.Name = "wfAdjust"
        self.Text = "AdjustSound"
        self.tmrUpdate.EndInit()
        self.groupBox1.ResumeLayout(False)
        self.groupBox4.ResumeLayout(False)
        self.groupBox2.ResumeLayout(False)
        self.groupBox5.ResumeLayout(False)
        self.tbarPan.EndInit()
        self.tbarVolume.EndInit()
        self.tbarFreq.EndInit()
        self.ResumeLayout(False)

    def UpdateBehaviorText(self):
        sText = None
        Looped      = self.checkLoop.Checked
        FocusSticky = self.radioSticky.Checked
        FocusGlobal = self.radioGlobal.Checked
        MixHardware = self.radioHardware.Checked
        MixSoftware = self.radioSoftware.Checked

        # Figure what the user should expect based on the dialog choice
        if (FocusSticky):
            sText = "Buffers with \"sticky\" focus will continue to play if the user switches to another application not using DirectSound.  However, if the user switches to another DirectSound application, all normal-focus and sticky-focus buffers in the previous application are muted."
        elif (FocusGlobal):
            sText = "Buffers with global focus will continue to play if the user switches focus to another application, even if the new application uses DirectSound. The one exception is if you switch focus to a DirectSound application that uses the DSSCL_WRITEPRIMARY cooperative level. In this case, the global-focus buffers from other applications will not be audible."
        else:
            # Normal focus
            sText = "Buffers with normal focus will mute if the user switches focus to any other application"

        if (MixHardware):
            sText = sText + "\n\nWith the hardware mixing flag, the new buffer will be forced to use hardware mixing. If the device does not support hardware mixing or if the required hardware resources are not available, the call to the DirectSound.CreateSoundBuffer method will fail." 

        elif (MixSoftware):
            sText = sText + "\n\nWith the software mixing flag, the new buffer will use software mixing, even if hardware resources are available."

        else :
            # Default mixing
            sText = sText + "\n\nWith default mixing, the new buffer will use hardware mixing if available, otherwise software mixing will be used." 

        self.lblBehavior.Text = sText

    def EnablePlayUI(self,bEnable):
        self.buttonPlay.Enabled = bEnable
        self.buttonStop.Enabled = not bEnable
        self.buttonSound.Enabled = bEnable
        self.checkLoop.Enabled = bEnable
        self.radioDefault.Enabled = bEnable
        self.radioGlobal.Enabled = bEnable
        self.radioHardware.Enabled = bEnable
        self.radioNormal.Enabled = bEnable
        self.radioSoftware.Enabled = bEnable
        self.radioSticky.Enabled = bEnable

    def DefaultPlayUI(self):
        self.buttonPlay.Enabled = False
        self.buttonStop.Enabled = False
        self.buttonSound.Enabled = True
        self.checkLoop.Enabled = False
        self.radioDefault.Enabled = True
        self.radioGlobal.Enabled = True
        self.radioHardware.Enabled = True
        self.radioNormal.Enabled = True
        self.radioSoftware.Enabled = True
        self.radioSticky.Enabled = True
        self.textFile.Text = None

    def buttonExit_Click(self, sender, e):
        self.Dispose()


    def buttonSound_Click(self, sender, e):
        FocusSticky = self.radioSticky.Checked
        FocusGlobal = self.radioGlobal.Checked
        MixHardware = self.radioHardware.Checked
        MixSoftware = self.radioSoftware.Checked

        # Make sure we're stopped
        self.buttonStop_Click(None, None)
        self.textStatus.Text = "Loading file..."
        if (None != self.applicationBuffer):
            self.applicationBuffer.Dispose()
        self.applicationBuffer = None

        self.tbarFreq.Value = self.tbarFreq.Minimum
        self.tbarPan.Value = 0
        self.tbarVolume.Value = 0

        # Show the open file dialog and let's load the file
        if (None == self.ofdFile.InitialDirectory):

            # Default to the 'My documents' folder if it's available
            self.ofdFile.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.Personal)

        # Clear out any old file name that may be in there
        self.ofdFile.FileName = None
        if (DialogResult.OK == self.ofdFile.ShowDialog()):
            # Save the initial dir as the last one picked.
            self.ofdFile.InitialDirectory = Path.GetDirectoryName(self.ofdFile.FileName)
            try:
                desc = BufferDescription()
                
                desc.ControlFrequency  = True
                desc.ControlPan = True
                desc.ControlVolume = True

                if (FocusGlobal):
                    desc.GlobalFocus = True

                if (FocusSticky):
                    desc.StickyFocus = True

                if (MixHardware):
                    desc.LocateInHardware = True

                if (MixSoftware):
                    desc.LocateInSoftware = True

                self.applicationBuffer = SecondaryBuffer(self.ofdFile.FileName, desc, self.applicationDevice)
                self.tbarFreq.Value = desc.Format.SamplesPerSecond
                lastGoodFrequency = desc.Format.SamplesPerSecond
                self.textFile.Text = self.ofdFile.FileName
                self.textFreq.Text = self.tbarFreq.Value.ToString()
                self.textStatus.Text = "File loaded."
                self.EnablePlayUI(True)
            except:
                #Console.WriteLine(de.ToString())
                self.textFile.Text = None
                self.textStatus.Text = "Could not load this segment."
                self.DefaultPlayUI()

        else:
            self.textFile.Text = None
            self.textStatus.Text = "Load aborted."
            self.DefaultPlayUI()



    def buttonStop_Click(self, sender, e):
       if (not None is self.applicationBuffer):
            self.textStatus.Text = "Sound stopped."
            self.EnablePlayUI(True)
            self.applicationBuffer.Stop()
            self.applicationBuffer.SetCurrentPosition(0)

    def tbarFreq_Scroll(self, sender, e):
        newFrequency = 0
        if (not None is self.applicationBuffer):
            try:
                newFrequency = sender.Value
                # Attempt to set the frequency to the new value
                self.applicationBuffer.Frequency = newFrequency
                self.textFreq.Text = newFrequency.ToString()
                lastGoodFrequency = newFrequency
            except:
                # Let's try to guess why it failed..
                if ((self.applicationBuffer.Caps.LocateInHardware) and (newFrequency > applicationDevice.Caps.MaxSecondarySampleRate)):
                    self.textStatus.Text = "Hardware buffers don't support greater than Caps.MaxSecondarySampleRate"
                elif (100000 < newFrequency):
                    # Some platforms (pre-WinXP SP1) don't support 
                    # >100k Hz so they will fail when setting it higher
                    self.textStatus.Text = "Some OS platforms do not support >100k Hz"
                else:
                    self.textStatus.Text = "Setting the frequency failed"

                # Reset to the last valid frequency
                self.applicationBuffer.Frequency = lastGoodFrequency
                sender.Value = lastGoodFrequency

    def buttonPlay_Click(self, sender, e):
        FocusSticky = self.radioSticky.Checked
        FocusGlobal = self.radioGlobal.Checked
        MixHardware = self.radioHardware.Checked
        MixSoftware = self.radioSoftware.Checked

        if (not None is self.applicationBuffer):
            self.textStatus.Text = "Sound playing."
            self.EnablePlayUI(False)
            Application.DoEvents() # Process the Stop click that EnablePlayUI generates.

            # First we need to 'recreate' the buffer
            if (not None is self.applicationBuffer):
                self.applicationBuffer.Dispose()
            self.applicationBuffer = None

            desc = BufferDescription()
            desc.ControlFrequency  = True
            desc.ControlPan = True
            desc.ControlVolume = True

            if (FocusGlobal):
                desc.GlobalFocus = True

            if (FocusSticky):
                desc.StickyFocus = True

            if (MixHardware):
                desc.LocateInHardware = True

            if (MixSoftware):
                desc.LocateInSoftware = True

            try:
                print '#1'
                self.applicationBuffer = SecondaryBuffer(self.ofdFile.FileName, desc, self.applicationDevice)
                print '#2'
                PlayFlags  = BufferPlayFlags.Looping if self.checkLoop.Checked else 0
                print '#3'
                # Before we play, make sure we're using the correct settings
                self.tbarFreq_Scroll(self.tbarFreq, None)
                self.tbarPan_Scroll(self.tbarPan, None)
                self.tbarVolume_Scroll(self.tbarVolume, None)
                self.applicationBuffer.Play(0, PlayFlags)
            except:
                self.textStatus.Text = "Could not open this file with these settings."
                self.DefaultPlayUI()




    def tbarPan_Scroll(self, sender, e):
       if (not None is self.applicationBuffer):
            self.textPan.Text = sender.Value.ToString()
            self.applicationBuffer.Pan = sender.Value * 500

    def tbarVolume_Scroll(self, sender, e):
        if (not None is self.applicationBuffer):
            self.textVolume.Text = sender.Value.ToString()
            self.applicationBuffer.Volume = sender.Value * 100

    def tmrUpdate_Elapsed(self, sender, e):
        if (not None is self.applicationBuffer):
            if (False == self.applicationBuffer.Status.Playing and False == self.applicationBuffer.Status.Looping):
                self.buttonStop_Click(None, None)

    def RadioChecked(self, sender, e):
        self.UpdateBehaviorText()
if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = MyForm()
    Application.Run(frm)