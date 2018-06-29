from math import sin as sin2
from time import clock

class timer:
	def __init__(self, func):
		self._func = func
		self._tempototale = 0
	def __call__(self, *args, **kargs):
		start = clock()
		result = self._func(*args, **kargs)
		elapsed = clock() - start
		print("{0}: {1}".format(self._func.__name__, elapsed))
		self._tempototale += elapsed
		return result

@timer
def matecheck(x):
	return sin2(x)
	
l = [0,1]

def fact(n):
	global l
	while l[0] < n+1:
		yield l[1]
		l[0], l[1]  = l[0]+1, l[1] * (l[0]+1)

@timer		 
def sin(x, n):		
	return sum([((-1)**elem)*(x**((2*elem)+1))/(list(p for p in fact((2*elem)+1))[-1]) for elem in range(n)])
	
if __name__ == "__main__":
	print(matecheck(3))
	print()
	print(sin(3,13))
