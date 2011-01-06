# -*- coding: cp950 -*-
'''
Facade Pattern
'''

class SubSystemOne:
    def MethodOne(self):
        print '子系統方法1'

class SubSystemTwo:
    def MethodTwo(self):
        print '子系統方法2'

class SubSystemThree:
    def MethodThree(self):
        print '子系統方法3'

class SubSystemFour:
    def MethodFour(self):
        print '子系統方法4'

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
