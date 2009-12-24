# -*- coding: utf-8 -*-
"""
Description: DirectSound 播放 wave 

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

from System.Windows.Forms import *
from System.Drawing import *
from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *

class MyForm(Form):
    def __init__(self):
        print 'constructor'
        self.InitializeComponent()

    def _Form1_Load(self, sender, e):
        print 'form_load'
        pass

    def Dispose(self, disposing):              
        super(type(self), self).Dispose(disposing)    

    def InitializeComponent(self):
        self.SuspendLayout()

        # do something
        self._button1 = Button()
        self._button1.Location = Point(66, 25)
        self._button1.Name = 'button1'
        self._button1.Size = Size(145, 38)
        self._button1.TabIndex = 0
        self._button1.Text = 'Play'
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self._button1_Click
        self.Controls.Add(self._button1)

        # Form
        self.ClientSize = Size(292, 273)
        self.Name = 'Form1'
        self.Text = 'Form1'
        self.Load += self._Form1_Load

        self.ResumeLayout(False)

    def _button1_Click(self, sender, e):
        # 播放
        playWav(self, "C:\\Program Files\\Microsoft SDKs\\Windows\\v6.1\\Samples\\NetDs\\Tapi\\Tapi3\\Cpp\\FileTerm\\Welcome.wav")
        pass


def playWav(frm, wav):
    """
    播放 wav
    """
    dev = Device()
    dev.SetCooperativeLevel(frm, CooperativeLevel.Normal)
    snd = SecondaryBuffer(wav, dev)
    snd.Play(0, BufferPlayFlags.Default)

if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = MyForm()
    Application.Run(frm)