# -*- coding: cp950 -*-
'''
布卡漫畫格式 .buka 檔案萃取

*.buka 存放在 /mnt/sdcard/ibuka/down/{漫畫序號}/*.buka
'''
import os, sys
out = None
i = 1

fn_buka = sys.argv[1] #"d:\\131126.buka"
target = sys.argv[2] #'d:\\'

'''
JPG
開頭 FFD8
結尾 FFD9

REF:
http://blog.blueshop.com.tw/yowcheng/archive/2007/08/01/51961.aspx
'''
with open(fn_buka, "rb") as f:
    byte = f.read(1)
    while byte != "":
        # begin
        if ord(byte) == 0xff:
            b2 = f.read(1)
            if ord(b2) == 0xd8:
                fn = os.path.join(target, '%03d.jpg' % i)
                print 'extracting %s' % fn
                out = open(fn, 'wb')
                out.write(chr(0xff))
                out.write(chr(0xd8))
                i+=1
                #print 'start'
            elif ord(b2) == 0xd9:
                out.write(chr(0xff))
                out.write(chr(0xd9))
                out.close()
                out = None
                #print 'close'
                #break
            else:
                if not out is None:
                    out.write(byte)
                    out.write(b2)
                    #print 'write'
            byte = f.read(1)
            continue
        else:
            if not out is None:
                out.write(byte)
                #print 'write #2'

        
            
        
           
        byte = f.read(1)
if not out is None:
    out.close()
