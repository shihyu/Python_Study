# -*- coding: utf-8 -*-
"""
Description: 將目錄的 jpg 列表建立成文字檔

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import glob
import codecs
out = codecs.open('d:\\a.txt', 'w', 'utf-8')
for fn in glob.glob("d:\\*.jpg"):
    out.write( u'%s\r\n' % fn )
out.close()
