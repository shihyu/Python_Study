# -*- coding: cp950 -*-
'''
Strategy Pattern
'''

class Strategy:
    def AlgorithmInterface(self):
        pass

class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print '演算法 A 實現'
class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print '演算法 B 實現'
class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print '演算法 C 實現'
        
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
