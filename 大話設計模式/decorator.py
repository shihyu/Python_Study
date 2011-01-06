# -*- coding: cp950 -*-
'''
Decorator Pattern
'''

class Component:
    def Operation(self):
        pass
    
class ConcreteComponent(Component):
    def Operation(self):
        print '具體操作'
        
class Decorator(Component):
    def __init__(self):
        self.component = None

    def SetComponent(self, component):
        self.component = component
        
    def Operation(self):
        if not self.component is None:
            self.component.Operation()
            
class ConcreteDecoratorA(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.addedState = ''
    def Operation(self):
        Decorator.Operation(self)
        self.addedState = 'New State'
        print '具體裝飾物件 A 的操作'
class ConcreteDecoratorB(Decorator):    
    def Operation(self):
        Decorator.Operation(self)
        self.AddedBehavior()
        print '具體裝飾物件 b 的操作'
    def AddedBehavior(self):
        pass

if __name__ == '__main__':
    c = ConcreteComponent()
    d1 = ConcreteDecoratorA()
    d2 = ConcreteDecoratorB()
    d1.SetComponent(c)
    d2.SetComponent(d1)
    d2.Operation()
