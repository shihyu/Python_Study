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
        print '具體類別 A 方法 1 實現'
    def PrimitiveOperation2(self):
        print '具體類別 A 方法 2 實現'
        
class ConcreteClassB(AbstractClass):
    def PrimitiveOperation1(self):
        print '具體類別 B 方法 1 實現'
    def PrimitiveOperation2(self):
        print '具體類別 B 方法 2 實現'
    
if __name__ == '__main__':
    c = ConcreteClassA()
    c.TemplateMethod()

    c = ConcreteClassB()
    c.TemplateMethod()    
