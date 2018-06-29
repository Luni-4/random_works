from math import sqrt
from traceback import print_stack
		
		
class memoization(object):
	def __init__(self, func):
		self._func = func
		print("secondo ", self._func)
		self._cacheName = '_cache__' + func.__name__		
		
	def __get__(self, instance, owner):
		self._instance = instance
		return self
        
	def __call__(self, *args, **kwargs):
		print("call memo")		
		cache = self._instance.__dict__.setdefault(self._cacheName, {})
		if args in cache:
			return cache[args]
		else:
			object = cache[args] = self._func(self._instance, *args, **kwargs)
		return object
		

def logging(f):
	def save(*args, **kwargs):	
		with open("files.txt", "a", encoding = "utf-8") as out:
			out.write(f.__name__ + str(args) + "\n")
		return f(*args, **kwargs)
	return save
	
'''class logging(object):
	def __init__(self, func):
		print("Primo")
		self._f = func
		
	def __get__(self, instance, owner):
		self._instance = instance
		print("ciao")
		return self._instance
	
	def __call__(self, *args):
		print("call logging")	
		with open("files.txt", "a", encoding = "utf-8") as out:
			out.write(self._f.__name__ + str(args) + "\n")'''

class stack_trace(object):
	def __init__(self, func):
		self._f = func
		
	def __get__(self, instance, owner):
		self._instance = instance
		return self
	
	def __call__(self, *args, **kwargs):
		print_stack()	
		return self._f(self._instance, *args, **kwargs)
		
class myMath(object):

	@memoization
	#@stack_trace
	#@logging	
	def fact(self, n):
		print("ciao")
		return (n<=1 and 1) or n*self.fact(n-1)
		
	@memoization
	def fib(self, n):
		m = lambda n: ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
		return list((int(m(p)) for p in range(n+1)))
	
	@memoization
	#@stack_trace	
	def taylor(self, f, x, n):
		return sum(list((f(x,p) for p in range(n+1))))
			
		

if __name__ == "__main__":
	a = myMath()
	print(a.fib(1))
	print(a.fact(5))
	print(a.fact(5))
	print(a.fact(5))
	print(a.taylor(lambda x,y: x**y/a.fact(y), 1, 2))
