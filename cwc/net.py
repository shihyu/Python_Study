# -*- coding: utf-8 -*-
import re
def ip2value(ip):
    """
    IP 字串轉數值
    """
    regex =re.compile('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    r = regex.search(ip)
    if(r.group(0) == None):
        raise ValueError, "invalid format"

    def check_range(v):
        if(v>0 and v<256):
            pass
        else:
            raise ValueError, "invalid format"
        
    a=int(r.group(1))
    b=int(r.group(2))
    c=int(r.group(3))
    d=int(r.group(4))

    check_range(a)
    check_range(b)
    check_range(c)
    check_range(d)
    
    return a*(256**3)+b*256*256+c*256+d

print ip2value('72.167.124.214')
