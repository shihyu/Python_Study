# -*- coding: cp950 -*-
'''
Factory Method Pattern
'''
class Nightingals:
    '''
    南丁格爾
    '''
    def Sweep(self):
        print '掃地'        
    def Wash(self):
        print '洗衣'        
    def BuyRice(self):
        print '買米'

class Undergraduate(Nightingals):
    def Sweep(self):
        print '掃地 #1'        
    def Wash(self):
        print '洗衣 #1'        
    def BuyRice(self):
        print '買米 #1'
    
class Volunteer(Nightingals):    
    def Sweep(self):
        print '掃地 #2'        
    def Wash(self):
        print '洗衣 #2'        
    def BuyRice(self):
        print '買米 #2'    

class IFactory:
    def CreateNightingal(self):
        pass

class NightingalUndergraduateFactory(IFactory):
    def CreateNightingal(self):    
        return Undergraduate()
    
class VolunteerFactory(IFactory):
    def CreateNightingal(self):
        return Volunteer()
        
if __name__ == '__main__':
    factory = NightingalUndergraduateFactory()
    person = factory.CreateNightingal()
    person.BuyRice()
    person.Wash()
    person.Sweep()    
    
    
