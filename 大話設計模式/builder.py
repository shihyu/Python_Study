# -*- coding: cp950 -*-
'''
Builder Pattern
'''

class Director:
    def Construct(self, builder):
        builder.BuildPartA()
        builder.BuildPartB()      
    
class Builder:
    def BuildPartA(self):
        pass
    def BuildPartB(self):
        pass
    def GetResult(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()
        
    def BuildPartA(self):
        self.product.Add('零件A')
    def BuildPartB(self):
        self.product.Add('零件B')
        
    def GetResult(self):
        return self.product

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()
        
    def BuildPartA(self):
        self.product.Add('零件X')
    def BuildPartB(self):
        self.product.Add('零件Y')
        
    def GetResult(self):
        return self.product
    
class Product:
    def __init__(self):
        self.store = []
    def Add(self, item):
        self.store.append( item )

    def Show(self):
        print '產品建立---'
        for v in self.store:
            print v
if __name__ == '__main__':
    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()
    
    director.Construct(b1)
    p1 = b1.GetResult()
    p1.Show()
    
    director.Construct(b2)
    p2 = b2.GetResult()
    p2.Show()    
