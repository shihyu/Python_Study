# -*- coding: cp950 -*-
"""
Description: 檢測密碼強度

Reference:
[1] http://www.cnblogs.com/homezzm/archive/2009/12/01/1614477.html

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

def char_mode(iN):
    if 48 <= iN <=57: #數字    
        return 1

    if 65 <= iN <=90: #大寫字母    
        return 2

    if 97 <= iN <=122: #小寫    
        return 4
    else:    
        return 8 #特殊字符       

def bit_to_total(num):
    """
    計算模式組合
    """
    modes = 0
    for i in range(0, 4):
        if num & 1 > 0:
            modes += 1

        num = num >> 1
    
    return modes

def chk_strong(s):
    if len(s)<=4:
        return 0

    modes = 0
    for c in s:
        modes = modes | char_mode( ord(c) )

    return bit_to_total(modes)


print chk_strong('135a_792468')
    
