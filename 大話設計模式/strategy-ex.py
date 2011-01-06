# -*- coding: cp950 -*-
'''
strategy + simple factory example
'''
import math

class CashSuper:
    def acceptCash(self, money):
        pass

class CashNormal(CashSuper):
    def acceptCash(self, money):
        return money

class CashReturn(CashSuper):
    def __init__(self, v, v2):
        self.moneyCondition = v
        self.moneyReturn = v2
        
    def acceptCash(self, money):
        if money > self.moneyCondition:
            return money - (math.floor(money/self.moneyCondition)*self.moneyReturn)
        return money

class CashRebate(CashSuper):
    def __init__(self, v):
        self.moneyRebate = v
        
    def acceptCash(self, money):
        return self.moneyRebate * money
    
class CashContext:
    def __init__(self, cash_type):
        self.cs = None
        if cash_type == '���`���O':
            self.cs = CashNormal()
        elif cash_type == '�� 300 �e 100':
            self.cs = CashReturn(300, 100)            
        elif cash_type == '��8��':
            self.cs = CashRebate(0.8)

    def GetResult(self, money):
        return self.cs.acceptCash(money)

    
if __name__ == '__main__':
    context = CashContext('���`���O')
    print context.GetResult(1000)

    context = CashContext('�� 300 �e 100')
    print context.GetResult(1000)

    context = CashContext('��8��')
    print context.GetResult(1000)
    
