#-*- coding: UTF-8 -*-
"""
Description: 下載 podcast 

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
Reference:
[1] http://www.hanselman.com/blog/DownloadPodcastsWithPowershell.aspx
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import urllib
import feedparser 
feed = feedparser.parse('http://feeds.feedburner.com/HanselminutesCompleteMP3')

def download_file(url, fn):
    pass

#feed['items'][0]['enclosures'][0]['url']
for item in feed['items']:
    try:
        url= item['enclosures'][0]['url']
        fn = url.split('/')[-1]
        print '%s => downloading' % fn        
        urllib.urlretrieve (url, fn)
    except:
        print '%s => igone' % url
        

    
