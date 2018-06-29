import string
import re

class PolishCalculator(object):

	def __init__(self,string):
		self._string = string.split()
		self._operand = {"+"	: lambda x,y : x+y,     \
						 "-"	: lambda x,y : x-y,     \
						 "*"	: lambda x,y : x*y,     \
						 "/"	: lambda x,y : x/y,     \
						 "**"	: lambda x,y : x**y,    \
						 "or"	: lambda x,y : x or y,  \
						 "and"	: lambda x,y : x and y, \
						 "not"	: lambda x :   not x    }
		self._stack = []
				  
		
	def convert(self):					
		self._sl = ""
		for y in reversed(self._string):
			if y in self._operand.keys():
				self._stack.append(y)			
			else:
				self._sl += (" " + y[::-1] if self._stack == [] else " " + y[::-1] + " " + self._stack.pop()[::-1])
		return self._sl[::-1]	
					
	
	def __str__(self):
		return "La conversione in infix è: {0}".format(self.convert())
		
	def check(self, x):
		self._boolean = {"T": True, "F": False}
		return self._boolean[x] if x in self._boolean else float(x)
		
		
	def eval(self, string):
		self._string2 = string.split()		
		for y in self._string2:			
			if y in self._operand.keys():
			
				if len(self._stack) == 1:
					return self._operand[y](self._stack.pop())
					
				secondo = self._stack.pop()
				primo = self._stack.pop()			 
				self._stack.append(self._operand[y](primo,secondo)) 				
			else:
				self._stack.append(self.check(y))
		return self._stack.pop()	
	
if __name__ == "__main__":
	a = PolishCalculator("3 4 +")
	print(a.convert())
	print(a.eval("T not"))
	
	
