# -*- coding: cp950 -*-
'''
Prototype Pattern
'''
import copy

class Resume:
    def __init__(self, name):
        self.name = name
        self.sex = None
        self.age = None
        self.timeArea = None
        self.company = None
        
    def SetPersonalInfo(self, sex, age):
        self.sex =sex
        self.age = age
        
    def SetWorkExperience(self, timeArea, company):
        self.timeArea = timeArea
        self.company = company
        
    def Display(self):
        print '%s %s %s' % (self.name, self.sex, self.age)
        print '�u�@�g���G %s %s' % (self.timeArea, self.company)
        
    def Clone(self):
        return copy.deepcopy(self)



    
if __name__ == '__main__':
    a = Resume('�j��')
    a.SetPersonalInfo('�k', '29')
    a.SetWorkExperience('1998-2000', 'xx ���q')

    b = a.Clone()
    b.SetWorkExperience('2000-2006', 'yy ���q')

    c = a.Clone()
    c.SetPersonalInfo('�k', '24')    
    c.SetWorkExperience('1998-2003', 'zz ���q')

    a.Display()
    b.Display()
    c.Display()    
