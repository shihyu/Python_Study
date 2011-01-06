# -*- coding: cp950 -*-
'''
Strategy Pattern
'''

class Strategy:
    def AlgorithmInterface(self):
        pass

class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print '�t��k A ��{'
class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print '�t��k B ��{'
class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print '�t��k C ��{'
        
class Context:
    def __init__(self, strategy):
        self.strategy = strategy
        
    def ContextInterface(self):
        self.strategy.AlgorithmInterface()

if __name__ == '__main__':
    context = Context( ConcreteStrategyA() )
    context.ContextInterface()

    context = Context( ConcreteStrategyB() )
    context.ContextInterface()

    context = Context( ConcreteStrategyC() )
    context.ContextInterface()    
