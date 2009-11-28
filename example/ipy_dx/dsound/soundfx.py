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
        #self.effectDescription = ArrayList()
        self.effectDescription = []
        self.shouldLoop = False
        self.isIgnoringSettings = False
        self.currentIndex = 0
        self.InitializeComponent()
        self.InitDirectSound()
        self.ClearUI(True)

    def InitDirectSound(self):
        description = BufferDescription()
        wfx = WaveFormat()
        try:
            self.applicationDevice = Device()
            self.applicationDevice.SetCooperativeLevel(self, CooperativeLevel.Priority)
        except:
            MessageBox.Show("Unable to create sound device. Sample will now exit.")
            self.Close()
            raise

    def ClearUI(self, ClearControls):
        self.labelParamName1.Text =\
        self.labelParamValue1.Text =\
        self.labelParamName2.Text =\
        self.labelParamValue2.Text =\
        self.labelParamName3.Text =\
        self.labelParamValue3.Text =\
        self.labelParamName4.Text =\
        self.labelParamValue4.Text =\
        self.labelParamName5.Text =\
        self.labelParamValue5.Text =\
        self.labelParamName6.Text =\
        self.labelParamValue6.Text = ''

        if (ClearControls):
            self.groupboxFrameWaveform.Enabled =\
            self.radiobuttonTriangle.Enabled =\
            self.radiobuttonTriangle.Enabled =\
            self.radiobuttonRadioSine.Enabled =\
            self.groupboxFramePhase.Enabled =\
            self.radiobuttonRadioNeg180.Enabled =\
            self.radiobuttonRadioNeg90.Enabled =\
            self.radiobuttonRadioZero.Enabled =\
            self.radiobuttonRadio90.Enabled =\
            self.radiobuttonRadio180.Enabled = False

            self.trackbarSlider1.Minimum =\
            self.trackbarSlider2.Minimum =\
            self.trackbarSlider3.Minimum =\
            self.trackbarSlider4.Minimum =\
            self.trackbarSlider5.Minimum =\
            self.trackbarSlider6.Minimum = 0

            self.trackbarSlider1.Value =\
            self.trackbarSlider2.Value =\
            self.trackbarSlider3.Value =\
            self.trackbarSlider4.Value =\
            self.trackbarSlider5.Value =\
            self.trackbarSlider6.Value = 0

            self.trackbarSlider1.Enabled =\
            self.trackbarSlider2.Enabled =\
            self.trackbarSlider3.Enabled =\
            self.trackbarSlider4.Enabled =\
            self.trackbarSlider5.Enabled =\
            self.trackbarSlider6.Enabled = False


    def _Form1_Load(self, sender, e):
        try:
            self.ApplicationDevice = Device()
            self.ApplicationDevice.SetCooperativeLevel(self, CooperativeLevel.Priority)
        except:
            MessageBox.Show("Unable to create sound device. Sample will now exit.")
            self.Close()

    def Dispose(self, disposing):              
        if (disposing):

            if (not self.applicationBuffer is None):
                self.applicationBuffer.Dispose()
            if (not self.applicationDevice is None):
                self.applicationDevice.Dispose()


        super(type(self), self).Dispose(disposing)    

    def InitializeComponent(self):
    	self.components = Container()
        self.buttonOk = Button()
        self.groupboxFrame = GroupBox()
        self.labelParamName1 = Label()
        self.labelParamValue1 = Label()
        self.trackbarSlider1 = TrackBar()
        self.labelParamMin1 = Label()
        self.labelParamMax1 = Label()
        self.labelParamName2 = Label()
        self.labelParamValue2 = Label()
        self.trackbarSlider2 = TrackBar()
        self.labelParamMin2 = Label()
        self.labelParamMax2 = Label()
        self.labelParamName3 = Label()
        self.labelParamValue3 = Label()
        self.trackbarSlider3 = TrackBar()
        self.labelParamMin3 = Label()
        self.labelParamMax3 = Label()
        self.labelParamName4 = Label()
        self.labelParamValue4 = Label()
        self.trackbarSlider4 = TrackBar()
        self.labelParamMin4 = Label()
        self.labelParamMax4 = Label()
        self.labelParamName5 = Label()
        self.labelParamValue5 = Label()
        self.trackbarSlider5 = TrackBar()
        self.labelParamMin5 = Label()
        self.labelParamMax5 = Label()
        self.labelParamName6 = Label()
        self.labelParamValue6 = Label()
        self.trackbarSlider6 = TrackBar()
        self.labelParamMin6 = Label()
        self.labelParamMax6 = Label()
        self.radiobuttonTriangle = RadioButton()
        self.radiobuttonSquare = RadioButton()
        self.radiobuttonRadioSine = RadioButton()
        self.groupboxFrameWaveform = GroupBox()
        self.buttonOpen = Button()
        self.labelTextFilename = Label()
        self.labelStatic2 = Label()
        self.labelTextStatus = Label()
        self.checkboxLoop = CheckBox()
        self.buttonPlay = Button()
        self.buttonStop = Button()
        self.labelStatic3 = Label()
        self.labelStatic4 = Label()
        self.radiobuttonRadioNeg180 = RadioButton()
        self.radiobuttonRadioNeg90 = RadioButton()
        self.radiobuttonRadioZero = RadioButton()
        self.radiobuttonRadio90 = RadioButton()
        self.radiobuttonRadio180 = RadioButton()
        self.groupboxFramePhase = GroupBox()
        self.groupboxEffects = GroupBox()
        self.buttonDelete = Button()
        self.listboxEffects = ListBox()
        self.comboEffects = ComboBox()
        self.timer1 = Timer(self.components)
        self.trackbarSlider1.BeginInit()
        self.trackbarSlider2.BeginInit()
        self.trackbarSlider3.BeginInit()
        self.trackbarSlider4.BeginInit()
        self.trackbarSlider5.BeginInit()
        self.trackbarSlider6.BeginInit()
        self.groupboxFrameWaveform.SuspendLayout()
        self.groupboxFramePhase.SuspendLayout()
        self.groupboxEffects.SuspendLayout()
        self.SuspendLayout()

	# 
        # buttonOk
        # 
        self.buttonOk.Location = Point(87, 432)
        self.buttonOk.Name = "buttonOk"
        self.buttonOk.Size = Size(67, 23)
        self.buttonOk.TabIndex = 0
        self.buttonOk.Text = "E&xit"
        self.buttonOk.Click += self.buttonOk_Click
        # 
        # groupboxFrame
        # 
        self.groupboxFrame.Location = Point(165, 76)
        self.groupboxFrame.Name = "groupboxFrame"
        self.groupboxFrame.Size = Size(525, 380)
        self.groupboxFrame.TabIndex = 1
        self.groupboxFrame.TabStop = False
        self.groupboxFrame.Text = "Parameters"
        # 
        # labelParamName1
        # 
        self.labelParamName1.Location = Point(169, 112)
        self.labelParamName1.Name = "labelParamName1"
        self.labelParamName1.Size = Size(117, 13)
        self.labelParamName1.TabIndex = 2
        self.labelParamName1.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue1
        # 
        self.labelParamValue1.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue1.Location = Point(294, 112)
        self.labelParamValue1.Name = "labelParamValue1"
        self.labelParamValue1.Size = Size(67, 16)
        self.labelParamValue1.TabIndex = 3
        self.labelParamValue1.Text = "Value"
        self.labelParamValue1.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider1
        # 
        self.trackbarSlider1.Location = Point(426, 112)
        self.trackbarSlider1.Name = "trackbarSlider1"
        self.trackbarSlider1.Size = Size(195, 45)
        self.trackbarSlider1.TabIndex = 4
        self.trackbarSlider1.Text = "Slider1"
        self.trackbarSlider1.TickStyle = TickStyle.None
        self.trackbarSlider1.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin1
        # 
        self.labelParamMin1.Location = Point(366, 112)
        self.labelParamMin1.Name = "labelParamMin1"
        self.labelParamMin1.Size = Size(60, 16)
        self.labelParamMin1.TabIndex = 5
        self.labelParamMin1.Text = "min"
        self.labelParamMin1.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax1
        # 
        self.labelParamMax1.Location = Point(627, 120)
        self.labelParamMax1.Name = "labelParamMax1"
        self.labelParamMax1.Size = Size(52, 13)
        self.labelParamMax1.TabIndex = 6
        self.labelParamMax1.Text = "max"
        self.labelParamMax1.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamName2
        # 
        self.labelParamName2.Location = Point(169, 160)
        self.labelParamName2.Name = "labelParamName2"
        self.labelParamName2.Size = Size(117, 13)
        self.labelParamName2.TabIndex = 7
        self.labelParamName2.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue2
        # 
        self.labelParamValue2.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue2.Location = Point(294, 160)
        self.labelParamValue2.Name = "labelParamValue2"
        self.labelParamValue2.Size = Size(67, 16)
        self.labelParamValue2.TabIndex = 8
        self.labelParamValue2.Text = "Value"
        self.labelParamValue2.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider2
        # 
        self.trackbarSlider2.Location = Point(426, 163)
        self.trackbarSlider2.Name = "trackbarSlider2"
        self.trackbarSlider2.Size = Size(195, 45)
        self.trackbarSlider2.TabIndex = 9
        self.trackbarSlider2.Text = "Slider1"
        self.trackbarSlider2.TickStyle = TickStyle.None
        self.trackbarSlider2.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin2
        # 
        self.labelParamMin2.Location = Point(366, 160)
        self.labelParamMin2.Name = "labelParamMin2"
        self.labelParamMin2.Size = Size(60, 16)
        self.labelParamMin2.TabIndex = 10
        self.labelParamMin2.Text = "min"
        self.labelParamMin2.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax2
        # 
        self.labelParamMax2.Location = Point(627, 168)
        self.labelParamMax2.Name = "labelParamMax2"
        self.labelParamMax2.Size = Size(52, 13)
        self.labelParamMax2.TabIndex = 11
        self.labelParamMax2.Text = "max"
        self.labelParamMax2.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamName3
        # 
        self.labelParamName3.Location = Point(169, 208)
        self.labelParamName3.Name = "labelParamName3"
        self.labelParamName3.Size = Size(117, 13)
        self.labelParamName3.TabIndex = 12
        self.labelParamName3.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue3
        # 
        self.labelParamValue3.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue3.Location = Point(294, 208)
        self.labelParamValue3.Name = "labelParamValue3"
        self.labelParamValue3.Size = Size(67, 16)
        self.labelParamValue3.TabIndex = 13
        self.labelParamValue3.Text = "Value"
        self.labelParamValue3.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider3
        # 
        self.trackbarSlider3.Location = Point(426, 208)
        self.trackbarSlider3.Name = "trackbarSlider3"
        self.trackbarSlider3.Size = Size(195, 45)
        self.trackbarSlider3.TabIndex = 14
        self.trackbarSlider3.Text = "Slider1"
        self.trackbarSlider3.TickStyle = TickStyle.None
        self.trackbarSlider3.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin3
        # 
        self.labelParamMin3.Location = Point(366, 208)
        self.labelParamMin3.Name = "labelParamMin3"
        self.labelParamMin3.Size = Size(60, 16)
        self.labelParamMin3.TabIndex = 15
        self.labelParamMin3.Text = "min"
        self.labelParamMin3.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax3
        # 
        self.labelParamMax3.Location = Point(627, 216)
        self.labelParamMax3.Name = "labelParamMax3"
        self.labelParamMax3.Size = Size(52, 13)
        self.labelParamMax3.TabIndex = 16
        self.labelParamMax3.Text = "max"
        self.labelParamMax3.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamName4
        # 
        self.labelParamName4.Location = Point(169, 256)
        self.labelParamName4.Name = "labelParamName4"
        self.labelParamName4.Size = Size(117, 13)
        self.labelParamName4.TabIndex = 17
        self.labelParamName4.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue4
        # 
        self.labelParamValue4.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue4.Location = Point(294, 256)
        self.labelParamValue4.Name = "labelParamValue4"
        self.labelParamValue4.Size = Size(67, 16)
        self.labelParamValue4.TabIndex = 18
        self.labelParamValue4.Text = "Value"
        self.labelParamValue4.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider4
        # 
        self.trackbarSlider4.Location = Point(426, 256)
        self.trackbarSlider4.Name = "trackbarSlider4"
        self.trackbarSlider4.Size = Size(195, 45)
        self.trackbarSlider4.TabIndex = 19
        self.trackbarSlider4.Text = "Slider1"
        self.trackbarSlider4.TickStyle = TickStyle.None
        self.trackbarSlider4.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin4
        # 
        self.labelParamMin4.Location = Point(366, 256)
        self.labelParamMin4.Name = "labelParamMin4"
        self.labelParamMin4.Size = Size(60, 16)
        self.labelParamMin4.TabIndex = 20
        self.labelParamMin4.Text = "min"
        self.labelParamMin4.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax4
        # 
        self.labelParamMax4.Location = Point(627, 256)
        self.labelParamMax4.Name = "labelParamMax4"
        self.labelParamMax4.Size = Size(52, 13)
        self.labelParamMax4.TabIndex = 21
        self.labelParamMax4.Text = "max"
        self.labelParamMax4.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamName5
        # 
        self.labelParamName5.Location = Point(169, 304)
        self.labelParamName5.Name = "labelParamName5"
        self.labelParamName5.Size = Size(117, 13)
        self.labelParamName5.TabIndex = 22
        self.labelParamName5.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue5
        # 
        self.labelParamValue5.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue5.Location = Point(294, 304)
        self.labelParamValue5.Name = "labelParamValue5"
        self.labelParamValue5.Size = Size(67, 16)
        self.labelParamValue5.TabIndex = 23
        self.labelParamValue5.Text = "Value"
        self.labelParamValue5.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider5
        # 
        self.trackbarSlider5.Location = Point(426, 304)
        self.trackbarSlider5.Name = "trackbarSlider5"
        self.trackbarSlider5.Size = Size(195, 45)
        self.trackbarSlider5.TabIndex = 24
        self.trackbarSlider5.Text = "Slider1"
        self.trackbarSlider5.TickStyle = TickStyle.None
        self.trackbarSlider5.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin5
        # 
        self.labelParamMin5.Location = Point(366, 304)
        self.labelParamMin5.Name = "labelParamMin5"
        self.labelParamMin5.Size = Size(60, 16)
        self.labelParamMin5.TabIndex = 25
        self.labelParamMin5.Text = "min"
        self.labelParamMin5.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax5
        # 
        self.labelParamMax5.Location = Point(627, 312)
        self.labelParamMax5.Name = "labelParamMax5"
        self.labelParamMax5.Size = Size(52, 13)
        self.labelParamMax5.TabIndex = 26
        self.labelParamMax5.Text = "max"
        self.labelParamMax5.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamName6
        # 
        self.labelParamName6.Location = Point(169, 352)
        self.labelParamName6.Name = "labelParamName6"
        self.labelParamName6.Size = Size(117, 13)
        self.labelParamName6.TabIndex = 27
        self.labelParamName6.TextAlign = ContentAlignment.TopRight
        # 
        # labelParamValue6
        # 
        self.labelParamValue6.BorderStyle = BorderStyle.Fixed3D
        self.labelParamValue6.Location = Point(294, 352)
        self.labelParamValue6.Name = "labelParamValue6"
        self.labelParamValue6.Size = Size(67, 16)
        self.labelParamValue6.TabIndex = 28
        self.labelParamValue6.Text = "Value"
        self.labelParamValue6.TextAlign = ContentAlignment.TopCenter
        # 
        # trackbarSlider6
        # 
        self.trackbarSlider6.Location = Point(426, 352)
        self.trackbarSlider6.Name = "trackbarSlider6"
        self.trackbarSlider6.Size = Size(195, 45)
        self.trackbarSlider6.TabIndex = 29
        self.trackbarSlider6.Text = "Slider1"
        self.trackbarSlider6.TickStyle = TickStyle.None
        self.trackbarSlider6.Scroll += self.trackbarSliderScroll
        # 
        # labelParamMin6
        # 
        self.labelParamMin6.Location = Point(366, 352)
        self.labelParamMin6.Name = "labelParamMin6"
        self.labelParamMin6.Size = Size(60, 16)
        self.labelParamMin6.TabIndex = 30
        self.labelParamMin6.Text = "min"
        self.labelParamMin6.TextAlign = ContentAlignment.TopCenter
        # 
        # labelParamMax6
        # 
        self.labelParamMax6.Location = Point(627, 352)
        self.labelParamMax6.Name = "labelParamMax6"
        self.labelParamMax6.Size = Size(52, 13)
        self.labelParamMax6.TabIndex = 31
        self.labelParamMax6.Text = "max"
        self.labelParamMax6.TextAlign = ContentAlignment.TopCenter
        # 
        # radiobuttonTriangle
        # 
        self.radiobuttonTriangle.Location = Point(16, 16)
        self.radiobuttonTriangle.Name = "radiobuttonTriangle"
        self.radiobuttonTriangle.Size = Size(69, 16)
        self.radiobuttonTriangle.TabIndex = 32
        self.radiobuttonTriangle.Text = "Triangle"
        self.radiobuttonTriangle.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonSquare
        # 
        self.radiobuttonSquare.Location = Point(88, 16)
        self.radiobuttonSquare.Name = "radiobuttonSquare"
        self.radiobuttonSquare.Size = Size(64, 16)
        self.radiobuttonSquare.TabIndex = 33
        self.radiobuttonSquare.Text = "Square"
        self.radiobuttonSquare.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadioSine
        # 
        self.radiobuttonRadioSine.Location = Point(152, 16)
        self.radiobuttonRadioSine.Name = "radiobuttonRadioSine"
        self.radiobuttonRadioSine.Size = Size(48, 16)
        self.radiobuttonRadioSine.TabIndex = 34
        self.radiobuttonRadioSine.Text = "Sine"
        self.radiobuttonRadioSine.CheckedChanged += self.trackbarSliderScroll

	# 
        # buttonOpen
        # 
        self.buttonOpen.Location = Point(12, 12)
        self.buttonOpen.Name = "buttonOpen"
        self.buttonOpen.TabIndex = 47
        self.buttonOpen.Text = "&Open File"
        self.buttonOpen.Click += self.buttonOpen_Click
        # 
        # labelTextFilename
        # 
        self.labelTextFilename.BorderStyle = BorderStyle.Fixed3D
        self.labelTextFilename.Location = Point(94, 14)
        self.labelTextFilename.Name = "labelTextFilename"
        self.labelTextFilename.Size = Size(595, 20)
        self.labelTextFilename.TabIndex = 48
        self.labelTextFilename.Text = "Filename"
        self.labelTextFilename.TextAlign = ContentAlignment.MiddleLeft
        # 
        # labelStatic2
        # 
        self.labelStatic2.Location = Point(19, 44)
        self.labelStatic2.Name = "labelStatic2"
        self.labelStatic2.Size = Size(67, 16)
        self.labelStatic2.TabIndex = 49
        self.labelStatic2.Text = "Status"
        # 
        # labelTextStatus
        # 
        self.labelTextStatus.BorderStyle = BorderStyle.Fixed3D
        self.labelTextStatus.Location = Point(94, 44)
        self.labelTextStatus.Name = "labelTextStatus"
        self.labelTextStatus.Size = Size(595, 20)
        self.labelTextStatus.TabIndex = 50
        self.labelTextStatus.Text = "No file loaded."
        self.labelTextStatus.TextAlign = ContentAlignment.MiddleLeft
        # 
        # checkboxLoop
        # 
        self.checkboxLoop.Location = Point(42, 376)
        self.checkboxLoop.Name = "checkboxLoop"
        self.checkboxLoop.Size = Size(86, 16)
        self.checkboxLoop.TabIndex = 51
        self.checkboxLoop.Text = "&Loop Sound"
        self.checkboxLoop.CheckedChanged += self.checkboxLoop_CheckedChanged
        # 
        # buttonPlay
        # 
        self.buttonPlay.Location = Point(10, 400)
        self.buttonPlay.Name = "buttonPlay"
        self.buttonPlay.Size = Size(67, 23)
        self.buttonPlay.TabIndex = 52
        self.buttonPlay.Text = "&Play"
        self.buttonPlay.Click += self.buttonPlay_Click
        # 
        # buttonStop
        # 
        self.buttonStop.Location = Point(87, 400)
        self.buttonStop.Name = "buttonStop"
        self.buttonStop.Size = Size(67, 23)
        self.buttonStop.TabIndex = 53
        self.buttonStop.Text = "&Stop"
        self.buttonStop.Enabled = False
        self.buttonStop.Click += self.buttonStop_Click
        # 
        # labelStatic3
        # 
        self.labelStatic3.BorderStyle = BorderStyle.Fixed3D
        self.labelStatic3.Location = Point(372, 88)
        self.labelStatic3.Name = "labelStatic3"
        self.labelStatic3.Size = Size(52, 16)
        self.labelStatic3.TabIndex = 62
        self.labelStatic3.Text = "Min"
        self.labelStatic3.TextAlign = ContentAlignment.TopCenter
        # 
        # labelStatic4
        # 
        self.labelStatic4.BorderStyle = BorderStyle.Fixed3D
        self.labelStatic4.Location = Point(627, 88)
        self.labelStatic4.Name = "labelStatic4"
        self.labelStatic4.Size = Size(52, 16)
        self.labelStatic4.TabIndex = 64
        self.labelStatic4.Text = "Max"
        self.labelStatic4.TextAlign = ContentAlignment.TopCenter
        # 
        # radiobuttonRadioNeg180
        # 
        self.radiobuttonRadioNeg180.Location = Point(16, 16)
        self.radiobuttonRadioNeg180.Name = "radiobuttonRadioNeg180"
        self.radiobuttonRadioNeg180.Size = Size(45, 16)
        self.radiobuttonRadioNeg180.TabIndex = 65
        self.radiobuttonRadioNeg180.Text = "-180"
        self.radiobuttonRadioNeg180.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadioNeg90
        # 
        self.radiobuttonRadioNeg90.Location = Point(72, 16)
        self.radiobuttonRadioNeg90.Name = "radiobuttonRadioNeg90"
        self.radiobuttonRadioNeg90.Size = Size(39, 16)
        self.radiobuttonRadioNeg90.TabIndex = 66
        self.radiobuttonRadioNeg90.Text = "-90"
        self.radiobuttonRadioNeg90.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadioZero
        # 
        self.radiobuttonRadioZero.Location = Point(120, 16)
        self.radiobuttonRadioZero.Name = "radiobuttonRadioZero"
        self.radiobuttonRadioZero.Size = Size(30, 16)
        self.radiobuttonRadioZero.TabIndex = 67
        self.radiobuttonRadioZero.Text = "0"
        self.radiobuttonRadioZero.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadio90
        # 
        self.radiobuttonRadio90.Location = Point(152, 16)
        self.radiobuttonRadio90.Name = "radiobuttonRadio90"
        self.radiobuttonRadio90.Size = Size(36, 16)
        self.radiobuttonRadio90.TabIndex = 68
        self.radiobuttonRadio90.Text = "90"
        self.radiobuttonRadio90.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadio180
        # 
        self.radiobuttonRadio180.Location = Point(200, 16)
        self.radiobuttonRadio180.Name = "radiobuttonRadio180"
        self.radiobuttonRadio180.Size = Size(42, 16)
        self.radiobuttonRadio180.TabIndex = 69
        self.radiobuttonRadio180.Text = "180"
        self.radiobuttonRadio180.CheckedChanged += self.trackbarSliderScroll

        # 
        # labelTextFilename
        # 
        self.labelTextFilename.BorderStyle = BorderStyle.Fixed3D
        self.labelTextFilename.Location = Point(94, 14)
        self.labelTextFilename.Name = "labelTextFilename"
        self.labelTextFilename.Size = Size(595, 20)
        self.labelTextFilename.TabIndex = 48
        self.labelTextFilename.Text = "Filename"
        self.labelTextFilename.TextAlign = ContentAlignment.MiddleLeft
        # 
        # labelStatic2
        # 
        self.labelStatic2.Location = Point(19, 44)
        self.labelStatic2.Name = "labelStatic2"
        self.labelStatic2.Size = Size(67, 16)
        self.labelStatic2.TabIndex = 49
        self.labelStatic2.Text = "Status"
        # 
        # labelTextStatus
        # 
        self.labelTextStatus.BorderStyle = BorderStyle.Fixed3D
        self.labelTextStatus.Location = Point(94, 44)
        self.labelTextStatus.Name = "labelTextStatus"
        self.labelTextStatus.Size = Size(595, 20)
        self.labelTextStatus.TabIndex = 50
        self.labelTextStatus.Text = "No file loaded."
        self.labelTextStatus.TextAlign = ContentAlignment.MiddleLeft
        # 
        # checkboxLoop
        # 
        self.checkboxLoop.Location = Point(42, 376)
        self.checkboxLoop.Name = "checkboxLoop"
        self.checkboxLoop.Size = Size(86, 16)
        self.checkboxLoop.TabIndex = 51
        self.checkboxLoop.Text = "&Loop Sound"
        self.checkboxLoop.CheckedChanged += self.checkboxLoop_CheckedChanged
        # 
        # buttonPlay
        # 
        self.buttonPlay.Location = Point(10, 400)
        self.buttonPlay.Name = "buttonPlay"
        self.buttonPlay.Size = Size(67, 23)
        self.buttonPlay.TabIndex = 52
        self.buttonPlay.Text = "&Play"
        self.buttonPlay.Click += self.buttonPlay_Click
        # 
        # buttonStop
        # 
        self.buttonStop.Location = Point(87, 400)
        self.buttonStop.Name = "buttonStop"
        self.buttonStop.Size = Size(67, 23)
        self.buttonStop.TabIndex = 53
        self.buttonStop.Text = "&Stop"
        self.buttonStop.Enabled = False
        self.buttonStop.Click += self.buttonStop_Click
        # 
        # labelStatic3
        # 
        self.labelStatic3.BorderStyle = BorderStyle.Fixed3D
        self.labelStatic3.Location = Point(372, 88)
        self.labelStatic3.Name = "labelStatic3"
        self.labelStatic3.Size = Size(52, 16)
        self.labelStatic3.TabIndex = 62
        self.labelStatic3.Text = "Min"
        self.labelStatic3.TextAlign = ContentAlignment.TopCenter
        # 
        # labelStatic4
        # 
        self.labelStatic4.BorderStyle = BorderStyle.Fixed3D
        self.labelStatic4.Location = Point(627, 88)
        self.labelStatic4.Name = "labelStatic4"
        self.labelStatic4.Size = Size(52, 16)
        self.labelStatic4.TabIndex = 64
        self.labelStatic4.Text = "Max"
        self.labelStatic4.TextAlign = ContentAlignment.TopCenter
        # 
        # radiobuttonRadioNeg180
        # 
        self.radiobuttonRadioNeg180.Location = Point(16, 16)
        self.radiobuttonRadioNeg180.Name = "radiobuttonRadioNeg180"
        self.radiobuttonRadioNeg180.Size = Size(45, 16)
        self.radiobuttonRadioNeg180.TabIndex = 65
        self.radiobuttonRadioNeg180.Text = "-180"
        self.radiobuttonRadioNeg180.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadioNeg90
        # 
        self.radiobuttonRadioNeg90.Location = Point(72, 16)
        self.radiobuttonRadioNeg90.Name = "radiobuttonRadioNeg90"
        self.radiobuttonRadioNeg90.Size = Size(39, 16)
        self.radiobuttonRadioNeg90.TabIndex = 66
        self.radiobuttonRadioNeg90.Text = "-90"
        self.radiobuttonRadioNeg90.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadioZero
        # 
        self.radiobuttonRadioZero.Location = Point(120, 16)
        self.radiobuttonRadioZero.Name = "radiobuttonRadioZero"
        self.radiobuttonRadioZero.Size = Size(30, 16)
        self.radiobuttonRadioZero.TabIndex = 67
        self.radiobuttonRadioZero.Text = "0"
        self.radiobuttonRadioZero.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadio90
        # 
        self.radiobuttonRadio90.Location = Point(152, 16)
        self.radiobuttonRadio90.Name = "radiobuttonRadio90"
        self.radiobuttonRadio90.Size = Size(36, 16)
        self.radiobuttonRadio90.TabIndex = 68
        self.radiobuttonRadio90.Text = "90"
        self.radiobuttonRadio90.CheckedChanged += self.trackbarSliderScroll
        # 
        # radiobuttonRadio180
        # 
        self.radiobuttonRadio180.Location = Point(200, 16)
        self.radiobuttonRadio180.Name = "radiobuttonRadio180"
        self.radiobuttonRadio180.Size = Size(42, 16)
        self.radiobuttonRadio180.TabIndex = 69
        self.radiobuttonRadio180.Text = "180"
        self.radiobuttonRadio180.CheckedChanged += self.trackbarSliderScroll

        # 
        # buttonDelete
        # 
        self.buttonDelete.Location = Point(40, 248)
        self.buttonDelete.Name = "buttonDelete"
        self.buttonDelete.Size = Size(64, 24)
        self.buttonDelete.TabIndex = 3
        self.buttonDelete.Text = "Delete"
        self.buttonDelete.Click += self.buttonDelete_Click
        # 
        # listboxEffects
        # 
        self.listboxEffects.Location = Point(8, 48)
        self.listboxEffects.Name = "listboxEffects"
        self.listboxEffects.Size = Size(128, 186)
        self.listboxEffects.TabIndex = 2
        self.listboxEffects.KeyUp += KeyEventHandler(self.listboxEffects_KeyUp)
        self.listboxEffects.SelectedIndexChanged += self.listboxEffects_SelectedIndexChanged

        # 
        # timer1
        # 
        self.timer1.Interval = 50
        self.timer1.Tick += self.timer1_Tick

        # 
        # groupboxFrameWaveform
        # 
        self.groupboxFrameWaveform.Controls.AddRange(Array[Control] ([\
            self.radiobuttonSquare,\
            self.radiobuttonTriangle,\
            self.radiobuttonRadioSine\
        ]))
        self.groupboxFrameWaveform.Location = Point(180, 400)
        self.groupboxFrameWaveform.Name = "groupboxFrameWaveform"
        self.groupboxFrameWaveform.Size = Size(225, 42)
        self.groupboxFrameWaveform.TabIndex = 35
        self.groupboxFrameWaveform.TabStop = False
        self.groupboxFrameWaveform.Text = "Waveform"

