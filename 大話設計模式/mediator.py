'''
Mediator
'''

class Mediator:
	def Send(self, message, colleague):
		pass

class Colleague:
	def __init__(self):
		self.mediator = None
	def Colleague(self, mediator):
		self.mediator = mediator

class ConcreteMediator(Mediator):
	def __init__(self):
		self.colleague1 = None
		self.colleague2 = None

	def Send(self, message, colleague):
		if colleague == self.colleague1:
			self.colleague2.Notify(message)
		else:
			self.colleague1.Notify(message)

class ConcreteColleague1(Colleague):
	def Send(self, message):
		self.mediator.Send(message, self)
	def Notify(self, message):
		print '同事1得到資訊:' + message

class ConcreteColleague2(Colleague):
	def Send(self, message):
		self.mediator.Send(message, self)
	def Notify(self, message):
		print '同事2得到資訊:' + message

if __name__ == '__main__':
	m = ConcreteMediator()
	c1 = ConcreteColleague1(m)
	c2 = ConcreteColleague2(m)

	m.colleague1 = c1
	m.colleague2 = c2

	c1.Send('吃過飯了嗎')
	c2.Send('沒有呢，你打算請客嗎？')