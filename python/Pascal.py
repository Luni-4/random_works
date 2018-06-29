from math import factorial

class Pascal(object):
	def __init__(self, n):
		self._n = n
		self._reversed = False
		self._step = []
	
	def __reversed__(self):
		self._reversed = True
		return self.__iter__()
	
	def __iter__(self):
		self.ntemp = self._n if self._reversed else 0
		return self
		
	def down(self):		
		if(self.ntemp < 0):			
			raise StopIteration
		
	def up(self):
		if(self.ntemp > self._n):
			raise StopIteration			
		
		
	def __next__(self):
	
		if self._reversed:
			self.down()
		else:
			self.up()
			
		if(-1 < self.ntemp < 2):
			self._step = [1] * (self.ntemp + 1) 
			self.ntemp = self.ntemp - 1 if self._reversed else self.ntemp + 1
			return iter(self._step)
			
		
		self.divide = self.ntemp // 2 	
		self._step = [1] + [factorial(self.ntemp) // (factorial(p+1) * factorial(self.ntemp-(p+1))) for p in range(self.divide)]
		self._step = self._step + self._step[self.divide-1::-1]  if self.ntemp % 2 == 0 else self._step + self._step[::-1]
		
		self.ntemp = self.ntemp - 1 if self._reversed else self.ntemp + 1
		
		return iter(self._step)
	
			
if __name__ == "__main__":
	m = list(p for p in Pascal(14))
	print(m)
