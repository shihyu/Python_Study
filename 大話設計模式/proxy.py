# -*- coding: cp950 -*-
'''
Proxy Pattern
'''

class Subject:
    def Request(self):
        pass
    
class RealSubject(Subject):
    def Request(self):
        print '�u�ꪺ�ШD'
        
class Proxy(Subject):
    def __init__(self):
        self.realSubject = None
        
    def Request(self):
        if self.realSubject is None:
            self.realSubject = RealSubject()
            
        self.realSubject.Request()
        
if __name__ == '__main__':
    px = Proxy()
    px.Request()
    
