# -*- coding: cp950 -*-
'''
Template Method Pattern
'''

class AbstractClass:
    def TemplateMethod(self):
        self.PrimitiveOperation1()
        self.PrimitiveOperation2()
        
    def PrimitiveOperation1(self):
        pass
    def PrimitiveOperation2(self):
        pass

class ConcreteClassA(AbstractClass):
    def PrimitiveOperation1(self):
        print '�������O A ��k 1 ��{'
    def PrimitiveOperation2(self):
        print '�������O A ��k 2 ��{'
        
class ConcreteClassB(AbstractClass):
    def PrimitiveOperation1(self):
        print '�������O B ��k 1 ��{'
    def PrimitiveOperation2(self):
        print '�������O B ��k 2 ��{'
    
if __name__ == '__main__':
    c = ConcreteClassA()
    c.TemplateMethod()

    c = ConcreteClassB()
    c.TemplateMethod()    
