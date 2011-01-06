'''
Design Pattern: Adapter
'''   
class Target:
    def Request(self):
        print 'request'
        
class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()
        
    def Request(self):
        self.adaptee.SpecificRequest()
        
class Adaptee:        
    def SpecificRequest(self):
        print 'special request'


if __name__ == '__main__':
    target = Adapter()
    target.Request()
    
