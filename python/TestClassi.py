import unittest
from functools import reduce

def test_bad_input(matrix):
	class BadInputs(unittest.TestCase):
		def test_negative(self):
			""" Testa valori negativi per matrice quadrata """
			self.assertRaises(ValueError, matrix, -1)
		def test_zeros(self):
			""" Testa valori nulli per matrice quadrata """
			self.assertRaises(ValueError, matrix, 0)
	return BadInputs

def test_function(matrix, n):
	class Function(unittest.TestCase):
		def test_transpose(self):			
			self.assertEqual(matrix(n).transpose(), matrix(n)._mat)
		def test_determinant(self):			
			self.assertEqual(matrix(n).determinant(), 1)
		def test_sum_row_and_column(self):			
			self.assertEqual(matrix(n).sum_by_row(), matrix(n).sum_by_column())	
	return Function
		

class SquareMatrix(object):
	def __init__(self, n):
		if n < 1:
			raise ValueError("Non sono ammessi valori inferiori a 1")
		self._n = n
		self._mat = [y*[0] + [1] + ((n-1)-y)*[0] for y in range(n)]
		
	def transpose(self):
		return [[self._mat[x][y] for x in range(len(self._mat))] for y in range(len(self._mat[0]))]
	
	def sum_by_row(self):
		return sum([sum(self._mat[x]) for x in range(len(self._mat))])
	
	def sum_by_column(self):
		self.temp = self.transpose()
		return sum([sum(self.temp[x]) for x in range(len(self.temp))])
	
	def determinant(self):
		return reduce(lambda x,y: x*y,[self._mat[x][x] for x in range(len(self._mat))]) - \
			   reduce(lambda x,y: x*y,[self._mat[x][(self._n-1)-x] for x in range(len(self._mat))])

if __name__ == "__main__":
	badinput = test_bad_input(SquareMatrix)
	transpose = test_function(SquareMatrix, 3)
	unittest.main()
