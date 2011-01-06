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
        print '工作經歷： %s %s' % (self.timeArea, self.company)
        
    def Clone(self):
        return copy.deepcopy(self)



    
if __name__ == '__main__':
    a = Resume('大鳥')
    a.SetPersonalInfo('男', '29')
    a.SetWorkExperience('1998-2000', 'xx 公司')

    b = a.Clone()
    b.SetWorkExperience('2000-2006', 'yy 公司')

    c = a.Clone()
    c.SetPersonalInfo('男', '24')    
    c.SetWorkExperience('1998-2003', 'zz 公司')

    a.Display()
    b.Display()
    c.Display()    
