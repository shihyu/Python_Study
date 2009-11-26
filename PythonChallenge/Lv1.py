#-*- coding: UTF-8 -*-
"""
Description: 

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""
data_1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
data_2 = "map"

def mymethod(data):
    result = []
    for c in data:
        v=ord(c)
        if 97<=v<=122:
            if v+2>122:
                v=v-26                                                                                                                       
            result.append(chr(v+2))        
        else:
            result.append(c)
    print ''.join(result)

def recommended(data):
    import string
    t=string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    print   string.translate(data, t)   

if __name__ == '__main__':
    mymethod(data_1)
    mymethod(data_2)
    
    recommended(data_1)
    recommended(data_2)    
