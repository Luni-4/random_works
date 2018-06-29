import math

def def_polygon(name, n, side):
	class polygon(object):	
		def __init__(self):			
			if side <= 0:
				raise ValueError("{0} is an inadmissible size for a {1}’s side".format(side, name))				
			
		def calculate_area(self):		
			return .25 * n * side**2 * (math.tan(math.pi/n)**-1)
			
		def calculate_perimeter(self):			
			return n*side
		
		def __lt__(self, other):		
			return self.calculate_area() < other.calculate_area()		
		
		def __str__(self):
			return "I’m a {0} and my area is {1}".format(name, self.calculate_area())
	return polygon
	

class Rectangle(object):
	def __init__(self, base, height):
		self._base = base
		self._height = height
		
	def calculate_area(self):
		return self._base * self._height
		
	def calculate_perimeter(self):
		return (self._base + self._height) * 2
		
	def __lt__(self,other):
		return self.calculate_area() < other.calculate_area()
	
	def __str__(self):
		return "I’m a Rectangle!\nMy area is {0}\n".format(self.calculate_area())	
		

class Circle(object):
	def __init__(self, ray):
		if ray <= 0:
			raise ValueError("{0} is an inadmissible size for a circle’s ray".format(ray))
		self._ray=ray
		
	def calculate_area(self):
		return self._ray**2*math.pi
		
	def calculate_perimeter(self):
		return 2*self._ray*math.pi
		
	def __lt__(self,other):
		return self.calculate_area() < other.calculate_area()
	
	def __str__(self):
		return "I’m a Circle!\nMy ray is: {0}\nMy area is {1}\n".format(self._ray, self.calculate_area())		
		 
 
					
if __name__ == "__main__":
	l = [Rectangle(2,3), Rectangle(1,1), Circle(4)]
	print(l)
	
	print("\nStampa del contenuto della lista")
	
	for i in l: print(i)
	
	print()	

	p = sorted(l, key = lambda k: k.calculate_perimeter())
	
	m = sorted(l) 
	
	print("\nStampa degli elementi ordinati")
	for i in m: print(i)
	
	print("\nStampa degli elementi ordinati per perimetro")
	for i in p: print(i.calculate_perimeter())
	
	print("\nItera sugli elementi a seconda dell'area")
	for i in l: print(i)	
