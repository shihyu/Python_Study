'''
Design Pattern: Memento
'''
  

class Caretaker:
    def __init__(self):
        self.Memento = None

class Memento:
    def __init__(self, state):
        self.State = state
        
class Originator:
    def __init__(self):
        self.State = None
        
    def SetMemento(self, m):
        self.State = m.State
        
    def CreateMemento(self):
        return Memento(self.State)

    def Show(self):
        print self.State


if __name__ == '__main__':
    org = Originator()
    org.State = 'on'
    org.Show()

    c = Caretaker()
    c.Memento = org.CreateMemento()

    org.State = 'off'
    org.Show()

    org.SetMemento(c.Memento)
    org.Show()
    
