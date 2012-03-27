# -*- coding: cp950 -*-
import xmlrpclib
import os.path
import os
import codecs
import traceback

name = ''
password = ''
#dir = './blogback'
url = 'https://storage.msn.com/storageservice/MetaWeblog.rpc'
number = 9999
encoding = 'cp936'

def main():
    #if not os.path.exists(dir):
    #    os.mkdir(dir)
            
    print 'Connecting to server – %s\n' % url
    server = xmlrpclib.Server(url)
        
    print 'Getting posts number = %d\n' % number
    result = server.metaWeblog.getRecentPosts('', name, password, number)
    num = 0
        
    for v in result:
        filename = os.path.normpath(os.path.join(dir, formateFilename(v['title']+'.htm')))
        v['date'] = getDateTime(v['dateCreated'])
        v['encoding'] = encoding
        print 'saving —- %s …' % filename
        try:
            try:
                fp = file(filename, 'wb')
                writer = codecs.lookup(encoding)[3](fp)
                writer.write(htmltemplate % v)
            except:
                traceback.print_exc()
        finally:
            fp.close()
        num += 1
    print '\nFinished! Total %d posts be saved!' % num

def getDateTime(d):
    a = str(d)
    return a[0:4]+'/'+a[4:6]+'/'+a[6:8]+'-'+a[9:]
        
def formateFilename(filename):
    s = r'/\<>?:*」|'
    f = ''
    for ch in filename:
        if ch in s:
            f += '%' + oct(ord(ch))
        else:
            f += ch
    return f
        
if __name__ == '__main__':
    main()
