'''
Mediator
'''

class Flyweight:
	def Operation(self, extrinsicstate):
		pass
class ConcreteFlyweight(Flyweight):
	def Operation(self, extrinsicstate):
		print '具體 Flyweight: ' + extrinsicstate

class UnsharedConcreteFlyweight(Flyweight):
	def Operation(self, extrinsicstate):
		print '不共用的具體 Flyweight: ' + extrinsicstate

class FlyweightFactory:
	def __init__(self):
		self.flyweights = {
			'x': ConcreteFlyweight(),
			'y': ConcreteFlyweight(),
			'z': ConcreteFlyweight(),
		}

	def GetFlyWeight(self, key):
		return flyweights[key]

if __name__ == '__main__':
	extrinsicstate = 22
	f = FlyweightFactory()

	fx = f.GetFlyWeight('x')
	extrinsicstate -= 1
	fx.Operation(extrinsicstate)

	fy = f.GetFlyWeight('y')
	extrinsicstate -= 1
	fy.Operation(extrinsicstate)

	fz = f.GetFlyWeight('z')
	extrinsicstate -= 1
	fz.Operation(extrinsicstate)

	uf = UnsharedConcreteFlyweight()
	extrinsicstate -= 1
	uf.Operation(extrinsicstate)