# -*- coding: cp950 -*-
'''
Proxy Pattern
'''

class IGiveGift:
    '''
    �N�z�̤���
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
    �l�D��
    '''
    def __init__(self, girl):
        self.SchoolGirl = girl
        
    def GiveDolls(self):
        print '%s �e�A�v����' % self.SchoolGirl.Name
        
    def GiveFlowers(self):
        print '%s �e�A�A��' % self.SchoolGirl.Name
        
    def GiveChocolate(self):
        print '%s �e�A���J�O' % self.SchoolGirl.Name
        
class Proxy(IGiveGift):
    '''
    �N�z��
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
    girl = SchoolGirl('���b�b')
    daili = Proxy( girl )
    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()
    
    
    
