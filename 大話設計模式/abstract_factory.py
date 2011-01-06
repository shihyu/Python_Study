# -*- coding: cp950 -*-
'''
Abstrract Factory Pattern
'''

class IFactory:
    def CreateUser(self):
        pass
    def CreateDepartment(self):
        pass
    
class SqlserverFactory(IFactory):
    def CreateUser(self):
        return SqlserverUser()
    
    def CreateDepartment(self):
        return SqlserverDepartment()
    
class AccessFactory(IFactory):    
    def CreateUser(self):
        return AccessUser()
    def CreateDepartment(self):
        return AccessDepartment()

class IUser:
    def Insert(self, item):
        pass
    def GetUser(self, idx):
        pass

class SqlserverUser(IUser):
    def Insert(self, item):
        print 'SqlServer User ��s�W���� %s' % item.name
    
    def GetUser(self, idx):
        print 'SqlServer User ��^�Ǥ@������'
    
class AccessUser(IUser):
    def Insert(self, item):
        print 'Access User ��s�W���� %s' % item.name
    
    def GetUser(self, idx):
        print 'Access User ��^�Ǥ@������'
        
class IDepartment:
    def Insert(self, item):
        pass
    
    def GetDepartment(self, idx):
        pass
class SqlserverDepartment(IDepartment):
    def Insert(self, item):
        print 'SqlServer Department ��s�W���� %s' % item.name
    
    def GetDepartment(self, idx):
        print 'SqlServer Department ��^�Ǥ@������'
    
class AccessDepartment(IDepartment):
    def Insert(self, item):
        print 'Access Department ��s�W���� %s' % item.name
    
    def GetDepartment(self, idx):
        print 'Access Department ��^�Ǥ@������'

class User:
    def __init__(self):
        self.name = '�j��'

class Department:
    def __init__(self):
        self.name = '�ȪA'
        
if __name__ == '__main__':
    user = User()
    dept = Department()
    
    factory = SqlserverFactory()
    iu = factory.CreateUser()
    iu.Insert(user)
    iu.GetUser(1)

    idept = factory.CreateDepartment()
    idept.Insert(dept)
    idept.GetDepartment(1)
    
    factory = AccessFactory()
    iu = factory.CreateUser()
    iu.Insert(user)
    iu.GetUser(1)

    idept = factory.CreateDepartment()
    idept.Insert(dept)
    idept.GetDepartment(1)
