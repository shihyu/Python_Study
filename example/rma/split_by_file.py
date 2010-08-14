# -*- coding: cp950 -*-
"""

@see http://www.ouyaoxiazai.com/article/24/311.html
"""
import os
import re
import string
import sys
import codecs


S=1000
M=60*S
H=60*M
D=24*H

RMA_EXE = "rma.exe"
RMEDITOR_EXE = "rmeditor.exe"
def parse_file(fn):
    plain_f = codecs.open(fn, 'r', 'utf-8')  
    file_struct = {'infile':'', 'seg': []}

    for i,line in enumerate(plain_f):
        if i == 0:
            infn = line = line.strip()
	    file_struct['infile'] = line
            continue
        
        if len(line)>0:
            if line.count('-')>0:
                begin, end=re.split('-', line)
		file_struct['seg'].append( {'st': begin, 'et': end} )


    return file_struct

def split_rmvb(ds):
    """
    分割
    """
    seg_ts = ds['seg'] #[{'st':'00:0:00:00', 'et':'00:0:00:00'}]
    name,ext=os.path.splitext(ds['infile'])
    fn = ds['infile']
    cmd_list = []
    i = 0
    for seg in seg_ts:
        ofn= "%s-clip%d%s" % (name, i, ext)
        cmd = "%s -i \"%s\" -o \"%s\" -s %s -e %s" % (RMEDITOR_EXE, fn, ofn, seg['st'], seg['et'])
        cmd_list.append( cmd)
	i+=1
        #print cmd
        #print os.popen(cmd).read()
    fo =open("split_by_file.bat", "w")
    fo.write('\r\n'.join(cmd_list))
    fo.close()
    
    os.system("split_by_file.bat")

if __name__ == '__main__' :
    fn = sys.argv[1]
    ds = parse_file(fn)

    if os.path.exists(fn):
        split_rmvb(ds)
    else:
        print 'file not exists'
    









