# -*- coding: cp950 -*-
'''
Facade Pattern
'''

class SubSystemOne:
    def MethodOne(self):
        print '�l�t�Τ�k1'

class SubSystemTwo:
    def MethodTwo(self):
        print '�l�t�Τ�k2'

class SubSystemThree:
    def MethodThree(self):
        print '�l�t�Τ�k3'

class SubSystemFour:
    def MethodFour(self):
        print '�l�t�Τ�k4'

class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def MethodA(self):        
        print 'method #1'
        self.one.MethodOne()        
        self.two.MethodTwo()        
        self.four.MethodFour()        
        
        
    def MethodB(self):
        print 'method #2'
        self.two.MethodTwo()
        self.three.MethodThree()        
if __name__ == '__main__':
    f = Facade()
    f.MethodA()
    f.MethodB()
