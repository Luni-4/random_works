from multitriggered import *

class ToBeMultiTriggered:
	def m1(self):
		print("### m1 has been called")
	
	@multi_triggered(2, lambda x,y: x*y)
	def m2(self, i):
		print("### m2({0}) has been called!".format(i))
	
	@multi_triggered(3, lambda x,y: x+y)
	def m3(self,x,y): 
		print("### m3({0}, {1}) has been called!".format(x,y))

if __name__ == '__main__':
	to_be = ToBeMultiTriggered()
	to_be.m1()
	to_be.m2(5)
	to_be.m3('a',3)
	to_be.m2(7)
	to_be.m3('b',5)
	to_be.m2(3)
	to_be.m3('c',7)
