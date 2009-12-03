# -*- coding: cp950 -*-
"""
利用 ffmpeg 轉檔
"""
import os
program = 'ffmpeg.exe'
# convert to jpg
infile = ''
outfile = ''
cmd = '{0} -i "{1}" -f image2 -ss 1 -vframes 1 -s 280x200 -an "{2}" '.format(program, infile, outfile) 
#convert to flv
cmd = '{0} -i "{1}" -ar 22050 -ab 32 -f flv "{2}" '.format(program, infile, outfile) 
print cmd
