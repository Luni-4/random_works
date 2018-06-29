class NotValidMatrix(Exception): pass

class Matrix(object):
	def __init__(self, mat):
		checkvoid = lambda mat: any(len(x) == 0 or len(x) != len(mat[0]) for x in mat)
		checkint = lambda mat: all(isinstance(elem, int) for x in mat for elem in x)
				
		if not isinstance(mat, list) or len(mat) == 0 or checkvoid(mat) or not checkint(mat):
			raise NotValidMatrix("Matrix is not valid")
		
		self.mat = mat
		
	def __repr__(self):
		return str(self.mat)
	
	def __setattr__(self, name, value):
		if name == "mat":
			
			checkvoid = lambda mat: any(len(x) == 0 or len(x) != len(mat[0]) for x in mat)
			checkint = lambda mat: all(isinstance(elem, int) for x in mat for elem in x)
				
			if not isinstance(value, list) or len(value) == 0 or checkvoid(value) or not checkint(value):
				raise NotValidMatrix("Matrix is not valid")			
			
		super(Matrix, self).__setattr__(name, value)	
		
	
	def getrowsize(self):
		return len(self.mat)
	
	def getcolumnsize(self):
		return len(self.mat[0])
	
	def getdimension(self):
		return self.getrowsize() * self.getcolumnsize()
	
	def __eq__(self,y):
		if self.getdimension() != y.getdimension():
			raise NotValidMatrix("Matrixes have different dimensions, so they're not equal to each other")
		
		return len([x for x in range(self.getrowsize()) if self.mat[x] != y.mat[x]]) == 0
	
	def copy(self,y):
		if self.getdimension() != y.getdimension():
			raise NotValidMatrix("Matrixes have different dimensions")
		
		self.mat = [x for x in y.mat]
	
	def __add__(self, y):
		if self.getdimension() != y.getdimension():
			raise NotValidMatrix("Matrixes have different dimensions, so they can't be added")

		return Matrix([[self.mat[x][z] + y.mat[x][z] for z in range(self.getcolumnsize())] for x in range(self.getrowsize())])
	
	def multiply(self, a):
		if not isinstance(a, int):
			raise ValueError("The value must be an integer")
		
		return Matrix([[a * y for y in x] for x in self.mat])
	
	def transpose(self):	
		return Matrix([[self.mat[x][y] for x in range(self.getrowsize())] for y in range(self.getcolumnsize())])
	
	def __mul__(self, y):
		if self.getcolumnsize() != y.getrowsize():
			raise NotValidMatrix("Matrixes can't be multiplied, the number of columns of the first one \
								  must match the number of rows of the second one")
			
		return Matrix([[sum([m * n for m, n in zip(x, z)]) for z in y.transpose().mat] for x in self.mat])
	
	def norm(self):
		return sum([sum([abs(y) for y in x]) for x in self.transpose().mat])	


if __name__ == "__main__":
	a = Matrix([[1, 2, 3], [4, 5, 6]])
	b = Matrix([[1, 2, 3], [8, 5, 6]])
	
	# Setting attribute 
	a.mat = [[1, 2, 8], [4, 5, 6]]
	
	# print a e b
	print(a)
	print(b)
	
	# Testing equal
	if a == b:
		print("Uguali")
	
	# Testing sum
	c = a + b
	print(c)
	
	# Testing copy
	b.copy(a)
	print(b)
	
	# Testing multiply
	print(a.multiply(5))
	
	# Testing Transpose
	print(a.transpose())
	
	# Testing Multiplication
	c = Matrix([[(3)*y + (x+1) for x in range(3)] for y in range(3)])
	d = Matrix([[1, 2], [4, 5], [7, 8]])
	print(c)
	print(d)
	print(c * d)
	
	# Testing norm
	print(a.norm())
