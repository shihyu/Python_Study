# -*- coding: cp950 -*-

class ObjectStructure:
    def __init__(self):
        self.elements = []

    def Attach(self, element):
        self.elements.append(element)

    def Detach(self, element):
        self.elements.remove(element)

    def Accept(self, visitor):
        for elem in self.elements:
            elem.Accept(visitor)
            
class Visitor:
    def VisitConcreteElementA(self,elem):
        pass
    def VisitConcreteElementB(self,elem):
        pass
        
class ConcreteVisitor1(Visitor):
    def VisitConcreteElementA(self,elem):
        print '%s 被 %s 存取' % (str(elem), str(self))
    
    def VisitConcreteElementB(self,elem):
        print '%s 被 %s 存取' % (str(elem), str(self))
    
    def __str__(self):
        return 'ConcreteVisitor1'
    
class ConcreteVisitor2(Visitor):    
    def VisitConcreteElementA(self,elem):
        print '%s 被 %s 存取' % (str(elem), str(self))
        
    def VisitConcreteElementB(self,elem):
        print '%s 被 %s 存取' % (str(elem), str(self))

    def __str__(self):
        return 'ConcreteVisitor2'
    
class Element:
    def Accept(self,visitor):
        '''
        抽象方法
        '''
        pass
    
class ConcreteElementA(Element):
    def Accept(self,visitor):
        visitor.VisitConcreteElementA(self)
    
    def OperatorA(self):
        pass

    def __str__(self):
        return 'ConcreteElementA'
    
class ConcreteElementB(Element):
    def Accept(self, visitor):
        visitor.VisitConcreteElementB(self)

    def OperatorA(self):
        pass

    def __str__(self):
        return 'ConcreteElementB'
    
if __name__ == '__main__':    
    o= ObjectStructure()
    o.Attach(ConcreteElementA())
    o.Attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    v2 = ConcreteVisitor2()

    o.Accept(v1)
    o.Accept(v2)
