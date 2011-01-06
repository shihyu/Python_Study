'''
Chain of Responsibility
'''

class Handler:
	def __init__(self, name):
		self.successor = None
		self.name = name

	def SetSuccessor(self, successor):
		'''
		@param successor 繼任者
		'''
		self.successor = successor

	def HandleRequest(self, request):
		pass

class ConcreteHandler1(Handler):
	def HandleRequest(self, request):
		if request >=0 and request < 10:
			print '%s 處理請求 %s' % (self.name, request)

		elif not self.successor is None:
			self.successor.HandleRequest(request)

class ConcreteHandler2(Handler):
	def HandleRequest(self, request):
		if request >=10 and request < 20:
			print '%s 處理請求 %s' % (self.name, request)

		elif not self.successor is None:
			self.successor.HandleRequest(request)

class ConcreteHandler3(Handler):
	def HandleRequest(self, request):
		if request >=20 and request < 30:
			print '%s 處理請求 %s' % (self.name, request)

		elif not self.successor is None:
			self.successor.HandleRequest(request)

if __name__ == '__main__':
	h1 = ConcreteHandler1('H1')
	h2 = ConcreteHandler2('H2')
	h3 = ConcreteHandler3('H3')

	h1.SetSuccessor(h2)
	h2.SetSuccessor(h3)

	requests = [2,5,14,22,18,3,27,20]
	for request in requests:
		h1.HandleRequest(request)
