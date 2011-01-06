# -*- coding: cp950 -*-
'''
State Pattern
'''

class Context:
    def __init__(self, state):
        self._State = state
        
    def Request(self):
        self._State.Handle(self)


    def getState(self):
        return self._State
    

    def setState(self, value):
        print '新狀態 %s' % value.name
        self._State = value

    State = property( getState, setState)
    
class State:
    def Handle(self, context):
        pass

class ConcreteStateA(State):
    def __init__(self):
        self.name = 'A'  
    def Handle(self, context):
        context.State = ConcreteStateB()
        
class ConcreteStateB(State):
    def __init__(self):
        self.name = 'B'  
    def Handle(self, context):
        context.State = ConcreteStateA()    

if __name__ == '__main__':
    c = Context( ConcreteStateA() )
    c.Request()
    c.Request()
    c.Request()
    c.Request()

    print 'ok'
