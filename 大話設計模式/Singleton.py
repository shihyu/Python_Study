# -*- coding: cp950 -*-
'''

Singleton

'''

class Singleton:
    __instance = None
    
    def __init__(self):
        '''
        ���䴩 private ctor �ҥH�ݭn�B�~�ˬd
        '''
        if Singleton.__instance:
            raise Singleton.__instance
        
        self.Value = 1
        Singleton.__instance = self
        
    @staticmethod
    def GetInstance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
            
        return Singleton.__instance 
        
    
if __name__ == '__main__':
    obj = Singleton.GetInstance()
    print obj.Value
    obj.Value = 100
    print obj.Value
    obj2 = Singleton.GetInstance()
    print obj2.Value


