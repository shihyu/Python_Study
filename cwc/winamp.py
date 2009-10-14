# -*- coding: utf-8 -*-
"""
Description: 透過 Windows Message 操控 Winamp

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import win32gui
import win32api
import win32con

class Winamp():
    """
    控制 Winamp

    example:
    player = Winamp()
    player.start()
    """
    WC_STOP             = 40047
    WC_START            = 40045
    WC_PLAY_OR_PAUSE    = 40046
    WC_NEXT_TRACK       = 40048
    WC_PREVIOUS_TRACK   = 40044
    WC_CLOSE            = 40001       
    WC_RAISE_VOLUME     = 40058
    WC_LOWER_VOLUME     = 40059
    WC_TOGGLE_REPEAT    = 40022
    WC_TOGGLE_SHUFFLE   = 40023       
    WC_FAST_FORWARD     = 40148
    WC_FAST_REWIND      = 40144  
            
    def __init__(self):
        self.winamp=win32gui.FindWindow('Winamp v1.x', None)
        if(self.winamp == 0):
            raise ValueError, 'winamp not found'
    
    def _cmd(self, code):
        win32api.SendMessage(self.winamp, win32con.WM_COMMAND, code, 0)

    def start(self):
        """
        開始播放
        """
        self._cmd(Winamp.WC_START)

    def stop(self):
        """
        停止播放
        """
        self._cmd(Winamp.WC_STOP)

    def playOrPause(self):
        """
        播放或暫停
        """
        self._cmd(Winamp.WC_PLAY_OR_PAUSE)
    def prev(self):
        """
        上一首
        """
        self._cmd(Winamp.WC_PREVIOUS_TRACK)        
    def next(self):
        """
        下一首
        """
        self._cmd(Winamp.WC_NEXT_TRACK)
        

