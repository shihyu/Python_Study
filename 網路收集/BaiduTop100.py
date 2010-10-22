# -*- coding: gbk -*-

"""
�ٶ�MP3�¸�����ع���
ʹ�ö��߳������������ҳ�����ҵ��ĵ�һ��MP3�ļ�
Ϊ���õ����ļ����ؿ�һ��,ʹ��һ���������,������ֻά��5���߳�
ע��: �п������ز��ɹ�,��Ϊ�ٶȸ���URL��һ������Ч��
��������ٶ�MP3����ҳ��URL�ӽ��ܺ����޸���,Ҳ������ȷ��ȡURL��

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
        self.songs = [] # ÿһ��Ԫ�ض���[index,search_url,song_name,singer]�ĸ�ʽ
        self.limit = limit #ֻ����ǰ��Ķ����׸�
        self.base_folder = base_folder #���MP3�ļ���Ŀ¼

    def getSongs(self, page):
        """���¸�TOP100��ҳ���аѸ����������Ϣ��ȡ����"""
        reobj = re.compile(r'<td class="th">(\d+)\.</td>\s+<td><a href="(.*?)" target="_blank">(.*?)</a> \(<a href=".*?>(.*?)</a>\)</td>')
        for match in reobj.finditer(page):
            self.songs.append([int(match.group(1)),match.group(2),match.group(3),match.group(4)])

    def run(self):
        list_page = getContent(self.list_url)
        self.getSongs(list_page)
        task_list = []
        queue = Queue.Queue() #ʹ��һ������,��֤ÿ��ֻ���������߳�����
        for index,search_url,song_name,singer in self.songs: #���������100�׸�
            if index>self.limit:
                break
            if not os.access(self.base_folder+"/"+song_name+".mp3",os.F_OK): #�����ڵ�MP3�ļ�������
                task_list.append([search_url, song_name, singer, self.base_folder])
        task_list.reverse()
        while len(task_list)>0:
            for i in range(5): #ÿ���������5���߳�,ʹ�õ����ļ������ٶȸ���
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
        search_result = getContent(self.url) #������Ӧ���������ҳ
        reobj = re.compile(r'<tr>\s+<td class=tdn>\d+</td>\s+<td class=d><a href="(.*?)" title=".*?<td>[0-9\.]+ M</td>\s+<td>(.*?)</td>', re.DOTALL)
        for match in reobj.finditer(search_result): #����ȡ��������������MP3��ʽ������
            download_page_url = match.group(1)
            file_type = match.group(2)
            if file_type=="mp3":
                self._download(download_page_url)
                self.queue.task_done()
                return
        self.queue.task_done() #��һ������,��Ϊ�����ڵ�һҳ���Ҳ���MP3������,�����������������,�������߳�һֱ����

    def _download(self, download_page_url):
        """��MP3�ļ�������ҳ,���ܶ�Ӧ��URL�������ļ�������"""
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

    #�������������ǰٶ�MP3����ҳ�������ڽ���MP3��������ʹ�õ�
    #����ԭʼ����Ϊv773://AAA.635w1u086wq.q1/83z2or/ENELEI.03H
    #��Ҫ���ܳ�http://www.springmusic.cn/upload/090704.mp3��������
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
