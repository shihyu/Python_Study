# -*- coding: cp950 -*-
'''
Proxy Pattern
'''

class IGiveGift:
    '''
    代理者介面
    '''
    def GiveDolls(self):
        pass
    def GiveFlowers(self):
        pass
    def GiveChocolate(self):
        pass

class SchoolGirl:
    def __init__(self, name):
        self.Name = name
        
class Pursuit(IGiveGift):
    '''
    追求者
    '''
    def __init__(self, girl):
        self.SchoolGirl = girl
        
    def GiveDolls(self):
        print '%s 送你洋娃娃' % self.SchoolGirl.Name
        
    def GiveFlowers(self):
        print '%s 送你鮮花' % self.SchoolGirl.Name
        
    def GiveChocolate(self):
        print '%s 送你巧克力' % self.SchoolGirl.Name
        
class Proxy(IGiveGift):
    '''
    代理者
    '''
    def __init__(self, girl):
        self.Pursuit = Pursuit(girl)
        
    def GiveDolls(self):
        self.Pursuit.GiveDolls()
        
    def GiveFlowers(self):
        self.Pursuit.GiveFlowers()
        
    def GiveChocolate(self):
        self.Pursuit.GiveChocolate()
        
if __name__ == '__main__':
    girl = SchoolGirl('李嬌嬌')
    daili = Proxy( girl )
    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()
    
    
    
