# -*- coding: cp950 -*-
"""
Description: 利用描述檔分割與合併PDF檔案
"""
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

from datetime import datetime
from urlparse import urljoin, urlparse
import os, urllib, sys, re, codecs, string, uuid, time
TARGET_FOLDER = 'c:\\a'

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 GTB7.1 (.NET CLR 3.5.30729)"

urllib._urlopener = AppURLopener()


htmlCodes = [
    ['&', '&amp;'],
    ['<', '&lt;'],
    ['>', '&gt;'],
    ['"', '&quot;'],
]
htmlCodesReversed = htmlCodes[:]
htmlCodesReversed.reverse()

def htc(m):
    return chr(int(m.group(1),16))

def urldecode(url):
    rex = re.compile('%([0-9a-hA-H][0-9a-hA-H])',re.M)
    return rex.sub(htc,url)

def htmlEncode(s, codes=htmlCodes):
    """ Returns the HTML encoded version of the given string. This is useful to
    display a plain ASCII text string on a web page."""
    for code in codes:
        s = s.replace(code[0], code[1])
    return s

def htmlDecode(s, codes=htmlCodesReversed):
    """ Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>. It is the inverse of htmlEncode()."""
    for code in codes:
        s = s.replace(code[1], code[0])
    return s

pre_id = ''
def create_index_dat(path, title, url, encoding='UTF-8'):
    """
    建立 index.dat
    """
    global pre_id
    while 1:
       did = datetime.now().strftime("%Y%m%d%H%M%S")
       if not did == pre_id: 
          pre_id = did
	  break
       time.sleep(1)
	
    template = u"""id	%s
type	
title	%s
chars	%s
icon	favicon.ico
source	%s
comment	
folder	Unknown""" %(did, unicode(title), encoding, url)
    index_dat = os.path.normpath(u'%s\\index.dat' % path)
    #print index_dat	
    #print template
    #open(index_dat, "wb").write(template)
    codecs.open(index_dat, 'w', 'utf-8').write(template)



def create_folder(fd):
    if(not os.path.exists(fd)):
        os.makedirs( fd )    

def path_combine(path1, path2):
    result = os.path.normpath(u"%s\\%s" % (path1, path2))
    return result

def filter_invalid_file_char(s):
    s = re.sub('[\r|\n|\t|\'|\\\\|&nbsp;]', '', s)	
    #s = s.replace('\n', '')
    return re.sub('[\\/:"*?<>|]+', '', s)	

def create_index_html(url):
    """
    下載網址解析相關資訊
    """
    # 下載網頁內容
    try:
	html = urllib.urlopen(url).read()
    except IOError:
	print "%s -- fail" % url	
	return

    #print html
    # 解析內文：編碼格式、標題, 相同網域的資源超連結(css/image/js/html)
    from BeautifulSoup import BeautifulSoup
    soup = BeautifulSoup(html)
    try:   
        title = soup.findAll({'title':True})[0].text
        title = string.strip(filter_invalid_file_char(title))
	title = htmlDecode(title)
    except IndexError:
        title = 'Untitle'
    
    try:
	print title
    except UnicodeEncodeError:
	print title.encode('utf-8')

    no = 1
    _title = title

    while(True):
	target_path = os.path.normpath("%s\\%s" % (TARGET_FOLDER, title))    
	if not os.path.exists(target_path):
	   break;
        title = "%s-%d" %(_title, no)
	no = no +1
    create_folder( target_path )
    
    #for tag in soup.findAll('meta'):
    #    print '>>',tag['content']

    links = {}

    def create_item(link, ext):
        if urlparse( link ).scheme == '':
 	    name = link.split('/')[-1]
	    if name == '':
		return
	    #print '>%s<' %name
	    if len(name.split('.'))==1 :
		name = u'%s.%s' %(name, ext)
	    name = filter_invalid_file_char(name)			
	    
	    if ext=='':
  	        rep_name = name		
	    else:
	        rep_name = uuid.uuid1().get_hex()	
	    #print "%s => %s" % (rep_name, ext)
	    
	    if not name in links:
	        links[name] = {'search':link, 'src': urljoin(url, link.encode('utf-8')), 'target': path_combine(target_path, rep_name) ,'replace': rep_name} 
    	
    for tag in soup.findAll(['link'], href=True):
        create_item( tag['href'], 'css' )

    for tag in soup.findAll(['script', 'img'], src=True):
	ext = ''
	if tag.name=='script':
	   ext = 'js'
        create_item( tag['src'], ext)
    


    #title='Google'
    encoding='UTF-8'    

    #下載資源超連結
    #TODO: 支援遞迴下載html
    #print links
    for key in links:
	link = links[key]
	#print link['target']
        urllib.urlretrieve(link['src'], link['target'])
        html = html.replace(link['search'].encode('utf-8'), link['replace'].encode('utf-8'))
        #html = html.replace('title', 'xxxxx')
        
    #儲存代換後的網頁內容成 index.html
    index_html = os.path.normpath('%s\\index.html' % target_path)
    open(index_html, "wb").write(html)
    
    return (target_path, title, encoding, links)

def scrapbook(url):
    ret = create_index_html(url)
    if ret is None:
	return;
    (target_path, title, encoding, links) = ret
    #print title,encoding
    create_index_dat(target_path, title, url, encoding)
     



if __name__ == '__main__':
    #url = sys.argv[1]
    urls=[	


    ]		
    total = len(urls)
    idx = 1
    for url in urls:
       print "(%d/%d) - %s " % (idx, total, url)
       scrapbook(url)
       idx = idx + 1