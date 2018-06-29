from math import factorial

def pi_series():
	i, a = 1, 4.0
	while True:
		yield a
		a += ((-1)**i)*(4/(2*(i)+1))
		i += 1

def e_series():
	i, a = 1, 1.0
	while True:
		yield a
		a += (1/ factorial(i))
		i += 1 
		
def euler_accelerator(g):
	np, n = next(g), next(g)
	while True:		
		nn = next(g)
		yield nn - (((nn - n)**2) / (np - 2 * n + nn))
		np, n = n, nn	
