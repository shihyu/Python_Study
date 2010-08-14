import glob
import split
import sys

if __name__ == '__main__' :
    fn = sys.argv[1]
    for fn in glob.glob(fn):
        print fn    
        split.split_rmvb(fn)


