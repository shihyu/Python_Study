# -*- coding: cp950 -*-
'''
Composite Patter
'''
class Aggregate:
    def CreateIterator(self):
        '''
        回傳實做 Iterator 介面的物件
        '''
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []

    def Add(self, item):
        self.items.append(item)
        
    def CreateIterator(self):
        return ConcreteIterator(self)

    def Count(self):
        return len(self.items)
    
    def GetItem(self, index):
        return self.items[index]
    
class Iterator:
    def First(self):
        pass
    def Next(self):
        pass
    def IsDone(self):
        pass
    def CurrentItem(self):
        pass



class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = 0
    def First(self):
        return self.aggregate.GetItem(0)
    
    def Next(self):
        self.current += 1
        if self.IsDone():
            return None
        return self.CurrentItem()
    
    def IsDone(self):        
        return self.current >= self.aggregate.Count()
    
    def CurrentItem(self):
        return self.aggregate.GetItem(self.current)

    

if __name__ == '__main__':
    a = ConcreteAggregate()
    a.Add( '大鳥' )
    a.Add( '小菜' )
    a.Add( '行李' )
    a.Add( '老外' )
    a.Add( '巴士內部員工' )
    a.Add( '小偷' )

    it = a.CreateIterator()
    item = it.First()
    while(not it.IsDone()):
        print '%s 請買車票!' % it.CurrentItem()
        it.Next()
        
