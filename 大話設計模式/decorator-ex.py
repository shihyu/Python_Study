# -*- coding: cp950 -*-
class Person:
    def __init__(self, name):
        self.name = name

    def Show(self):
        print '�˧ꪺ %s' % self.name

class Finery(Person):
    '''
    �A����H���O
    '''
    def __init__(self):
        self.component = None
    def Decorate(self, component):
        self.component = component

    def Show(self):
        if not self.component is None:
            self.component.Show()


class TShirts(Finery):
    def Show(self):
        print '��A'
        self.component.Show()
        
class BigTrouse(Finery):
    def Show(self):
        print '�Ǥl'
        self.component.Show()

class Sneakers(Finery):
    def Show(self):
        print '�c�l'
        self.component.Show()
        
if __name__ == '__main__':
    xc = Person('�p��')
    print '�Ĥ@�ظ˧�'
    pqx = Sneakers()
    kk = BigTrouse()
    dtx = TShirts()

    pqx.Decorate(xc)
    kk.Decorate(pqx)
    dtx.Decorate(kk)
    dtx.Show()
    
