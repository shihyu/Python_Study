#-*- coding: UTF-8 -*-
"""
�Q�� Google Translate ½Ķ
"""
import urllib,urllib2
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.result = []
        self.open = False
    def start_div(self, attrs):
        id = [v for k, v in attrs if k=='id']
        if 'result_box' in id:
            self.open = True
    def handle_data(self, text):
        if self.open:
            self.result.append(text)
            self.open = False

while True:
    text = raw_input("�п�J�n½Ķ���^��(�h�X��Jq)�G")
    if text=='q':
        break;
    values={'hl':'zh-TW','ie':'utf8','text':text,'langpair':"en|zh-TW"}
    url='http://translate.google.cn/translate_t'
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    req.add_header('User-Agent', "Mozilla/5.0+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)")
    response = urllib2.urlopen(req)
    parser = URLLister()
    parser.feed(response.read())
    parser.close()
    print "½Ķ���G:"
    for i in parser.result:
        i = unicode(i,'utf-8').encode('gbk');
        print i