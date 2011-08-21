# -*- coding: utf-8 -*-

import os.path
import shutil
import sys
from xml.sax import make_parser, handler

reload(sys) 
sys.setdefaultencoding('utf-8') 

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)
    


class Step1(handler.ContentHandler):

    def __init__(self, title):
        self.fid = None
        self.title = title
    def startElement(self, name, attrs):
        # step 1: find title
        if name == 'RDF:Description' and attrs['NS1:title'] == self.title:
           self.fid = attrs['RDF:about']
            
class Step2(handler.ContentHandler):

    def __init__(self, fid):
        self.children = []
        self._req = False
        self.fid = fid
        
    def startElement(self, name, attrs):       
        # step 2: find children id
        if name == 'RDF:Seq' and attrs['RDF:about'] == self.fid:
            self._req = True
        elif self._req == True and name == 'RDF:li':
            self.children.append( attrs['RDF:resource'])

        #if name == 'RDF:Description' and attrs['RDF:about'] =='urn:scrapbook:item20110717234355':
        #    print attrs['NS1:id']
        #    print attrs['NS1:title']
        #    print attrs['NS1:source']
            
    def endElement(self, name):
        # step 2
        if self._req == True:
            if name == 'RDF:Seq':
                self._req = False
        pass        

class Step3(handler.ContentHandler):

    def __init__(self, children, target):
        self.children = children
        self.result = []
        self.target = target
        import codecs
        self.f = codecs.open( os.path.join(target, 'index.html'), 'w', 'utf-8')
        self.f.write('''<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
</head>
<body>
''')
    def startElement(self, name, attrs):       
        if name == 'RDF:Description' and attrs['RDF:about'] in self.children:
            src = os.path.join(scrapbook_root, 'data', attrs['NS1:id'])
            self.f.write('''
            <div>
                * <a href="data/%s/index.html">%s</a>[<a href="%s">Source</a>]
            </div>
            <br/>
            ''' % (attrs['NS1:id'], safe_unicode(attrs['NS1:title']), attrs['NS1:source']) )            
            #print src
            if os.path.exists(src):
                #
                try:
                    shutil.move(src, os.path.join(self.target, 'data', attrs['NS1:id']))
                except Exception as e:
                    #print '[error]', src, os.path.join(self.target, attrs['NS1:id'], 'data')
                    print e
                    pass
                

    def endDocument(self):
        self.f.write('''
</body>
</html>
''')        
        self.f.close()
        
tag=u'comic'
fd=r'd:\book_%s' % tag
scrapbook_root = u'E:\\software\\My Dropbox\\可攜軟體\\網路\\瀏覽器\\Firefox_Profiles\\24tfjcl7.F31\\ScrapBook' 
scrapbook_rdf = os.path.join(scrapbook_root, 'scrapbook.rdf')   
parser = make_parser()
handler = Step1(tag)
parser.setContentHandler(handler)
print scrapbook_rdf
parser.parse(scrapbook_rdf)
print handler.fid

handler = Step2(handler.fid)
parser.setContentHandler(handler)
parser.parse(scrapbook_rdf)
#print handler.children
print 'Found: ',len(handler.children)


if(not os.path.exists(fd)):
    os.makedirs( fd )
handler = Step3(handler.children, fd)
parser.setContentHandler(handler)
parser.parse(scrapbook_rdf)
#print handler.result

#parser.parse(r'F:\ScrapBook\scrapbook.rdf')
