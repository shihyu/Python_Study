#-*- coding: UTF-8 -*-
"""
Description: 

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""
import string
content = file('lv2.data').read()
result = []
while(len(content)>0):
    c=content[0]
    v=string.count(content, c)
    if v==1:
        result.append(c)

    content =content.replace(c, '')
print ''.join(result)    

