from math import log2
from random import randint

def prime_sieve(n):
	l = []
	i = 2
	while i < n+1:
		prime = True
		for p in l: 
			if i % p == 0: 
				prime = False
				break
		if prime == True: 
			l.append(i)
			yield l[-1] 
		i += 1	


def trivial_division(n):
	prime_factors = []
	if n < 2:
		return []
	for p in prime_sieve(int(n**0.5)):
		if p*p > n: break
		while n % p == 0:
			prime_factors.append(p)
			n //= p
	if n > 1:
		prime_factors.append(n)
	return len(prime_factors) == 1
	
def seq(p):
	si = 4
	yield si
	i = 1
	while i < p -2:
		si = (si**2) - 2
		yield si

def lucaslehmer(n):
	p = log2(n+1)
	sp2 = int(x for x in seq(p))
	return sp2 % n == 0

def littlefermat(n):
	na = [randint(1,n-1) for x in range(int(n**0.5))]
	prime = 0
	for a in na:
		#if (a**(n-1) - 1) % n == 0:
			prime += 1
	return prime >= len(na)

def is_prime(n):
	if n < 10001:
		return trivial_division(n)
	elif 10001 <= n <= 524280:
		return lucaslehmer(n)
	else:
		return littlefermat(n)
	
def test_primes(vl):
  if len(vl)>0: 
     print("{:14d} :- {}".format(vl[0], is_prime(vl[0])))
     test_primes(vl[1:])

if __name__ == '__main__':
  test_primes([25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])	
		
	
