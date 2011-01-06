# -*- coding: cp950 -*-
'''
Bridge
'''

class Abstraction:
    def SetImplementor(self, implementor):
        self.implementor = implementor
        
    def Operation(self):
        self.implementor.OperatorImp()

class RefinedAbstraction(Abstraction):
    def Operation(self):
        self.implementor.OperatorImp()

class Implementor:
    def OperatorImp(self):
        print 'op imp'

class ConcreteImplementorA(Implementor):
    def OperatorImp(self):
        print 'op imp #1'

class ConcreteImplementorB(Implementor):
    def OperatorImp(self):
        print 'op imp #2'

def RunDP():
    '''
    �з� Design Pattern ���յ{��
    '''
    r = RefinedAbstraction()

    imp = ConcreteImplementorA()    
    r.SetImplementor(imp)
    r.Operation()
    
    imp = ConcreteImplementorB()    
    r.SetImplementor(imp)
    r.Operation()    
#------------ example -------------
class HandsetSoft:
    '''
    ����n���H���O
    '''
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    '''
    ����C��
    '''
    def Run(self):
        print '�������C��'

class HandsetAddressList(HandsetSoft):
    '''
    ����q�T��
    '''    
    def Run(self):
        print '�������q�T��'        

class HandsetBrand:
    '''
    ����~�P
    '''
    def SetHandsetSoft(self, soft):
        self.soft = soft

    def Run(self):
        pass

class HandsetBrandN(HandsetBrand):
    '''
    ����~�PN
    '''
    def Run(self):
        self.soft.Run()

class HandsetBrandM(HandsetBrand):
    '''
    ����~�PM
    '''
    def Run(self):
        self.soft.Run()


        
if __name__ == '__main__':
    ab = HandsetBrandN()
    ab.SetHandsetSoft( HandsetGame() )
    ab.Run()
    ab.SetHandsetSoft( HandsetAddressList() )
    ab.Run()
    
    ab = HandsetBrandM()
    ab.SetHandsetSoft( HandsetGame() )
    ab.Run()
    ab.SetHandsetSoft( HandsetAddressList() )
    ab.Run()
