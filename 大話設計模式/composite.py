# -*- coding: cp950 -*-
'''
Composite Patter
'''

class Component:
    def __init__(self, name):
        self.name = name

    def Add(self, c):
        pass

    def Remove(self, c):
        pass

    def Display(self, depth):
        pass
    
class Leaf(Component):
    def Add(self, c):
        print "cannot add to a leaf"

    def Remove(self, c):
        print "cannot remove from a leaf"

    def Display(self, depth):
        print '-' * depth, self.name
    
class Composite(Component):
    def __init__(self, name):
        Component.__init__(self,name)
        self.children = []
        
    def Add(self, c):
        self.children.append(c)

    def Remove(self, c):
        self.children.remove(c)

    def Display(self, depth):
        print '-' * depth, self.name        
        for item in self.children:
            item.Display(depth+2)

if __name__ == '__main__':
    root = Composite('root')
    root.Add(Leaf('Leaf A'))
    root.Add(Leaf('Leaf B'))

    comp = Composite('Composite X')
    comp.Add(Leaf('Leaf XA'))
    comp.Add(Leaf('Leaf XB'))
    root.Add(comp)

    comp2 = Composite('Composite Y')
    comp2.Add(Leaf('Leaf YA'))
    comp2.Add(Leaf('Leaf YB'))
    comp.Add(comp2)

    root.Add(Leaf('Leaf C'))

    root.Display(1)
