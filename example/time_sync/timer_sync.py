# -*- coding: utf-8 -*-
"""
利用 Time Service 自動同步 Windows 的時間
"""
import socket
import re
import os
from datetime import timedelta, datetime

server = 'time.nist.gov'
port = 13
GMT  = 8

# 取得目前時間資訊
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (server, port) )
data = s.recv(1024)
s.close()

# 解析轉換成系統時間格式
r = re.compile('(\d\d-\d\d-\d\d \d\d:\d\d:\d\d)')
ret = r.search(data)
date_str = ret.group(0)

dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")

dt += timedelta(hours=GMT)
d_str = dt.strftime("%Y-%m-%d")
t_str = dt.strftime("%H:%M:%S")

# 更新 Windows 系統時間
os.system( ('date %s' % d_str ))
os.system( ('time %s' % t_str ))
