# -*- coding: cp950 -*-
"""
Description: �Q�� Windows �� findstr.exe �i���ɮץ���j�M

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import os
import sys
import re

"""
/S ���N�j�M�l�ؿ�
/N ��ܦ��
"""
keyword = 'import32.lib'
path = r'D:\MyProject\cwccpptest' 
cmd = 'findstr /S /N "%s" %s\*' % (keyword, path)
rule = re.compile('(.*):(\d+):(.*)')
#print cmd
p = os.popen( cmd )
for line in p:
    ret = rule.match(line).groups()
    print 'File: %s' % ret[0]
    print 'Line:%d' % int(ret[1])
    print 'Content:\n%s' % ret[2]
    print

