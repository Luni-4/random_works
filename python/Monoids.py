from itertools import permutations, product, combinations as comb

class Monoid(object):
	def __init__(self, insieme, operation, identity):
		self._set = list(insieme)
		self._op = operation
		self._id = identity
	
	def associativity(self):
		check = lambda x, y, z: self._op(self._op(x,y), z) != self._op(x,self._op(y,z))		
		return not any(check(x[0], x[1], x[2]) for x in product(self._set, repeat = 3)) 		
		
	def identity(self):
		return not any(self._op(x, self._id(x)) != x and self._op(self._id(x), x) != x for x in self._set)			
	
	def closure(self, inf = 0):
		if inf == 0:
			return not any(self._op(x[0],x[1]) not in self._set for x in comb(self._set, 2))
						
		return not any(not inf(self._op(x[0],x[1])) for x in comb(self._set, 2))
		
		
class Group(Monoid):

	def invertibility(self):	
			
		if len(self._set) == 1:
			self.x = self._set[0]
			return self._op(self.x,self.x) == self._id(self.x) and self._op(self.x, self.x) == self._id(self.x)
			
		check = lambda x : self._op(x[0],x[1]) == self._id(x) and self._op(x[1],x[0]) == self._id(x) 
		return len([x for x in product(self._set, repeat = 2) if check(x)]) == len(self._set)		
			

class Ring(Group):
	def __init__(self, *args):
		super(Ring,self).__init__(args[0], args[1], args[3])		
		self._op2 = args[2]	
				
	def addition(self, inf = 0):
		if inf == 0:
			return self.associativity() and self.closure() and self.identity() and self.invertibility()
		return self.associativity() and self.closure(inf) and self.identity() and self.invertibility() 
		
	def multiplication(self, inf = 0):
		self._b = Monoid(self._set, self._op2, self._id)
		if inf == 0:
			return  self._b.associativity() and self._b.closure() and self._b.identity()  
		return self._b.associativity() and self._b.identity() and self._b.closure(inf)
	
	def ring(self, inf = 0):
		if inf == 0: 
			return self.addition() and self.multiplication()
		return self.addition(inf) and self.multiplication(inf)
		


# Inverte gli elementi in una permutazione
def swap(x, i, m):
	l = list(x)
	l[i], l[m] = l[m], l[i]
	return l	
	
			
if __name__ == "__main__":
	
	print("Booleani")
	a = Monoid({True, False}, lambda x,y: x or y, lambda x: False)
	print(a.associativity())
	print(a.identity())
	print(a.closure(), end="\n\n")
	
	print("n mod")
	b = Monoid({0, 1, 2, 3, 4, 5}, lambda x,y: (x + y) % 6, lambda x: 0)
	print(b.associativity())
	print(b.identity())
	print(b.closure(), end="\n\n")
	
	print("Permutazioni")
	c = Group(permutations("RGB"), lambda x,y: swap(swap(x,1,2),0,1), lambda x: swap(swap(x,0,1),0,1)) 
	print(c.associativity())
	print(c.identity())
	print(c.closure())
	print(c.invertibility(), end="\n\n")
	
	print("Razionali")
	d = Group({0.3, 0.5}, lambda x,y: x*y, lambda x: 1.0) 
	print(d.associativity())
	print(d.identity())
	print(d.closure(lambda x: isinstance(x,float)))
	print(d.invertibility(), end="\n\n")
	
	print("Zero ring")
	e = Ring({0}, lambda x,y: x+y, lambda x,y: x*y,  lambda x: 0) 
	print(e.addition())
	print(e.multiplication())
	print(e.ring(), end="\n\n")
	
	print("Relativi ring")
	f = Ring({-3, -2, -1, 0, 1, 2, 3}, lambda x,y: (x+y), lambda x,y: (x*y),  lambda x: 0) 
	print(f.addition(lambda x: isinstance(x,int)))
	print(f.multiplication(lambda x: isinstance(x,int)))
	print(f.ring(lambda x: isinstance(x,int)), end="\n\n")	
	
	print("Relativi Z4 ring")
	g = Ring({0, 1, 2, 3}, lambda x,y: (x+y) % 4, lambda x,y: (x*y) % 4,  lambda x: 0) 
	print(g.addition())
	print(g.multiplication())
	print(g.ring())	
