# -*- coding: utf-8 -*-
"""
Description: 批次匯入文章到 Google Sites
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"
import getopt

import os.path
import sys
import gdata.sites.client
import gdata.sites.data
import glob
import codecs
import logging
from docimport import *
from datetime import datetime
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
	return '<object width="480" height="385"><param name="movie" value="http://www.youtube.com/v/' + code + '?fs=1&amp;hl=zh_TW&amp;"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/Fe5BL8f81x0?fs=1&amp;hl=zh_TW" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed></object>'

def funpConv(url):
	pass

def _baseConvById(url, tag, id):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find(tag, id=id)))


def javaeyeConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find("table", id="forum_main")))

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
	return (soup.find('title').text, safe_str(soup.find('div', id='main')))

def cnblogConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find('div', id='postbody')))

def codeguruConv(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	return (soup.find('title').text, safe_str(soup.find('div', 'litcontent')))

class DocsImportWithUrl(DocsImport):
  def doIt(self, urls, parent_name = None):
    global log_file
    #print src
    parent = None    
    if not parent_name is None:
      # 取得上層 feed
      feed = self.client.GetContentFeed('https://sites.google.com/feeds/content/%s/%s?path=%s' %(self.dn, self.sn, parent_name))
      if len(feed.entry)>0:
         parent = feed.entry[0]


    for url in urls:
	    url = url.strip()	
	    if 	len(url) == 0:
		continue
	    
	    if not 'http://' in url and not 'https://' in url:
	       continue

	    print url	

			

	    try:
	        if 'www.youtube.com' in url:
		    html = YoutubeConv(url)
		    content = urllib.urlopen(url).read()
		    title = re.search('name="title" content="(.*)"', content).groups()[0]
		elif 'www.javaeye.com' in url:
		    title, html = javaeyeConv(url)	
		elif 'www.codeproject.com' in url:
		    title, html = codeprojectConv(url)
		elif 'msdn.microsoft.com' in url:
		    title, html = msdnConv(url)
		elif 'www.dotblogs.com.tw' in url:
		    title, html = dotblogConv(url)
		elif 'www.cnblogs.com' in url:
		    title, html = cnblogConv(url)		    
		elif 'www.codeguru.com' in url:
		    title, html = codeguruConv(url)
		else:
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
		      title = string.strip(filter_invalid_file_char(title))
		    except IndexError:
		      title = 'Untitle'
	    except:
		print 'download html error'
		log_file.write(url + "\n")
		continue	
	    			    	
	    #x =  soup.html.body
	    #print 
	    try:
	       link = self._import(title, html, parent)
	       print link
  	    except gdata.client.RequestError as ex:	
	       print ex
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
  
