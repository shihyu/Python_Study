import re
f=file("h:\\cniv.dat")
regex = re.compile('(.*)[ ]([a-z]*\d+):(\d+)\t(.*)')

table = {}
for i,ln in enumerate(f):
    ret = regex.search(ln)
    if ret == None:
        print ln
        continue
    
    data_list = ret.groups()
    table[ data_list[0] ] = 1

#print len(table)
for key in table:
    print key
