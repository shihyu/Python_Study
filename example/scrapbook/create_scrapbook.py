# -*- coding: cp950 -*-
"""
Description: �Q�δy�z�ɤ��λP�X��PDF�ɮ�
"""
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

from datetime import datetime
from urlparse import urljoin, urlparse
import os, urllib, sys, re, codecs, string
TARGET_FOLDER = 'c:\\a'

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 GTB7.1 (.NET CLR 3.5.30729)"

urllib._urlopener = AppURLopener()

def create_index_dat(path, title, url, encoding='UTF-8'):
    """
    �إ� index.dat
    """
    did = datetime.now().strftime("%Y%m%d%H%M%S")
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
    s = re.sub('[\r|\n]', '', s)	
    #s = s.replace('\n', '')
    return re.sub('[\\/:"*?<>|]+', '', s)	

def create_index_html(url):
    """
    �U�����}�ѪR������T
    """
    # �U���������e
    html = urllib.urlopen(url).read()
    #print html
    # �ѪR����G�s�X�榡�B���D, �ۦP���쪺�귽�W�s��(css/image/js/html)
    from BeautifulSoup import BeautifulSoup
    soup = BeautifulSoup(html)
    try:   
        title = soup.findAll({'title':True})[0].text
        title = string.strip(filter_invalid_file_char(title))
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
	    if len(name.split('.'))==1 :
		name = u'%s.%s' %(name, ext)
	    name = filter_invalid_file_char(name)			
	    if not name in links:
	        links[name] = {'search':link, 'src': urljoin(url, link.encode('utf-8')), 'target': path_combine(target_path, name) ,'replace': name} 
    	
    for tag in soup.findAll(['link'], href=True):
        create_item( tag['href'], 'css' )

    for tag in soup.findAll(['script', 'img'], src=True):
	ext = ''
	if tag.name=='script':
	   ext = 'js'
        create_item( tag['src'], ext)
    


    #title='Google'
    encoding='UTF-8'    

    #�U���귽�W�s��
    #TODO: �䴩���j�U��html
    #print links
    for key in links:
	link = links[key]
	#print link['target']
        urllib.urlretrieve(link['src'], link['target'])
        html = html.replace(link['search'].encode('utf-8'), link['replace'].encode('utf-8'))
        #html = html.replace('title', 'xxxxx')
        
    #�x�s�N���᪺�������e�� index.html
    index_html = os.path.normpath('%s\\index.html' % target_path)
    open(index_html, "wb").write(html)
    
    return (target_path, title, encoding, links)

def scrapbook(url):
    (target_path, title, encoding, links) = create_index_html(url)
    #print title,encoding
    create_index_dat(target_path, title, url, encoding)
     


if __name__ == '__main__':
    #url = sys.argv[1]
    urls=[	
	'http://www.google.com'		
    ]		
    total = len(urls)
    idx = 1
    for url in urls:
       print "(%d/%d) - %s " % (idx, total, url)
       scrapbook(url)
       idx = idx + 1