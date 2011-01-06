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
        if cash_type == '正常收費':
            self.cs = CashNormal()
        elif cash_type == '滿 300 送 100':
            self.cs = CashReturn(300, 100)            
        elif cash_type == '打8折':
            self.cs = CashRebate(0.8)

    def GetResult(self, money):
        return self.cs.acceptCash(money)

    
if __name__ == '__main__':
    context = CashContext('正常收費')
    print context.GetResult(1000)

    context = CashContext('滿 300 送 100')
    print context.GetResult(1000)

    context = CashContext('打8折')
    print context.GetResult(1000)
    
