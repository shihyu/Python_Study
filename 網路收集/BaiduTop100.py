# -*- coding: gbk -*-

"""
百度MP3新歌榜下载工具
使用多线程下载搜索结果页里面找到的第一个MP3文件
为了让单个文件下载快一点,使用一个任务队列,队列中只维护5个线程
注意: 有可能下载不成功,因为百度给的URL不一定是有效的
另外如果百度MP3下载页把URL加解密函数修改了,也不能正确提取URL了

copyright: yhustc <http://www.yhustc.com>
"""

import urllib, re
from threading import *
import Queue
import sys, os

def getContent(url):
    url = url.replace(" ","%20")
    u = urllib.urlopen(url)
    return u.read()

class BaiduSpider():
    def __init__(self, limit=20, base_folder="."):
        self.list_url = "http://list.mp3.baidu.com/list/newhits.html?id=1?top1"
        self.songs = [] # 每一个元素都是[index,search_url,song_name,singer]的格式
        self.limit = limit #只下载前面的多少首歌
        self.base_folder = base_folder #存放MP3文件的目录

    def getSongs(self, page):
        """在新歌TOP100的页面中把歌名与歌手信息提取出来"""
        reobj = re.compile(r'<td class="th">(\d+)\.</td>\s+<td><a href="(.*?)" target="_blank">(.*?)</a> \(<a href=".*?>(.*?)</a>\)</td>')
        for match in reobj.finditer(page):
            self.songs.append([int(match.group(1)),match.group(2),match.group(3),match.group(4)])

    def run(self):
        list_page = getContent(self.list_url)
        self.getSongs(list_page)
        task_list = []
        queue = Queue.Queue() #使用一个队列,保证每次只有最多五个线程运行
        for index,search_url,song_name,singer in self.songs: #这里面会有100首歌
            if index>self.limit:
                break
            if not os.access(self.base_folder+"/"+song_name+".mp3",os.F_OK): #不存在的MP3文件才下载
                task_list.append([search_url, song_name, singer, self.base_folder])
        task_list.reverse()
        while len(task_list)>0:
            for i in range(5): #每次最多启动5个线程,使得单个文件下载速度更快
                if len(task_list)==0:
                    break
                task = task_list.pop()
                queue.put(task)
                downloader = Downloader(queue)
                downloader.setDaemon(True)
                downloader.start()
            queue.join()

class Downloader(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        task = self.queue.get()
        self.url = task[0]
        self.song_name = task[1]
        self.singer = task[2]
        self.base_folder = task[3]

    def run(self):
        search_result = getContent(self.url) #歌名对应的搜索结果页
        reobj = re.compile(r'<tr>\s+<td class=tdn>\d+</td>\s+<td class=d><a href="(.*?)" title=".*?<td>[0-9\.]+ M</td>\s+<td>(.*?)</td>', re.DOTALL)
        for match in reobj.finditer(search_result): #到提取的下载链接中找MP3格式下载项
            download_page_url = match.group(1)
            file_type = match.group(2)
            if file_type=="mp3":
                self._download(download_page_url)
                self.queue.task_done()
                return
        self.queue.task_done() #这一句必须加,因为可能在第一页中找不到MP3的下载,必须结束这个任务才行,否则主线程一直阻塞

    def _download(self, download_page_url):
        """打开MP3文件的下载页,解密对应的URL后下载文件并保存"""
        download_page = getContent(download_page_url)
        mp3_url = self.getMP3Url(download_page)
        print self.song_name,self.singer
        print mp3_url
        urllib.urlretrieve(mp3_url,self.base_folder+"/"+self.song_name+".mp3")

    def getMP3Url(self, download_page):
        match = re.search(r'var sertim=(\d+),.*?B="(.*?)",A="";', download_page)
        sertim = int(match.group(1))
        B = match.group(2)
        return self._decode(sertim, B)

    #以下两个函数是百度MP3下载页面中用于解密MP3下载连接使用的
    #比如原始连接为v773://AAA.635w1u086wq.q1/83z2or/ENELEI.03H
    #需要解密成http://www.springmusic.cn/upload/090704.mp3才能下载
    def _K(self,O,L,M,I,F):
        for N in range(O,L+1):
            I[N]=N+M;
            F[N+M]=N

    def _decode(self,sertim, B):
        E=len(B)
        C=""
        I={}
        F={}
        J=sertim % 26
        if J==0:
            J = 1
        self._K(0,9,48,I,F)
        self._K(10,35,55,I,F)
        self._K(36,61,61,I,F)
        for D in range(E):
            A=B[D]
            if re.match(r"[A-Za-z0-9]\Z", A):
                H=F[ord(A)]-J;
                if(H<0):
                    H+=62
                A=chr(I[H])
            C += A
        return C

if len(sys.argv)<2:
    print """
    Usage: downloader.py folder [limit]
           folder: where to save these MP3 files
           limit: download how many TOP {limit} MP3, default 20
"""
    raw_input('Press enter to exit...')
else:
    base_folder = sys.argv[1]
    if len(sys.argv)<3:
        limit = 20
    elif int(sys.argv[2])>100:
        limit = 100
    else:
        limit = int(sys.argv[2])

    spider = BaiduSpider(limit,base_folder)
    spider.run()
