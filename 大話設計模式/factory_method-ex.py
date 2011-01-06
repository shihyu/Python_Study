# -*- coding: cp950 -*-
'''
Factory Method Pattern
'''
class Nightingals:
    '''
    �n�B�溸
    '''
    def Sweep(self):
        print '���a'        
    def Wash(self):
        print '�~��'        
    def BuyRice(self):
        print '�R��'

class Undergraduate(Nightingals):
    def Sweep(self):
        print '���a #1'        
    def Wash(self):
        print '�~�� #1'        
    def BuyRice(self):
        print '�R�� #1'
    
class Volunteer(Nightingals):    
    def Sweep(self):
        print '���a #2'        
    def Wash(self):
        print '�~�� #2'        
    def BuyRice(self):
        print '�R�� #2'    

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
    
    
