#-*- coding: UTF-8 -*-
"""
Description: 批次更名
Example:
ren('E:\\test\\*.jpg', '(.*)(-fix)(.JPG)', '\\1\\3')

python rn.py --path E:\test\*.jpg --old (.*)(-fix)(.JPG) --new \1\3
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import glob
import re
import os
def ren(path, old, new):
    for f in glob.glob(path):
        t = f.split('\\')
        path = '\\'.join(t[:-1])
        fn = t[-1]
        new_fn= re.sub(old, new, fn)
        os.rename(f, '\\'.join( [ path, new_fn]) )

def printHelp():
    print "python rn.py --path regex --old regex --new regex"
    sys.exit(2)
    
if __name__ == '__main__':
  import getopt
  import sys
  try:
    opts, args = getopt.getopt(sys.argv[1:], '',
                               ['path=', 'old=', 'new='])
  except getopt.error, msg:
    printHelp()

  path, old, new = None, None, None
  
  for option, arg in opts:
    if option == '--path':
      path = arg
    elif option == '--old':
      old = arg
    elif option == '--new':
      new = arg

  if path is None or old is None or new is None:
     printHelp()    

  print path, old, new  
  ren(path, old, new)
