from time import clock
import inspect

class cg(type):
	def __new__(meta, classname, supers, classdict):
		print(classdict)
		return type.__new__(meta, classname, supers, classdict)
		
def sup(f):
	def val(f):
		return f
	return val
	
class deco(object):
		def __init__(self,func):
			self.f = func
		
		def __get__(self, instance, owner):
			print(instance)
			print(owner)
			self.instance = instance
			return self
		
		def __call__(self, *args, **kwargs):
			return self.f(self.instance,*args, **kwargs)


def Timing(param):
	def func(f):
		print("Violence")
		def var(*args, **kwargs):
			if param:
				start = clock()
				tmp = f(*args, **kwargs)
				duration = clock() - start
				print("{}".format(duration))
				return tmp
			else:
				return f(*args, **kwargs)
		print(var)
		return var
	print(func)
	return func

class Giocattolo(object):
	def __new__(cls):
		print("pip")
		return object.__new__(cls)
	
	def __init__(self):
		print("ciao")
		
		c = 5
		
		def inner_scope():
			b = 2
			return "{:d} Sono troppo power".format(c)
		
		print(inner_scope())
	
	@Timing(True)
	def m2(self, i):
		print("Ciao Ciao")
	
	@sup(5)
	def m3(self, n):
		return n
		
class Areoplano(Giocattolo):
	def bike(self):
		return "ik ik"
	
	@classmethod
	def c(cls):
		return "class method"
	
	@staticmethod
	def b():
		return "Static method"
	
	'''def __getattr__(self,name):
		print("pip")
		return object.__getattr__(self,name)'''
	
	def __getattribute__(self,name):
		print("pip2")
		return Giocattolo.__getattribute__(self,name)
	
	@deco
	def take(self, m):
		return 5
	
def recursion(n, somma = 0):
	n = str(n)
	if n == "":
		return somma
	somma += int(n[0])
	return recursion(n[1:], somma)


if __name__ == "__main__":
	h = Areoplano()
	g = Giocattolo()
	g.m2(5)
	print(h.bike())
	print(g.m3(5))
	Giocattolo = cg("Giocattolo", (), dict(Giocattolo.__dict__))
	#print(h.take(1))
