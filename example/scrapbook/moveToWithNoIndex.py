# -*- coding: cp950 -*-
'''
找尋遺失 index.dat 的目錄
'''
import os.path
import glob
import os
import shutil

root_path = r'F:\ScrapBook\data'
for v in os.listdir(root_path):
    try:
        if not os.path.exists(os.path.join(root_path, v, 'index.dat')):
            shutil.move(os.path.join(root_path, v), os.path.join(r'f:\a', v))
            print v
    except:
        pass
#)
