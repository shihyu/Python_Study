# -*- coding: cp950 -*-
'''
Command Patterb 範例：燒烤店
'''

class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def ExecuteCommand(self):
        pas

class BakeMuttonCommand(Command):
    def ExecuteCommand(self):
        self.receiver.BakeMutton()
    def __str__(self):
        return '烤羊肉串'

class BakeChickenWingCommand(Command):
    def ExecuteCommand(self):
        self.receiver.BakeChickenWing()
    def __str__(self):
        return '烤雞翅'

class Barbecuer:
    def BakeChickenWing(self):
        print '烤雞翅'
    
    def BakeMutton(self):
        print '烤羊肉串'
    
class Waiter:
    def __init__(self):
        self.orders = [] # 訂單

    def SetOrder(self, command):
        if str(command) == '烤雞翅':
            print '服務生：雞翅沒有了，請點別的燒烤'
        else:    
            self.orders.append( command )
            print '增加訂單: %s' % str(command)
            
    def CancelOrder(self, command):
        for v in self.orders:
            if v == command:
                self.orders.remove(command)

        print '取消訂單： %s' % str(command)
        
    def Notify(self):
        for cmd in self.orders:
            cmd.ExecuteCommand()
    
if __name__ == '__main__':
    boy = Barbecuer()
    bakeMuttonCommand1 = BakeMuttonCommand(boy)
    bakeMuttonCommand2 = BakeMuttonCommand(boy)
    bakeChickenWingCommand = BakeChickenWingCommand(boy)
    girl = Waiter()
    girl.SetOrder(bakeMuttonCommand1)
    girl.SetOrder(bakeMuttonCommand2)
    girl.SetOrder(bakeChickenWingCommand)    
    girl.Notify()
