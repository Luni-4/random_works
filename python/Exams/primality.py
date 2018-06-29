from math import log2
from random import randint
import sys, resource

def trial_division(n):
	print("Trial-Division's Primality Test", end="\t")
	return len([x for x in range(2,int(n**0.5)+1) if n % x == 0]) == 0
	
def seq(p):
	si = 4
	i = 1
	while i < p - 1:
		si = (si**2) - 2
		i += 1
	return si

def lucaslehmer(n):
	print ("Lucas-Lehmer's Primality Test", end='\t')
	p = int(log2(n+1))
	sp2 = seq(p)
	return sp2 % n == 0
		

def littlefermat(n):
	print ("Little Fermat's Primality Test", end='\t')	
	na = [randint(1,20) for x in range(int(n**0.5))]
	prime = 0
	for a in na:		
		if pow(a, n-1, n) != 1:
			prime += 1
	return prime == 0

def is_prime(n):
	if n < 10001:
		return trial_division(n)
	elif 10001 <= n <= 524280:
		return lucaslehmer(n)
	else:
		return littlefermat(n)	
