from itertools import combinations_with_replacement as c

class NotGoldbach(ValueError): pass

def trial_division(n):
	return len([elem for elem in range(2, int(n**0.5) + 1) if n % elem == 0]) == 0

def goldbach(n):
	if n < 3:
		raise NotGoldbach("Numeri inferiori a 2 non sono numeri di Goldbach")
	
	if n % 2 != 0:
		raise NotGoldbach("{} non è un numero pari".format(n))
	
	prime = [x for x in range(2, n) if trial_division(x)]
	
	return [str(n) + " = " + str(x[0]) + " + " + str(x[1]) for x in c(prime, 2) if x[0] + x[1] == n]

def goldbach_list(n,m):
	if n < 3 or m < 3:
		raise NotGoldbach("Intervallo non corretto")
		
	return {x : goldbach(x) for x in range(n, m + 1) if x % 2 == 0}
	

if __name__ == "__main__":
	print(goldbach(20))
	print(goldbach_list(4,20))
