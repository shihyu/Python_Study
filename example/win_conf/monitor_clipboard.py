# -*- coding: utf-8 -*-


import win32con
import win32clipboard as w
import msvcrt
import re, codecs, sys,time
from datetime import datetime
import chardet


CF_HTML = w.RegisterClipboardFormat("HTML Format")
#CF_RTF  = w.RegisterClipboardFormat("Rich Text Format")

pattern = re.compile(r"(http|https|ftp)://[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(([0-9]{1,5})?/[^'\" <>]+)?")

class MonitorClipboard():
    def __init__(self):
        self.collection_links = []
        self.cache = {win32con.CF_TEXT: '', CF_HTML:'', win32con.CF_UNICODETEXT:''}

    def backupToFile(self, fn):
        '''
        備份蒐集的資料到檔案
        '''
        handle = codecs.open(fn, 'w', 'utf-8')
        for data in self.collection_links:
            result = chardet.detect(data)
            handle.write( data.decode(result['encoding']) )
            handle.write( u'\n')
        handle.close()
        print 'copy to %s' % fn        

    def run(self):
        """
        監聽剪貼簿
        """
        try:
            while 1:
                # hit any key to exit
                if msvcrt.kbhit():
                    ch = msvcrt.getch()
                    if ch == 'c':
                        fn = datetime.now().strftime("%Y%m%d%H%M%S")
                        self.backupToFile(fn)
                        self.collection_links=[]
                    elif ch == 'd':
                        self.collection_links=[]
                        print 'clear'
                    elif ch == 'q':    
                        sys.exit(0)

                # don't suck up a lot of CPU
                time.sleep(1)
                try:
                    w.OpenClipboard()
                    self._preParse( win32con.CF_TEXT )
                    self._preParse( CF_HTML )
                    self._preParse( win32con.CF_UNICODETEXT )                    
                finally:
                    w.CloseClipboard()
        except UnicodeDecodeError:
            self.backupToFile('program_error')
        except:
            self.backupToFile('program_end')

    def _preParse(self, fmt):
        """
        前處理
        """
        if not w.IsClipboardFormatAvailable(fmt):
            return
        
        data = w.GetClipboardData(fmt)
        # strip stuff after null terminator
        nullIndex = data.find('\0')
        if nullIndex != -1:
            data = data[:nullIndex]
        self.parse(fmt, data)

    def parse(self, fmt, data):
        """
        解析內容
        """
        # ignore if unchanged
        if data != self.cache[fmt]:
            self.cache[fmt] = data
            matches = pattern.finditer(data)

            for match in matches:
                if isinstance(match.group(0), unicode):
                    link = unicode(match.group(0)).encode('utf-8')
                else:
                    link = str(match.group(0))

                if not link in self.collection_links:
                    self.collection_links.append(link)
                    #print isinstance(link, unicode)
                    print link


if __name__ == '__main__':
    mc = MonitorClipboard()
    mc.run()



