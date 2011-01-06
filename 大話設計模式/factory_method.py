# -*- coding: cp950 -*-
'''
Factory Method Pattern
'''

class IFactory:
    '''
    工廠介面
    '''
    def CreateOperation(self):
        pass

class Operattion:
    def __init__(self):
        self.NumberA = 0
        self.NumberB = 0
        
class OperationAdd:
    def GetResult(self):
        return self.NumberA + self.NumberB

class OperationSub:
    def GetResult(self):
        return self.NumberA - self.NumberB

class OperationMul:
    def GetResult(self):
        return self.NumberA * self.NumberB

class OperationDiv:
    def GetResult(self):
        return self.NumberA / self.NumberB
    
class AddFactory(IFactory):
    def CreateOperation(self):
        return OperationAdd()

class SubFactory(IFactory):
    def CreateOperation(self):
        return OperationSub()

class MulFactory(IFactory):
    def CreateOperation(self):
        return OperationMul()

class DivFactory(IFactory):
    def CreateOperation(self):
        return OperationDiv()
        
if __name__ == '__main__':
    factory = AddFactory()
    op = factory.CreateOperation()
    op.NumberA = 3
    op.NumberB = 4
    print op.GetResult()
    
    
    
