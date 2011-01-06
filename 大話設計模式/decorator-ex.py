# -*- coding: cp950 -*-
class Person:
    def __init__(self, name):
        self.name = name

    def Show(self):
        print '裝扮的 %s' % self.name

class Finery(Person):
    '''
    服飾抽象類別
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
        print '衣服'
        self.component.Show()
        
class BigTrouse(Finery):
    def Show(self):
        print '褲子'
        self.component.Show()

class Sneakers(Finery):
    def Show(self):
        print '鞋子'
        self.component.Show()
        
if __name__ == '__main__':
    xc = Person('小菜')
    print '第一種裝扮'
    pqx = Sneakers()
    kk = BigTrouse()
    dtx = TShirts()

    pqx.Decorate(xc)
    kk.Decorate(pqx)
    dtx.Decorate(kk)
    dtx.Show()
    
