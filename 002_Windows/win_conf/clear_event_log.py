# -*- coding: cp950 -*-
'''
�M��Windows�t�Τ��ƥ��x
'''
import win32evtlog

def KillEventLog(EventLogName):
    h = win32evtlog.OpenEventLog('', EventLogName)
    win32evtlog.ClearEventLog(h, None)
    win32evtlog.CloseEventLog(h)

if __name__ == '__main__':
    for v in ['OAlerts.evt', 'Application', 'System', 'Security', 'SecEvent.Evt', 'SysEvent.Evt', 'DnsEvent.Evt']:
        KillEventLog(v)
