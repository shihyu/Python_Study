#!/usr/bin/env python
#  移除七天前檔案
# Usage:
#   remove_files_older_than.py ./*.jpg
#
import sys
import glob
import stat
import os
import time

if len(sys.argv)<2:
    print "Need 1 argument!"
    sys.exit(-1)

expireDays = 7
fileList = glob.glob( sys.argv[1] )
print "Found %d files." % len(fileList)

currentTime = time.localtime()
deletedCount = 0
for filename in fileList:
    filestat = os.stat( filename )
    modifiedTime = time.localtime( filestat[ stat.ST_MTIME ] )
    diff=time.mktime( currentTime )-time.mktime( modifiedTime )
    if (diff/(60.0*60*24))>expireDays :
        print diff/(60.0*60*24)
        print "Remove %s, mtime=%s..." % (filename, time.strftime(
                    "%Y/%m/%d %H:%M:%S", modifiedTime ) )
        os.remove( filename )
        deletedCount=deletedCount+1

if deletedCount > 0:
    print "Remove %d files" % deletedCount
else:
    print "No files expired."
