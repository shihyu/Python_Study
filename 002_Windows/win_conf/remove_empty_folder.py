# -*- coding: cp950 -*-
"""
Description: 移除空目錄

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import os
import shutil

target = r'F:\ScrapBook\data'
for d in os.listdir(target):
    path = os.path.join(target, d)
    if len(os.listdir(path)) == 0:
            print path
            
            shutil.rmtree( path)
