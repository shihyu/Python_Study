# -*- coding: cp950 -*-
'''
Command Patterb �d�ҡG�N�N��
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
        return '�N�Ϧצ�'

class BakeChickenWingCommand(Command):
    def ExecuteCommand(self):
        self.receiver.BakeChickenWing()
    def __str__(self):
        return '�N����'

class Barbecuer:
    def BakeChickenWing(self):
        print '�N����'
    
    def BakeMutton(self):
        print '�N�Ϧצ�'
    
class Waiter:
    def __init__(self):
        self.orders = [] # �q��

    def SetOrder(self, command):
        if str(command) == '�N����':
            print '�A�ȥ͡G���ͨS���F�A���I�O���N�N'
        else:    
            self.orders.append( command )
            print '�W�[�q��: %s' % str(command)
            
    def CancelOrder(self, command):
        for v in self.orders:
            if v == command:
                self.orders.remove(command)

        print '�����q��G %s' % str(command)
        
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
