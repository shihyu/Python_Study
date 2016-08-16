# -*- coding: utf-8 -*-
"""
Description: 批次匯入文章到 Google Sites
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"
#import getopt

import os.path
import gdata.sites.client
import gdata.sites.data
#import glob
import codecs
#import logging
from docimport import *
#from datetime import datetime
from urlparse import urljoin, urlparse
import os, urllib, sys, re, codecs, string
from BeautifulSoup import BeautifulSoup
import chardet


class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 GTB7.1 (.NET CLR 3.5.30729)"

urllib._urlopener = AppURLopener()

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)
def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

def filter_invalid_file_char(s):
    s = re.sub('[\r|\n]', '', s)	
    #s = s.replace('\n', '')
    return re.sub('[\\/:"*?<>|]+', '', s)	

def YoutubeConv(url):
	import re
	code = re.search("v=([a-zA-Z0-9_\-]+)", url).groups()[0]
	content = urllib.urlopen(url).read()
	title = re.search('name="title" content="(.*)"', content).groups()[0]
	html = '<object width="480" height="385"><param name="movie" value="http://www.youtube.com/v/' + code + '?fs=1&amp;hl=zh_TW&amp;"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/Fe5BL8f81x0?fs=1&amp;hl=zh_TW" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed></object>'
	return (title, html)

def funpConv(url):
	html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        url = soup.find('div', 'title').find('a')['href']
        Conv, url = dispatch(url)
        return Conv(url)

def _baseConvById(url, tag, id):
	html = urllib.urlopen(url).read()
	html = safe_str(html)
	result = chardet.detect(html) 
	print result
	html = html.decode( result['encoding'], 'replace' )     	
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find(tag, id=id)))

def _baseConvByClass(url, tag, class_name, encoding=None):
	html = urllib.urlopen(url).read()
	html = safe_str(html)

	if encoding is None:
            result = chardet.detect(html) 
            print result
            html = html.decode( result['encoding'], 'replace' )
        else:
            html = html.decode( encoding, 'replace')            

	soup = BeautifulSoup(html)

	import types
	html = None
	if isinstance(class_name, types.StringType):
            html = soup.find(tag, class_name)
        else:
            for v in class_name:
                html = soup.find(tag, v)
                if not html is None:
                    break
        
	return (soup.find('title').text, safe_str(html))

def javaeyeConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	block = soup.find("table", id="forum_main")
	if block is None:
            block = soup.find("div", id='news_content')

	return (soup.find('title').text, safe_str(block))

def codeprojectConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find('form', id='aspnetForm')))

def msdnConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find('div', id='MainContent')))

def dotblogConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	html = soup.find('div', id='main')
	if html is None:
            for v in ('entrybody', 'content'):
                html = soup.find('div', id=v)
                if not html is None:
                    break

        if html is None:
            for v in ('postText','note'):
                html = soup.find('div', v)
                if not html is None:
                    break                        
            
	return (soup.find('title').text, safe_str(html))

def cnblogConv(url):
        return _baseConvByClass(url, 'div', ('postbody', 'post', 'singlepost'))

def codeguruConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find('div', 'litcontent')))

def yamConv(url):
        return _baseConvByClass(url, 'div', ('post_content', 'articleBody'))
    
def defaultConv(url):
	html = urllib.urlopen(url).read()
	html = safe_str(html)
	result = chardet.detect(html) 
	print result
	html = html.decode( result['encoding'], 'replace' ) 
	title = re.search('<title>(.*)</title>', html, re.IGNORECASE | re.MULTILINE)

	try:   	      
		if title is None:
			title = 'Untitle'
		else:
			title = title.group(1)
	except IndexError:
		title = 'Untitle'

	return (title, html)
def poloConv(url):
    return _baseConvById(url, 'div', 'content_all')

def blogspot(url):
    	return _baseConvByClass(url, 'div', ('post-body', 'entry'), 'utf-8')

def pixnet(url):
    return _baseConvByClass(url, 'div', 'article-content')

def WretchConv(url):
        '''
        圖片無法正常呈現
        '''
	html = urllib.urlopen(url).read()	
        html = html.decode( 'utf-8', 'replace')
	soup = BeautifulSoup(html)	

        return (soup.find('title').text, safe_str(soup.find('div', 'articletext')))

def googleQConv(url):
        url = url.replace('http://www.google.com/url?q=', '')
        tmp = url.split('&')
        if len(tmp)>0:
            url = tmp[0]
            
        url = urllib.unquote(url)
        Conv, url = dispatch(url)
        return Conv(url)

def blogJava(url):
    return _baseConvByClass(url, 'div', 'post')

def xbeta(url):
    return _baseConvByClass(url, 'div', 'post1')

g_url_map = {
    'www.youtube.com': YoutubeConv,
    'www.javaeye.com': javaeyeConv,
    'www.codeproject.com': codeprojectConv,
    'msdn.microsoft.com':msdnConv,
    'www.dotblogs.com.tw':dotblogConv,
    'www.cnblogs.com':cnblogConv,
    'www.codeguru.com':codeguruConv,
    '.blogspot.com/':blogspot,
    '.pixnet.net/':pixnet,
    'http://funp.com/':funpConv,
    'http://xbeta.info':xbeta,
    'http://blog.xuite.net':poloConv,
    'http://www.wretch.cc':WretchConv,
    'http://blog.yam.com':yamConv,
    'http://www.blogjva.net':blogJava,
    'http://www.google.com/url?q=':googleQConv
}

def dispatch(url):
    global g_url_map

    print url				
    ConvFunc = defaultConv

    for v in g_url_map:
        if v in url:
            ConvFunc = g_url_map[v]
            break
    
    return (ConvFunc, url)
    
class DocsImportWithUrl(DocsImport):
  def doIt(self, urls, parent_name = None):
    global log_file
    parent = None    
    if not parent_name is None:
      feed = self.client.GetContentFeed('https://sites.google.com/feeds/content/%s/%s?path=%s' %(self.dn, self.sn, parent_name))
      if len(feed.entry)>0:
         parent = feed.entry[0]

    total = len(urls)
    i = 0
    i2 = 0
    for url in urls:
        try:
            i += 1            
            print "success=%d(%d/%d)" % (i2, i, total)            
            if i2 > 500:
                raise Exception('over 500')     
            
            url = url.strip()
            if 	len(url) == 0:
                continue
            
            if not 'http://' in url and not 'https://' in url:
               continue
            
            ConvFunc, url = dispatch(url)
            
            title,html = ConvFunc(url)
            if html is None or html == 'None':
                raise Exception ('content is None')

            if title == '' or title is None or title =='None':
                title = 'Untitle'
            
            html = ('<div><a href="%s">link</a></div>' % url) + html
            
            title = string.strip(filter_invalid_file_char(title))	
            link = self._import(title, html, parent)
            print link
            i2 += 1
             
        except gdata.client.RequestError as ex:
            print ex
            log_file.write(url + "\n")
        except Exception, ex :
            print ex
            #print 'download html error'
            log_file.write(url + "\n")

	    			    	
log_file = None
if __name__ == '__main__':
	_, name, pwd, url, file = sys.argv

	sn,dn,pn = parseSiteUrl( url  )
	log_file = open('error_' + file, 'w')	
	src = open(file).readlines()

	a = DocsImportWithUrl(site_name=sn, domain=dn)
	a.login(name, pwd)
	a.doIt(src, pn) 
	log_file.close()	
	print 'finish'

