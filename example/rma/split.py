# -*- coding: cp950 -*-
"""

@see http://www.ouyaoxiazai.com/article/24/311.html
"""
import os
import re
import string
import sys

S=1000
M=60*S
H=60*M
D=24*H

RMA_EXE = "rma.exe"
RMEDITOR_EXE = "rmeditor.exe"

def ts2str(ts):
    """
    timestamp 轉 DD:HH:MM:SS.mmm 格式
    """    
    d = ts /D
    t = ts %D

    h = t /H
    t = t %H

    m = t /M
    t = t %M

    s = t /S
    t = t %S

    
    return "%02d:%02d:%02d:%02d.%03d" % (d, h, m, s, t)

def split_ts(total_ts, clip_size=1200000 ):
    M1 = clip_size
    seg = total_ts / M1
    seg_m = total_ts % M1
    split_seg = []
    for i in range(0, seg):
        bt = i * M1
        et = (i+1)*M1
        split_seg.append(
            {
                "sn": i,
                "bt": ts2str(bt),
                "et": ts2str(et)
            }
        )
        

    if seg_m > 0:
        bt = et
        et = total_ts
        split_seg.append(
            {
                "sn": i+1,
                "bt": ts2str(bt),
                "et": ts2str(et)
            }
        )        


    return split_seg

def extract_ts(fn):
    """
    萃取影片資訊
    """
    cmd = "%s -db \"%s\"" % (RMA_EXE, fn)
    x = os.popen( cmd ).read()
    v = re.search('(\d*) ms', x).group(1)
    return string.atoi(v)

def split_rmvb(fn, clip_minutes = 1200):
    """
    分割
    """
    ts = extract_ts(fn)
    seg_ts = split_ts(ts, clip_minutes *S)
    name,ext=os.path.splitext(fn)
    cmd_list = []
    for seg in seg_ts:
        ofn= "%s-clip%d%s" % (name, seg['sn'],ext)
        cmd = "%s -i \"%s\" -o \"%s\" -s %s -e %s" % (RMEDITOR_EXE, fn, ofn, seg['bt'], seg['et'])
        cmd_list.append( cmd)
        #print cmd
        #print os.popen(cmd).read()
    fo =open("test.bat", "w")
    fo.write('\r\n'.join(cmd_list))
    fo.close()
    
    os.system("test.bat")

if __name__ == '__main__' :
    fn = sys.argv[1]
    if os.path.exists(fn):
        split_rmvb(fn)
    else:
        print 'file not exists'
    
    #split_rmvb("d:\\rma\\_20090717.rmvb")








