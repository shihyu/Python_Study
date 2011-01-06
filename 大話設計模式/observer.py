# -*- coding: cp950 -*-
'''
Observer Pattern
'''

class Subject:
    def Attach(self, observer):
        pass
    def Detach(self, observer):
        pass
    def Notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self.SubjectState = None
        self.observers = []
        
    def Attach(self, observer):
        self.observers.append(observer)
        
    def Detach(self, observer):
        self.observers.remove(observer)
        
    def Notify(self):
        map(lambda v: v.Update(), self.observers)
    
class Observer:
    def Update(self):
        pass

class ConcreteObserver(Observer):
    def __init__(self, subject, name):
        self.observerState = None
        self.subject = subject
        self.name = name
        
    def Update(self):
        self.observerState = self.subject.SubjectState
        print '觀察者%s的新狀態是%s' %(self.name, self.observerState)
        
if __name__ == '__main__':
    sub = ConcreteSubject()
    sub.Attach( ConcreteObserver(sub, "X") )
    sub.Attach( ConcreteObserver(sub, "Y") )
    sub.Attach( ConcreteObserver(sub, "Z") )

    sub.SubjectState = "Hello"
    sub.Notify()
