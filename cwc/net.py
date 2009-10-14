# -*- coding: utf-8 -*-
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import re

ip_regex =re.compile('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
def ip2value(ip):
    """
    IP 字串轉數值

    example:
    print ip2value('72.167.124.214') #1218936022
    """
    r = ip_regex.search(ip)
    if(r is None):
        raise ValueError, "invalid format"

    def check_range(v):
        v = int(v)
        if(v>0 and v<256):
            return v
        else:
            raise ValueError, "invalid format"
        
    a=check_range(r.group(1))
    b=check_range(r.group(2))
    c=check_range(r.group(3))
    d=check_range(r.group(4))
    
    return a*(256**3)+b*256*256+c*256+d


