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
    標準 Design Pattern 測試程式
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
    手機軟體抽象類別
    '''
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    '''
    手機遊戲
    '''
    def Run(self):
        print '執行手機遊戲'

class HandsetAddressList(HandsetSoft):
    '''
    手機通訊錄
    '''    
    def Run(self):
        print '執行手機通訊錄'        

class HandsetBrand:
    '''
    手機品牌
    '''
    def SetHandsetSoft(self, soft):
        self.soft = soft

    def Run(self):
        pass

class HandsetBrandN(HandsetBrand):
    '''
    手機品牌N
    '''
    def Run(self):
        self.soft.Run()

class HandsetBrandM(HandsetBrand):
    '''
    手機品牌M
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
