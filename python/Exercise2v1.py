from functools import reduce
import math
import sys

mcd = lambda x,y: x if (y == 0) else mcd(y, x % y)		
	
mcm = lambda x,y: x // mcd(x, y) * y

c = True

def fib():
	a,b = 0,1
	global c
	while c:
		yield a
		a,b = b, a+b
		
def r(elem):
	global c
	c = False
	return elem

def gen():
	return list(r(elem) for elem in fib() if len(str(elem)) > 999)
		
		 
 
					
if __name__ == "__main__":
	print(reduce(lambda x,y: x+y, [elem for elem in range(1000) if (elem % 3 == 0) or (elem % 5 == 0)]))
	print(reduce(mcm, range(2,8)))
	print(reduce(lambda x,y: x+y,(int(elem) for elem in str(2**1000))))
	print(gen())	
