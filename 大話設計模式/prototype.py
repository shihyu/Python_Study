# -*- coding: cp950 -*-
'''
Prototype Pattern
'''
import copy

class Prototype:
    '''
    
    '''
    def __init__(self, id):
        self.id = id

    def clone(self):
        pass

class ConcretePrototype1(Prototype):
    def clone(self):
        return copy.deepcopy(self)

    
if __name__ == '__main__':
    p1 = ConcretePrototype1(123)
    c1 = p1.clone()
    print c1.id
    c1.id = 999
    print c1.id    
    print p1.id
    
    