# 
        # groupboxFramePhase
        # 
        self.groupboxFramePhase.Controls.AddRange(Array[Control] ([
         self.radiobuttonRadioNeg180,
         self.radiobuttonRadioNeg90,
         self.radiobuttonRadioZero,
         self.radiobuttonRadio90,
         self.radiobuttonRadio180
        ]))
        self.groupboxFramePhase.Location = Point(420, 400)
        self.groupboxFramePhase.Name = "groupboxFramePhase"
        self.groupboxFramePhase.Size = Size(247, 42)
        self.groupboxFramePhase.TabIndex = 63
        self.groupboxFramePhase.TabStop = False
        self.groupboxFramePhase.Text = "Phase (Degrees)"

	    # 
        # groupboxEffects
        # 
        self.groupboxEffects.Controls.AddRange(Array[Control] ([
	      self.buttonDelete,
	      self.listboxEffects,
	      self.comboEffects
	    ]))
        self.groupboxEffects.Location = Point(8, 80)
        self.groupboxEffects.Name = "groupboxEffects"
        self.groupboxEffects.Size = Size(144, 280)
        self.groupboxEffects.TabIndex = 71
        self.groupboxEffects.TabStop = False
        self.groupboxEffects.Text = "Effects"

        # 
        # comboEffects
        # 
        self.comboEffects.DropDownStyle = ComboBoxStyle.DropDownList
        self.comboEffects.Items.AddRange(Array[Object] ([
          "Chorus",
          "Compressor",
          "Distortion",
          "Echo",
          "Flanger",
          "Gargle",
          "Waves Reverb",
          "ParamEq"
    	]))
        self.comboEffects.Location = Point(8, 16)
        self.comboEffects.Name = "comboEffects"
        self.comboEffects.Size = Size(128, 21)
        self.comboEffects.TabIndex = 1
        self.comboEffects.SelectedValueChanged += self.comboEffects_SelectedValueChanged

        self.Controls.AddRange(Array[Control] ([
              self.groupboxEffects,
              self.buttonOk,
              self.labelParamName1,
              self.labelParamValue1,
              self.trackbarSlider1,
              self.labelParamMin1,
              self.labelParamMax1,
              self.labelParamName2,
              self.labelParamValue2,
              self.trackbarSlider2,
              self.labelParamMin2,
              self.labelParamMax2,
              self.labelParamName3,
              self.labelParamValue3,
              self.trackbarSlider3,
              self.labelParamMin3,
              self.labelParamMax3,
              self.labelParamName4,
              self.labelParamValue4,
              self.trackbarSlider4,
              self.labelParamMin4,
              self.labelParamMax4,
              self.labelParamName5,
              self.labelParamValue5,
              self.trackbarSlider5,
              self.labelParamMin5,
              self.labelParamMax5,
              self.labelParamName6,
              self.labelParamValue6,
              self.trackbarSlider6,
              self.labelParamMin6,
              self.labelParamMax6,
              self.buttonOpen,
              self.labelTextFilename,
              self.labelStatic2,
              self.labelTextStatus,
              self.checkboxLoop,
              self.buttonPlay,
              self.buttonStop,
              self.labelStatic3,
              self.labelStatic4,
              self.groupboxFrameWaveform,
              self.groupboxFramePhase,
              self.groupboxFrame
        ]))
        # Form
        self.AcceptButton = self.buttonOk
        self.ClientSize = Size(700, 472)
        self.FormBorderStyle = FormBorderStyle.FixedSingle
        self.Location = Point(150, 160)
        self.MaximizeBox = False
        self.Name = "MainForm"
        self.Text = "SoundFX - Sound effects applied to Device.SecondaryBuffer"
        self.Closing += CancelEventHandler(self.MainForm_Closing)
        self.trackbarSlider1.EndInit()
        self.trackbarSlider2.EndInit()
        self.trackbarSlider3.EndInit()
        self.trackbarSlider4.EndInit()
        self.trackbarSlider5.EndInit()
        self.trackbarSlider6.EndInit()
        self.groupboxFrameWaveform.ResumeLayout(False)
        self.groupboxFramePhase.ResumeLayout(False)
        self.groupboxEffects.ResumeLayout(False)
        self.ResumeLayout(False)

    def trackbarSliderScroll(self, sender, e):
        # We're ignoring settings right now
        if self.isIgnoringSettings:
            return

        eff = self.effectDescription[self.currentIndex]
        efftype = eff.Effect.GetType()

        if (clr.GetClrType(ChorusEffect) == efftype):
            temp = EffectsChorus()
            temp.WetDryMix = self.trackbarSlider1.Value
            temp.Frequency = self.trackbarSlider4.Value
            temp.Feedback = self.trackbarSlider3.Value
            temp.Depth = self.trackbarSlider2.Value
            temp.Delay = self.trackbarSlider5.Value
            
            if (True == self.radiobuttonRadioSine.Checked):
                temp.Waveform = ChorusEffect.WaveSin
            else:
                temp.Waveform = ChorusEffect.WaveTriangle
            
            if (True == self.radiobuttonRadioNeg180.Checked):
                temp.Phase = ChorusEffect.PhaseNegative180
            elif (True == self.radiobuttonRadioNeg90.Checked):
                temp.Phase = ChorusEffect.PhaseNegative90
            elif (True == self.radiobuttonRadioZero.Checked):
                temp.Phase = ChorusEffect.PhaseZero
            elif (True == self.radiobuttonRadio90.Checked):
                temp.Phase = ChorusEffect.Phase90
            elif (True == self.radiobuttonRadio180.Checked):
                temp.Phase = ChorusEffect.Phase180

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp            

        elif (clr.GetClrType(CompressorEffect) == efftype):
            temp = EffectsCompressor()
            temp.Gain = self.trackbarSlider1.Value
            temp.Attack = self.trackbarSlider2.Value
            temp.Release = self.trackbarSlider3.Value
            temp.Threshold = self.trackbarSlider4.Value
            temp.Ratio = self.trackbarSlider5.Value
            temp.Predelay = self.trackbarSlider6.Value

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp
        elif (clr.GetClrType(DistortionEffect) == efftype):
            temp = EffectsDistortion()
            temp.Gain = self.trackbarSlider1.Value
            temp.Edge = self.trackbarSlider2.Value
            temp.PostEqCenterFrequency = self.trackbarSlider3.Value
            temp.PostEqBandwidth = self.trackbarSlider4.Value
            temp.PreLowpassCutoff = self.trackbarSlider5.Value

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp
        elif (clr.GetClrType(EchoEffect) == efftype):
            temp = EffectsEcho()
            temp.WetDryMix = self.trackbarSlider1.Value
            temp.Feedback = self.trackbarSlider2.Value
            temp.LeftDelay = self.trackbarSlider3.Value
            temp.RightDelay = self.trackbarSlider4.Value
            temp.PanDelay = self.trackbarSlider5.Value

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp
        elif (clr.GetClrType(FlangerEffect) == efftype):
            temp = EffectsFlanger()
            temp.WetDryMix = self.trackbarSlider1.Value
            temp.Depth = self.trackbarSlider2.Value
            temp.Feedback = self.trackbarSlider3.Value
            temp.Frequency = self.trackbarSlider4.Value
            temp.Delay = self.trackbarSlider5.Value
        
            if (True == self.radiobuttonRadioSine.Checked):
                temp.Waveform = FlangerEffect.WaveSin
            else:
                temp.Waveform = FlangerEffect.WaveTriangle

            if (True == self.radiobuttonRadioNeg180.Checked):
                temp.Phase = ChorusEffect.PhaseNegative180
            elif (True == self.radiobuttonRadioNeg90.Checked):
                temp.Phase = ChorusEffect.PhaseNegative90
            elif (True == self.radiobuttonRadioZero.Checked):
                temp.Phase = ChorusEffect.PhaseZero
            elif (True == self.radiobuttonRadio90.Checked):
                temp.Phase = ChorusEffect.Phase90
            elif (True == self.radiobuttonRadio180.Checked):
                temp.Phase = ChorusEffect.Phase180

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp

        elif (clr.GetClrType(GargleEffect) == efftype):
            temp = EffectsGargle()
            temp.RateHz = self.trackbarSlider1.Value
            if (self.radiobuttonSquare.Checked):
                temp.WaveShape = GargleEffect.WaveSquare
            else:
                temp.WaveShape = GargleEffect.WaveTriangle

            if (True == self.radiobuttonSquare.Checked):
                temp.WaveShape = GargleEffect.WaveSquare
            else:
                temp.WaveShape = GargleEffect.WaveTriangle

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp

        elif (clr.GetClrType(ParamEqEffect) == efftype):
            temp = EffectsParamEq()
            temp.Center = self.trackbarSlider1.Value
            temp.Bandwidth = self.trackbarSlider2.Value
            temp.Gain = self.trackbarSlider3.Value

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp

        elif (clr.GetClrType(WavesReverbEffect) == efftype):
            temp = EffectsWavesReverb()
            temp.InGain = self.trackbarSlider1.Value
            temp.ReverbMix = self.trackbarSlider2.Value
            temp.ReverbTime = (.001 * self.trackbarSlider3.Value)
            temp.HighFrequencyRtRatio = (.001 * self.trackbarSlider4.Value)

            eff.EffectSettings = temp
            eff.Effect.AllParameters = temp

        self.effectDescription[self.currentIndex] = eff
        self.UpdateUI(False)

    def buttonOk_Click(self, sender, e):
        """
        事件：結束程式
        """
        self.Close()

    def buttonOpen_Click(self, sender, e):
        """
        事件：檔案選取
        """
        description = BufferDescription()
        ofd = OpenFileDialog()

        self.labelTextStatus.Text = "Loading file..."

        # 取得預設路徑 (如： C:\WINDOWS\MEDIA)
        if ('' == self.path):
            self.path = Environment.SystemDirectory.Substring(0, Environment.SystemDirectory.LastIndexOf("\\")) + "\\media"

        ofd.DefaultExt = ".wav"
        ofd.Filter = "Wave Files|*.wav|All Files|*.*"
        ofd.FileName = self.fileName
        ofd.InitialDirectory = self.path

        if (not None is self.applicationBuffer):
            self.applicationBuffer.Stop()
            self.applicationBuffer.SetCurrentPosition(0)


        # 檔案選取
        if (DialogResult.Cancel == ofd.ShowDialog(self)):
            if(not None is self.applicationBuffer):
                self.applicationBuffer.Dispose()

            self.labelTextStatus.Text = "No file loaded."
            return

        self.fileName = ''

        description.ControlEffects = True
    
        # 利用檔案建立 SecondaryBuffer
        try:
            self.applicationBuffer = SecondaryBuffer(ofd.FileName, description,  self.applicationDevice)
        except(BufferTooSmallException): 
            self.labelTextStatus.Text = "Wave file is too small to be used with effects."
            return
        except(FormatException):
            # Invalid file was used. Managed DirectSound tries to convert any files less than
            # 8 bit to 8 bit. Some drivers don't support this conversion, so make sure to
            # catch the FormatException if it's thrown.
            self.labelTextStatus.Text = "Failed to create SecondaryBuffer from selected file."
            return

        
        # 紀錄參數
        if (not None is self.applicationBuffer):
            self.fileName = ofd.FileName
            self.path =  self.fileName.Substring(0, self.fileName.LastIndexOf("\\"))

        self.labelTextFilename.Text = self.fileName



    def checkboxLoop_CheckedChanged(self, sender, e):
        """
        事件：重複播放選項變更
        """
        self.shouldLoop = self.checkboxLoop.Checked


    def buttonPlay_Click(self, sender, e):
        """
        事件：開始播放
        """
        if (not None is self.applicationBuffer):
            self.applicationBuffer.Play(0, BufferPlayFlags.Looping if self.shouldLoop else BufferPlayFlags.Default)
            self.timer1.Enabled = True
            self.buttonStop.Enabled = True
            self.buttonPlay.Enabled = False
            self.comboEffects.Enabled = False
            self.labelTextStatus.Text="Sound playing."

    def buttonStop_Click(self, sender, e):
        """
        事件：停止播放
        """
        if (not None is self.applicationBuffer):
            if self.applicationBuffer.Status.Playing:
                self.applicationBuffer.Stop()
                self.applicationBuffer.SetCurrentPosition(0)
                self.timer1.Enabled = False
                self.buttonStop.Enabled = False
                self.buttonPlay.Enabled = True
                self.comboEffects.Enabled = True
                self.labelTextStatus.Text="Sound stopped."


    def buttonDelete_Click(self, sender, e):
        """
        事件：刪除特效
        """
        self.DeleteEffect()

    def AddEffect(self, temp):
        """
        添加特效
        """
        ret = None
        fx = None      
        WasPlaying = False
        count = 0

        if (not None is temp):
            #fx = Array.CreateInstance(EffectDescription, len(temp))
            #fx = []
            count = len(temp)

        if (True == self.applicationBuffer.Status.Playing):
            WasPlaying = True
        
        self.applicationBuffer.Stop()
        
        # Store the current params for each effect.
        fx = [elem.description for elem in temp]

        try:
            ret = self.applicationBuffer.SetEffects( Array[EffectDescription](fx) )
        except DirectXException as inst:
            
            labelTextStatus.Text = "Unable to set effect on the buffer. Some effects can't be set on 8 bit wave files."

            # Revert to the last valid effects.
            if (len(temp) <= 1):
                return False

            fx = Array.CreateInstance(EffectDescription, len(temp) -1)
            for i in range(count - 1):
                fx[i] = temp[i].description

            try:
                self.applicationBuffer.SetEffects(fx)
            except(DirectXException):
                pass

            return False

        
        # Restore the params for each effect.
        for i in range(count):
            eff = EffectInfo()

            eff.Effect = self.applicationBuffer.GetEffects(i)
            eff.EffectSettings = temp[i].EffectSettings
            eff.description = temp[i].description

            efftype = eff.Effect.GetType()

            if (clr.GetClrType(ChorusEffect) == efftype):
                if (not None is eff.EffectSettings):
                    eff.Effect.AllParameters = eff.EffectSettings
                else:
                    eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType ==efftype) :
                if (not None is eff.EffectSettings):
                    eff.Effect.AllParameters = eff.EffectSettings
                else:
                    eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(DistortionEffect) == efftype):
                if (not None is eff.EffectSettings):
                    eff.Effect.AllParameters = eff.EffectSettings
                else:
                    eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(EchoEffect) == efftype):
                if (not None is eff.EffectSettings):
                    eff.Effect.AllParameters = eff.EffectSettings
                else:
                    eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(FlangerEffect) == efftype):
                 if (not None is eff.EffectSettings):
                     eff.Effect.AllParameters = eff.EffectSettings
                 else:
                     eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(GargleEffect) == efftype):
                 if (not None is eff.EffectSettings):
                     eff.Effect.AllParameters = eff.EffectSettings
                 else:
                     eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(ParamEqEffect) == efftype):
                 if (not None is eff.EffectSettings):
                     eff.Effect.AllParameters = eff.EffectSettings
                 else:
                     eff.EffectSettings = eff.Effect.AllParameters
            elif (clr.GetClrType(WavesReverbEffect) == efftype):
                 if (not None is eff.EffectSettings):
                     eff.Effect.AllParameters = eff.EffectSettings
                 else:
                     eff.EffectSettings = eff.Effect.AllParameters

            temp[i] = eff

        
        if (WasPlaying):
            self.applicationBuffer.Play(0, BufferPlayFlags.Looping if shouldLoop else BufferPlayFlags.Default)

        if (not None is temp):
            if ((1 == ret[-1]) or (2 == ret[-1]) ):
                return True
        return False


    def DeleteEffect(self):
       temp = None

       if (-1 == listboxEffects.SelectedIndex) :
            return

       self.effectDescription.RemoveAt(listboxEffects.SelectedIndex)

       if (effectDescription.Count > 0):
            #temp = EffectInfo[effectDescription.Count]
            temp = Array.CreateInstance(EffectInfo, self.effectDescription.Count)
            self.effectDescription.CopyTo(temp, 0)
            self.AddEffect(temp)
            self.listboxEffects.Items.RemoveAt(self.listboxEffects.SelectedIndex)
            self.listboxEffects.SelectedIndex = self.currentIndex = 0
       else:
            temp = None
            self.AddEffect(temp)
            self.listboxEffects.Items.Clear()
            self.ClearUI(True)

       self.effectDescription.Clear()
       if (not None is temp):
           self.effectDescription.AddRange(temp)
            
    def listboxEffects_KeyUp(self, sender, e):
        if (e.KeyCode == Keys.Delete):
            self.DeleteEffect()

    def listboxEffects_SelectedIndexChanged(self, sender, e):
        """
        事件：特效設定切換
        """
        if (-1 == self.listboxEffects.SelectedIndex):
            return
        
        self.currentIndex = self.listboxEffects.SelectedIndex        
        # Make sure we don't update any settings while updating the UI
        self.isIgnoringSettings = True
        self.UpdateUI(True)
        self.isIgnoringSettings = False
    def UpdateUI(self, MoveControls):    
        """
        更新 UI
        """
       
        self.ClearUI(MoveControls)

        efftype = self.effectDescription[self.currentIndex].Effect.GetType()
        eff     = self.effectDescription[self.currentIndex].Effect

        if (clr.GetClrType(ChorusEffect) == efftype):
            temp = eff.AllParameters

            if (MoveControls):
                self.trackbarSlider1.Minimum = int(ChorusEffect.WetDryMixMin)
                self.trackbarSlider1.Maximum = int(ChorusEffect.WetDryMixMax)
                self.trackbarSlider1.Value = int(temp.WetDryMix)

                self.trackbarSlider2.Minimum = int(ChorusEffect.DepthMin)
                self.trackbarSlider2.Maximum = int(ChorusEffect.DepthMax)
                self.trackbarSlider2.Value = int(temp.Depth)

                self.trackbarSlider3.Minimum = int(ChorusEffect.FeedbackMin)
                self.trackbarSlider3.Maximum = int(ChorusEffect.FeedbackMax)
                self.trackbarSlider3.Value = int(temp.Feedback)

                self.trackbarSlider4.Minimum = int(ChorusEffect.FrequencyMin)
                self.trackbarSlider4.Maximum = int(ChorusEffect.FrequencyMax)
                self.trackbarSlider4.Value = int(temp.Frequency)

                self.trackbarSlider5.Minimum = int(ChorusEffect.DelayMin)
                self.trackbarSlider5.Maximum = int(ChorusEffect.DelayMax)
                self.trackbarSlider5.Value = int(temp.Delay)

                if (ChorusEffect.WaveSin == temp.Waveform):
                    self.radiobuttonRadioSine.Checked = True
                else:
                    self.radiobuttonTriangle.Checked = True

                if (ChorusEffect.PhaseNegative180 == temp.Phase):
                    self.radiobuttonRadioNeg180.Checked = True
                elif (ChorusEffect.PhaseNegative90 == temp.Phase):
                    self.radiobuttonRadioNeg90.Checked = True
                elif (ChorusEffect.PhaseZero == temp.Phase):
                    self.radiobuttonRadioZero.Checked = True
                elif (ChorusEffect.Phase90 == temp.Phase):
                    self.radiobuttonRadio90.Checked = True
                elif (ChorusEffect.Phase180 == temp.Phase):
                    self.radiobuttonRadio180.Checked = True

                self.groupboxFramePhase.Enabled = self.radiobuttonRadioNeg180.Enabled = self.radiobuttonRadioNeg90.Enabled =\
                self.radiobuttonRadioZero.Enabled = self.radiobuttonRadio90.Enabled = self.radiobuttonRadio180.Enabled =\
                self.groupboxFrameWaveform.Enabled = self.radiobuttonRadioSine.Enabled =\
                self.radiobuttonTriangle.Enabled = True

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled =\
                self.trackbarSlider4.Enabled = self.trackbarSlider5.Enabled = True

            self.labelParamValue1.Text = temp.WetDryMix.ToString()
            self.labelParamName1.Text = "Wet/Dry Mix (%)"
            
            self.labelParamValue2.Text =  temp.Depth.ToString()
            self.labelParamName2.Text = "Depth (%)"

            self.labelParamValue3.Text = temp.Feedback.ToString()
            self.labelParamName3.Text = "Feedback (%)"

            self.labelParamValue4.Text = temp.Frequency.ToString()
            self.labelParamName4.Text = "Frequency (Hz)"

            self.labelParamValue5.Text = temp.Delay.ToString()
            self.labelParamName5.Text = "Delay (ms)" 
        
        elif (clr.GetClrType(CompressorEffect) == efftype) :
            temp = eff.AllParameters
            
            if (MoveControls):
                self.trackbarSlider1.Minimum = int(CompressorEffect.GainMin)
                self.trackbarSlider1.Maximum = int(CompressorEffect.GainMax)
                self.trackbarSlider1.Value = int(temp.Gain)
                self.trackbarSlider2.Minimum = int(CompressorEffect.AttackMin)
                self.trackbarSlider2.Maximum = int(CompressorEffect.AttackMax)
                self.trackbarSlider2.Value = int(temp.Attack)
                self.trackbarSlider3.Minimum = int(CompressorEffect.ReleaseMin)
                self.trackbarSlider3.Maximum = int(CompressorEffect.ReleaseMax)
                self.trackbarSlider3.Value = int(temp.Release)
                self.trackbarSlider4.Minimum = int(CompressorEffect.ThresholdMin)
                self.trackbarSlider4.Maximum = int(CompressorEffect.ThresholdMax)
                self.trackbarSlider4.Value = int(temp.Threshold)
                self.trackbarSlider5.Minimum = int(CompressorEffect.RatioMin)
                self.trackbarSlider5.Maximum = int(CompressorEffect.RatioMax)
                self.trackbarSlider5.Value = int(temp.Ratio)
                self.trackbarSlider6.Minimum = int(CompressorEffect.PreDelayMin)
                self.trackbarSlider6.Maximum = int(CompressorEffect.PreDelayMax)
                self.trackbarSlider6.Value = int(temp.Predelay)

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled = \
                self.trackbarSlider4.Enabled = self.trackbarSlider5.Enabled = self.trackbarSlider6.Enabled = True
            
            self.labelParamValue1.Text = temp.Gain.ToString()
            self.labelParamName1.Text = "Gain (dB)"

            self.labelParamName2.Text = "Attack (ms)"
            self.labelParamValue2.Text = temp.Attack.ToString()
            
            self.labelParamName3.Text = "Release (ms)"
            self.labelParamValue3.Text = temp.Release.ToString()
            
            self.labelParamName4.Text = "Threshold (dB)"
            self.labelParamValue4.Text = temp.Threshold.ToString()
            
            self.labelParamName5.Text = "Ratio (x:1)"
            self.labelParamValue5.Text = temp.Ratio.ToString()
            
            self.labelParamName6.Text = "Predelay (ms)"
            self.labelParamValue6.Text = temp.Predelay.ToString()
        
        elif (clr.GetClrType(DistortionEffect) == efftype):
            temp = eff.AllParameters
            
            if (MoveControls):
                self.trackbarSlider1.Minimum = int(DistortionEffect.GainMin)
                self.trackbarSlider1.Maximum = int(DistortionEffect.GainMax)
                self.trackbarSlider1.Value = int(temp.Gain)
                self.trackbarSlider2.Minimum = int(DistortionEffect.EdgeMin)
                self.trackbarSlider2.Maximum = int(DistortionEffect.EdgeMax)
                self.trackbarSlider2.Value = int(temp.Edge)
                self.trackbarSlider3.Minimum = int(DistortionEffect.PostEqCenterFrequencyMin)
                self.trackbarSlider3.Maximum = int(DistortionEffect.PostEqCenterFrequencyMax)
                self.trackbarSlider3.Value = int(temp.PostEqCenterFrequency)
                self.trackbarSlider4.Minimum = int(DistortionEffect.PostEqBandwidthMin)
                self.trackbarSlider4.Maximum = int(DistortionEffect.PostEqBandwidthMax)
                self.trackbarSlider4.Value = int(temp.PostEqBandwidth)
                self.trackbarSlider5.Minimum = int(DistortionEffect.PreLowPassCutoffMin)
                self.trackbarSlider5.Maximum = int(DistortionEffect.PreLowPassCutoffMax)
                self.trackbarSlider5.Value = int(temp.PreLowpassCutoff)

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled =\
                    self.trackbarSlider4.Enabled = self.trackbarSlider5.Enabled = True
            
            self.labelParamName1.Text = "Gain (dB)"
            self.labelParamValue1.Text = temp.Gain.ToString()
            
            self.labelParamName2.Text = "Edge (%)"
            self.labelParamValue2.Text = temp.Edge.ToString()
            
            self.labelParamName3.Text = "PostEQ Center Freq (Hz)"
            self.labelParamValue3.Text = temp.PostEqCenterFrequency.ToString()
            
            self.labelParamName4.Text = "PostEQ Bandwidth (Hz)"
            self.labelParamValue4.Text = temp.PostEqBandwidth.ToString()
            
            self.labelParamName5.Text = "PreLowpass Cutoff (Hz)"
            self.labelParamValue5.Text = temp.PreLowpassCutoff.ToString()
        
        elif (clr.GetClrType(EchoEffect) == efftype):
            temp = eff.AllParameters
            
            if (MoveControls):
                self.trackbarSlider1.Minimum = int(EchoEffect.WetDryMixMin)
                self.trackbarSlider1.Maximum = int(EchoEffect.WetDryMixMax)
                self.trackbarSlider1.Value = int(temp.WetDryMix)
                self.trackbarSlider2.Minimum = int(EchoEffect.FeedbackMin)
                self.trackbarSlider2.Maximum = int(EchoEffect.FeedbackMax)
                self.trackbarSlider2.Value = int(temp.Feedback)
                self.trackbarSlider3.Minimum = int(EchoEffect.LeftDelayMin)
                self.trackbarSlider3.Maximum = int(EchoEffect.LeftDelayMax)
                self.trackbarSlider3.Value = int(temp.LeftDelay)
                self.trackbarSlider4.Minimum = int(EchoEffect.RightDelayMin)
                self.trackbarSlider4.Maximum = int(EchoEffect.RightDelayMax)
                self.trackbarSlider4.Value = int(temp.RightDelay)
                self.trackbarSlider5.Minimum = int(EchoEffect.PanDelayMin)
                self.trackbarSlider5.Maximum = int(EchoEffect.PanDelayMax)
                self.trackbarSlider5.Value = int(temp.PanDelay)

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled =\
                self.trackbarSlider4.Enabled = self.trackbarSlider5.Enabled = True
            
            self.labelParamName1.Text = "Wet/Dry Mix (%)"
            self.labelParamValue1.Text = temp.WetDryMix.ToString()
            
            self.labelParamName2.Text = "Feedback (%)"
            self.labelParamValue2.Text = temp.Feedback.ToString()
            
            self.labelParamName3.Text = "Left Delay (ms)"           
            self.labelParamValue3.Text = temp.LeftDelay.ToString()
                        
            self.labelParamName4.Text = "Right Delay (ms)"
            self.labelParamValue4.Text = temp.RightDelay.ToString()
            
            self.labelParamName5.Text = "Pan Delay (bool)"
            self.labelParamValue5.Text = temp.PanDelay.ToString()
        
        elif (clr.GetClrType(FlangerEffect) == efftype):
            temp = eff.AllParameters
            
            if (MoveControls) :
                self.trackbarSlider1.Minimum = int(FlangerEffect.WetDryMixMin)
                self.trackbarSlider1.Maximum = int(FlangerEffect.WetDryMixMax)
                self.trackbarSlider1.Value = int(temp.WetDryMix)
                self.trackbarSlider2.Minimum = int(FlangerEffect.DepthMin)
                self.trackbarSlider2.Maximum = int(FlangerEffect.DepthMax)
                self.trackbarSlider2.Value = int(temp.Depth)
                self.trackbarSlider3.Minimum = int(FlangerEffect.FeedbackMin)
                self.trackbarSlider3.Maximum = int(FlangerEffect.FeedbackMax)
                self.trackbarSlider3.Value = int(temp.Feedback)
                self.trackbarSlider4.Minimum = int(FlangerEffect.FrequencyMin)
                self.trackbarSlider4.Maximum = int(FlangerEffect.FrequencyMax)
                self.trackbarSlider4.Value = int(temp.Frequency)
                self.trackbarSlider5.Minimum = int(FlangerEffect.DelayMin)
                self.trackbarSlider5.Maximum = int(FlangerEffect.DelayMax)
                self.trackbarSlider5.Value = int(temp.Delay)

                if (ChorusEffect.WaveSin == temp.Waveform):
                    self.radiobuttonRadioSine.Checked = True
                else:
                    self.radiobuttonTriangle.Checked = True
            
                if (FlangerEffect.PhaseNeg180 == temp.Phase):
                    self.radiobuttonRadioNeg180.Checked = True
                elif (FlangerEffect.PhaseNeg90 == temp.Phase):
                    self.radiobuttonRadioNeg90.Checked = True
                elif (FlangerEffect.PhaseZero == temp.Phase):
                    self.radiobuttonRadioZero.Checked = True
                elif (FlangerEffect.Phase90 == temp.Phase):
                    self.radiobuttonRadio90.Checked = True
                elif (FlangerEffect.Phase180 == temp.Phase):
                    self.radiobuttonRadio180.Checked = True

                self.groupboxFramePhase.Enabled = self.radiobuttonRadioNeg180.Enabled = self.radiobuttonRadioNeg90.Enabled =\
                self.radiobuttonRadioZero.Enabled = self.radiobuttonRadio90.Enabled = self.radiobuttonRadio180.Enabled =\
                self.groupboxFrameWaveform.Enabled = self.radiobuttonRadioSine.Enabled = self.radiobuttonTriangle.Enabled = True

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled =\
                self.trackbarSlider4.Enabled = self.trackbarSlider5.Enabled = True
            
            self.labelParamName1.Text = "Wet/Dry Mix (%)"
            self.labelParamValue1.Text = temp.WetDryMix.ToString()
            
            self.labelParamName2.Text = "Depth (%)"
            self.labelParamValue2.Text = temp.Depth.ToString()
            
            self.labelParamName3.Text = "Feedback (%)"
            self.labelParamValue3.Text = temp.Feedback.ToString()
            
            self.labelParamName4.Text = "Frequency (Hz)"
            self.labelParamValue4.Text = temp.Frequency.ToString()
            
            self.labelParamName5.Text = "Delay (ms)"
            self.labelParamValue5.Text = temp.Delay.ToString()          
        
        elif (clr.GetClrType(GargleEffect) == efftype) :
            temp = eff.AllParameters
            
            if (MoveControls):
                self.trackbarSlider1.Minimum = int(GargleEffect.RateHzMin)
                self.trackbarSlider1.Maximum = int(GargleEffect.RateHzMax)
                self.trackbarSlider1.Value = int(temp.RateHz)

                if (GargleEffect.WaveSquare == temp.WaveShape):
                    self.radiobuttonSquare.Checked = True
                else:
                    self.radiobuttonTriangle.Checked = True

                self.groupboxFrameWaveform.Enabled = self.radiobuttonSquare.Enabled = self.radiobuttonTriangle.Enabled = True

                self.trackbarSlider1.Enabled = True
            
            self.labelParamName1.Text = "Rate (Hz)"
            self.labelParamValue1.Text = temp.RateHz.ToString()     
        
        elif (clr.GetClrType(ParamEqEffect) == efftype) :
            temp = eff.AllParameters
            
            if (MoveControls):
                self.trackbarSlider1.Minimum = int(ParamEqEffect.CenterMin)
                self.trackbarSlider1.Maximum = int(ParamEqEffect.CenterMax)
                self.trackbarSlider1.Value = int(temp.Center)
                self.trackbarSlider2.Minimum = int(ParamEqEffect.BandwidthMin)
                self.trackbarSlider2.Maximum = int(ParamEqEffect.BandwidthMax)
                self.trackbarSlider2.Value = int(temp.Bandwidth)
                self.trackbarSlider3.Minimum = int(ParamEqEffect.GainMin)
                self.trackbarSlider3.Maximum = int(ParamEqEffect.GainMax)
                self.trackbarSlider3.Value = int(temp.Gain)

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled = True
            
            self.labelParamName1.Text = "Center Freq (Hz)"
            self.labelParamValue1.Text = temp.Center.ToString()
            
            self.labelParamName2.Text = "Bandwidth (Hz)"
            self.labelParamValue2.Text = temp.Bandwidth.ToString()
            
            self.labelParamName3.Text = "Gain (dB)"
            self.labelParamValue3.Text = temp.Gain.ToString()
        
        elif (clr.GetClrType(WavesReverbEffect) == efftype) :
            temp = eff.AllParameters
            
            if (MoveControls) :
                self.trackbarSlider1.Minimum = int(WavesReverbEffect.InGainMin)
                self.trackbarSlider1.Maximum = int(WavesReverbEffect.InGainMax)
                self.trackbarSlider1.Value = int(temp.InGain)
                self.trackbarSlider2.Minimum = int(WavesReverbEffect.ReverbMixMin)
                self.trackbarSlider2.Maximum = int(WavesReverbEffect.ReverbMixMax)
                self.trackbarSlider2.Value = int(temp.ReverbMix)
                self.trackbarSlider3.Minimum = int(1000 * WavesReverbEffect.ReverbTimeMin)
                self.trackbarSlider3.Maximum = int(1000 * WavesReverbEffect.ReverbTimeMax)
                self.trackbarSlider3.Value = int(1000 * temp.ReverbTime)
                self.trackbarSlider4.Minimum = int(1000 * WavesReverbEffect.HighFrequencyRtRatioMin)
                self.trackbarSlider4.Maximum = int(1000 * WavesReverbEffect.HighFrequencyRtRatioMax)
                self.trackbarSlider4.Value = int(1000 * temp.HighFrequencyRtRatio)

                self.trackbarSlider1.Enabled = self.trackbarSlider2.Enabled = self.trackbarSlider3.Enabled = self.trackbarSlider4.Enabled = True
            
            self.labelParamName1.Text = "In Gain (dB)"
            self.labelParamValue1.Text = temp.InGain.ToString()
            
            self.labelParamName2.Text = "Waves Reverb Mix (dB)"
            self.labelParamValue2.Text = temp.ReverbMix.ToString()
            
            self.labelParamName3.Text = "Waves Reverb Time (ms)"
            self.labelParamValue3.Text = temp.ReverbTime.ToString()
            
            self.labelParamName4.Text = "HighFreq RT Ratio (x:1)"
            self.labelParamValue4.Text = temp.HighFrequencyRtRatio.ToString()
        

    def timer1_Tick(self, sender, e):
        if self.applicationBuffer.Status.Playing:
            return
        else:
            self.timer1.Enabled = False
            self.buttonStop.Enabled = False
            self.buttonPlay.Enabled = True
            self.comboEffects.Enabled = True

            self.labelTextStatus.Text="Sound stopped."


    def MainForm_Closing(self, sender, e):
        if (not None is self.applicationBuffer):
            if (self.applicationBuffer.Status.Playing):
                self.applicationBuffer.Stop()

    def comboEffects_SelectedValueChanged(self, sender, e):
        """
        切換特效
        """
        description  = ''

        if None is self.applicationBuffer:            
            return

        temp = self.effectDescription[:]
        temp.append( EffectInfo())

        if (self.comboEffects.SelectedIndex == 0):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardChorusGuid
                description = "Chorus"
        elif (self.comboEffects.SelectedIndex == 1):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardCompressorGuid
                description = "Compressor"
        elif (self.comboEffects.SelectedIndex == 2):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardDistortionGuid
                description = "Distortion"

        elif (self.comboEffects.SelectedIndex == 3):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardEchoGuid
                description = "Echo"

        elif (self.comboEffects.SelectedIndex == 4):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardFlangerGuid
                description = "Flanger"

        elif (self.comboEffects.SelectedIndex == 5):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardGargleGuid
                description = "Gargle"

        elif (self.comboEffects.SelectedIndex == 6):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardWavesReverbGuid
                description = "Waves Reverb"

        elif (self.comboEffects.SelectedIndex == 7):
                temp[- 1].description.GuidEffectClass = DSoundHelper.StandardParamEqGuid
                description = "ParamEq"
             
        if (self.AddEffect(temp)) :
            self.effectDescription = temp[:]
            self.listboxEffects.Items.Add(description)            
            self.listboxEffects.SelectedIndex = int(self.listboxEffects.Items.Count - 1)

if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = MyForm()
    Application.Run(frm)