from types import FunctionType

class CG(type):
	def __new__(meta, classname, supers, classdict):
		changed = []
		for attr, attrvalue in classdict.items():
			if type(attrvalue) is FunctionType:
				decorated = cg(attrvalue, classname)
				classdict[attr] = decorated
				changed.append(decorated)
		ma = type.__new__(meta, classname, supers, classdict)
		for decorated in changed:
			decorated._f.__globals__[classname] = ma
		return ma
	
class Stack(object):
	stack = ["main"]
	superstack = []
	@classmethod
	def isnotin(cls, l, ll): 
		indices = [i for i, x in enumerate(ll) if x == l[0]]
		return not any([l == ll[i:len(l)] for i in indices])
	@classmethod
	def push(cls, e): cls.stack.append(e)
	@classmethod
	def pop(cls): return cls.stack.pop()
	@classmethod
	def superpush(cls): 
		if all([cls.isnotin(cls.stack, ll) for ll in cls.superstack]):
			cls.superstack.append(cls.stack[:])
	



class cg(object):
	def __init__(self, f, classname):
		self._f = f
		self._classname = classname
	
	def __call__(self, *args, **kwargs):
		Stack.push("{}.{}({})".format(self._classname,self._f.__name__,*args))
		tmp = self._f(*args, **kwargs)
		Stack.superpush()
		Stack.pop()
		if len(Stack.stack) == 1:
			with open("cg.dot", "w", encoding = "UTF-8") as out:
				out.write(self.graph())
		return tmp
	def graph(self):
		res = "strict digraph cg {\n"
		for t in Stack.superstack: 
			res += "   "+" -> ".join(t)+"\n"
		return res + "}\n"
		




import ABC

A = CG("A", (), dict(ABC.A.__dict__))
B = CG("B", (), dict(ABC.B.__dict__))
C = CG("C", (), dict(ABC.C.__dict__))

if __name__ == "__main__":
   A.a(10)
   
