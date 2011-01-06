'''
Single Factory 
'''

class OperationError(Exception):
    pass

class Operation:
    def __init__(self):
        self.NumberA = 0
        self.NumberB = 0
        
    def GetResult(self):
        return 0
    
class OperationAdd(Operation):
    def GetResult(self):
        return self.NumberA + self.NumberB
class OperationSub(Operation):
    def GetResult(self):
        return self.NumberA - self.NumberB    
class OperationMul(Operation):
    def GetResult(self):
        return self.NumberA * self.NumberB    
class OperationDiv(Operation):
    def GetResult(self):
        if self.NumberB == 0:
            raise OperationError
        return self.NumberA / self.NumberB    

class OperationFactory:
    '''

    '''
    @staticmethod
    def CreateOperation(operate):
        if operate == '+':
            op = OperationAdd()
        elif operate == '-':
            op = OperationSub()            
        elif operate == '*':
            op = OperationMul()            
        elif operate == '/':
            op = OperationDiv()            
        else:
            raise OperationError

        return op


if __name__ == '__main__':
    op = OperationFactory.CreateOperation('+')
    op.NumberA = 1
    op.NumberB = 2
    print op.GetResult()

    op = OperationFactory.CreateOperation('-')
    op.NumberA = 1
    op.NumberB = 2
    print op.GetResult()

    op = OperationFactory.CreateOperation('*')
    op.NumberA = 1
    op.NumberB = 2
    print op.GetResult()

    op = OperationFactory.CreateOperation('/')
    op.NumberA = 1
    op.NumberB = 2
    print op.GetResult()

    try:
        op = OperationFactory.CreateOperation('%')
        op.NumberA = 1
        op.NumberB = 2
        print op.GetResult()
    except OperationError:
        print 'op error'
    
    try:
        op = OperationFactory.CreateOperation('/')
        op.NumberA = 1
        op.NumberB = 0
        print op.GetResult()
    except OperationError:
        print 'op error'
