# Importing
import re 
import time
from math import sin
import sys
import dis
import inspect
import copy




# Sorting and class

''' Inutile crare interfaccie comuni (esempio specifico, shape) perché python ha il duck typing

class Shape(object):
	def area(self): pass
	def perimeter(self): pass 
'''

class Rectangle(object):
	
	''' Classe che definisce il rettangolo '''
	
	#prova = 0 Variabile di classe
	
	def __init__(self, base, altezza):
		self._base = base
		self._altezza = altezza
	def area(self):
		return self._base * self._altezza
	def perimeter(self):
		return (self._base + self._altezza) * 2
	def __str__(self):
		return "Sono un Rettangolo!"
		
class Square(Rectangle):
	def __init__(self, lato):
		self._base = lato
		self._altezza = lato	
	def __str__(self):
		return "Sono un Quadrato"

#------------------------------------------------------------------------------------------	

# Closures
		

def sost(m):
	if re.search('[^mno]a$',m):
		return re.sub('$', 's', m)
	return m

def potenza(n):
	def power(x):
		return x**n
	return power
	
def product(f,x):
	def fi(*args):
		return f(x,*args)
	return fi
	
def f2(x,y):
	return x*y

#------------------------------------------------------------------------------------------		

# Decoratori
	
class timer:
	def __init__(self, func):
		self._func = func
		self._tempototale = 0
	def __call__(self, *args, **kargs):
		start = time.clock()
		result = self._func(*args, **kargs)
		elapsed = time.clock() - start
		self._tempototale += elapsed
		return result
		
def timerfunc(F):	
	def wrapper(*args, **kargs):
		start = time.clock()
		result = F(*args, **kargs)
		elapsed = time.clock() - start	
		wrapper.tempototale += elapsed	
		return result
	wrapper.tempototale = 0
	return wrapper

@timerfunc
def prova(n):
	return [x for x in range(n)]
	

# Metaclassi

class prova2(type):
	def __new__(meta, classname, supers, classdict):
		return type.__new__(meta, classname, supers, classdict)
	def __init__(Class, classname, supers, classdict):
		print("ciok")
		

class ciao(metaclass=prova2):
	def __init__(self, num):
		self._num = num
	def ciaociao(): pass

# Exception

class Diff(Exception):
	def __init__(self, args, kwargs):
		self.arg = args
		self.kwarg = kwargs

				

if __name__ == "__main__":
	# Import
	print(sin(5))
	
	#Dictionary
	key = {"z", "a", "m"}
	d = dict.fromkeys(sorted(key))
	print(d.items())
	

	# Regular Expression and Closures
	metti = "casa"
	print(sost(metti))
	# Trovare numeri decimali, interi, operatori logici e operatori numerici all'interno di una stringa
	string = "3+5*2"
	str2 = re.findall(r"[-+]?\d*\.\d+|\d+|[or]+|[and]+|[not]+|[TF+-/*]+", string)	
	
	# Creazione di una Closures (funzione che restituisce un'altra funzione)
	esec = potenza(5)
	
	# La Closures è come un puntatore a funzione
	print(esec(2))
	
	# Comprenshion e Closures
	j = [potenza(k) for k in range(10)]
	print([m(2) for m in j])	
	
	# Campo closure associato ad una funzione
	print(esec.__closure__)
	
	
	# Currying
	m = product(f2,2)
	print("Risultato: {0}".format(m(3)))
	
	
	
#------------------------------------------------------------------------------------------	

	# Instanze di classi (oggetti)
	a = Rectangle(3,5)
	b = Square(2)
	
	# Sorting di oggetti in lista
	lista = [Rectangle(3,5), Square(4), Rectangle(1,1)]
	
	# Stampa degli oggetti usando le comprenshion (functional programming, yay) e le built-in function di python
	print([x.area() for x in sorted(lista, key = lambda x: x.area(), reverse = True)])	
	
	# Stampa il valore restituito da __str__ (se __str__ non presente, restituisce oggetto)
	print(a)
	
	# Modifica di __str__ dal dizionario associato alla classe
	Rectangle.__str__ = "ciao ciao"
	
	# Modifica usando il dizionario, di un attributo di un'istanza
	
	a.__dict__['_base'] = 8
	print(a._base)
	
	# Le funzioni non sono accessibili dal dizionario dalla classe, devono prima essere bindate con l'istanza 
	
	# Stampa del dizionario associato alla classe
	print(Rectangle.__dict__)
	
#------------------------------------------------------------------------------------------
	
	# Decoratori
	print(prova(50))
	print(prova(50))
	print(prova(50))
	print(prova.tempototale)
	
	# Metaclassi
	
	k = ciao(5)
	
	# Tipo di oggetto
	print(type(Rectangle))
	
	# Istanza di oggetto
	print(isinstance(a,Rectangle))
#------------------------------------------------------------------------------------------	
	# Exception:
	f = sys._getframe()
	if f.f_back:
		raise Diff("ciao","ciao")	
	try:
		print("Fai il try")
	except Diff as e:
		print(e.arg)
		print(e.kwarg)

#------------------------------------------------------------------------------------------	
	# Any
	print(any(x < 0 for x in range(-1,10)))
	
	# All
	print(all(x > 0 for x in range(1,10)))

#------------------------------------------------------------------------------------------	
	# Stack
	l = [1, 2, 3]
	l1 = list()
	# Shallow copy
	l1 = l[:]
	l[0] = 2
	print(l1)
	#print(inspect.currentframe().f_globals)

#------------------------------------------------------------------------------------------	
	#Set
	y = set(["c","c","a"])
	d = set(["m","n","o"])
	print(y.add("ip"))
	y.update({"b","d","c"})
	print(y)
	y.discard("h")
	print(y.union(d))

#------------------------------------------------------------------------------------------	
	#Comprhension loop
	d = [[1, 2], [4, 5], [7, 8]]
	m = [1, 2, 4, 5, 7, 8]
	print([y if y % 2 == 0 else y + 2 for x in d for y in x])
	print([y for y in m if y % 2 == 0])
	
	
	
	
	




