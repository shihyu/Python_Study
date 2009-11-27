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

from System import *
from System.IO import *
from System.Windows.Forms import *
from System.Drawing import *
from Microsoft.DirectX import *
from Microsoft.DirectX.DirectSound import *

class MyForm(Form):
    def __init__(self):
        self.PathSoundFile = ''
        self.ApplicationBuffer = None
        self.ApplicationDevice = None

        self.InitializeComponent()

    def _Form1_Load(self, sender, e):
        try:
            self.ApplicationDevice = Device()
            self.ApplicationDevice.SetCooperativeLevel(self, CooperativeLevel.Priority)
        except:
            MessageBox.Show("Unable to create sound device. Sample will now exit.")
            self.Close()

    def Dispose(self, disposing):              
        super(type(self), self).Dispose(disposing)    

    def InitializeComponent(self):
        self.btnSoundfile = Button();
        self.lblFilename = Label();
        self.cbLoopCheck = CheckBox();
        self.btnPlay = Button();
        self.btnStop = Button();
        self.btnCancel = Button();

        self.SuspendLayout()

        # 
        # btnSoundfile
        # 
        self.btnSoundfile.Location = Point(10, 11);
        self.btnSoundfile.Name = "btnSoundfile";
        self.btnSoundfile.Size = Size(69, 21);
        self.btnSoundfile.TabIndex = 0;
        self.btnSoundfile.Text = "Sound &file...";
        self.btnSoundfile.Click += self.btnSoundfile_Click
        # 
        # lblFilename
        # 
        self.lblFilename.BorderStyle = BorderStyle.Fixed3D;
        self.lblFilename.Location = Point(94, 11);
        self.lblFilename.Name = "lblFilename";
        self.lblFilename.Size = Size(345, 21);
        self.lblFilename.TabIndex = 1;
        self.lblFilename.Text = "No file loaded.";
        self.lblFilename.TextAlign = ContentAlignment.MiddleLeft;
        # 
        # cbLoopCheck
        # 
        self.cbLoopCheck.Enabled = False;
        self.cbLoopCheck.Location = Point(9, 44);
        self.cbLoopCheck.Name = "cbLoopCheck";
        self.cbLoopCheck.Size = Size(87, 16);
        self.cbLoopCheck.TabIndex = 2;
        self.cbLoopCheck.Text = "&Loop sound";
        # 
        # btnPlay
        # 
        self.btnPlay.Enabled = False;
        self.btnPlay.Location = Point(104, 48);
        self.btnPlay.Name = "btnPlay";
        self.btnPlay.TabIndex = 3;
        self.btnPlay.Text = "&Play";
        self.btnPlay.Click += self.btnPlay_Click
        # 
        # btnStop
        # 
        self.btnStop.Enabled = False;
        self.btnStop.Location = Point(176, 48);
        self.btnStop.Name = "btnStop";
        self.btnStop.TabIndex = 4;
        self.btnStop.Text = "&Stop";
        self.btnStop.Click += self.btnStop_Click
        # 
        # btnCancel
        # 
        self.btnCancel.Location = Point(364, 48);
        self.btnCancel.Name = "btnCancel";
        self.btnCancel.TabIndex = 5;
        self.btnCancel.Text = "E&xit";
        self.btnCancel.Click += self.btnCancel_Click

        # Form
        self.AcceptButton = self.btnSoundfile;
        self.ClientSize = Size(470, 77)
        self.Controls.AddRange( Array[Control] ([ self.btnSoundfile, self.lblFilename, self.cbLoopCheck, self.btnPlay, self.btnStop, self.btnCancel ]) );

        self.Name = 'MainForm'
        self.Text = 'PlaySound'
        self.Load += self._Form1_Load

        self.ResumeLayout(False)

    def btnSoundfile_Click(self, sender, e):
        ofd = OpenFileDialog()
        ofd.InitialDirectory = self.PathSoundFile
        ofd.Filter=  "Wave files(*.wav)|*.wav"

        # Stop the sound if it's already playing before you open the the dialog
        if (not self.ApplicationBuffer is None):
            self.ApplicationBuffer.Stop()

        if( DialogResult.Cancel == ofd.ShowDialog() ):
            return
           
        if(self.LoadSoundFile(ofd.FileName)):
            self.PathSoundFile = Path.GetDirectoryName(ofd.FileName)
            self.lblFilename.Text = Path.GetFileName(ofd.FileName)
            self.EnablePlayUI(True)
        else:
            self.lblFilename.Text = "Could not create sound buffer."
            self.EnablePlayUI(False);

    def LoadSoundFile(self, name):
        try:
            print name
            self.ApplicationBuffer = SecondaryBuffer(name, self.ApplicationDevice)
        except:
            return False;

        return True;

    def EnablePlayUI(self, enable):
        if (enable):
            self.cbLoopCheck.Enabled = True
            self.btnPlay.Enabled = True
            self.btnStop.Enabled = True
        else:
            self.cbLoopCheck.Enabled = False
            self.btnPlay.Enabled = False
            self.btnStop.Enabled = False

    def btnStop_Click(self, sender, e):
        if not None is self.ApplicationBuffer:
            self.ApplicationBuffer.Stop()

    def btnPlay_Click(self, sender, e):
        if not None is self.ApplicationBuffer:
            self.ApplicationBuffer.Play(0, BufferPlayFlags.Looping if self.cbLoopCheck.Checked else BufferPlayFlags.Default)

    def btnCancel_Click(self, sender, e):
        self.Close()

if __name__ == '__main__':
    Application.EnableVisualStyles()
    Application.SetCompatibleTextRenderingDefault(False)
    frm = MyForm()
    Application.Run(frm)