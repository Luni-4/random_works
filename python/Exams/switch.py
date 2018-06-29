class Switch(object):
	
	cache = list()
	
	@classmethod
	def add(cls, k, v):
		cls.cache.append((k,v))
		
	def classi(self):
		return [x for x in Switch.cache if x[0].__qualname__[0] == self.__class__.__name__]
	
	def match(self,n):
		case = self.classi()
		func = None
		for x in case:
			if isinstance(x[1],list) or isinstance(x[1],tuple):
				if n in x[1]: func = x[0]
			else:
				if n == x[1]: func = x[0]
		if func == None: func = case[-1][0]
		def val(*args, **kwargs):
			return func(self,*args, **kwargs)
		return val		
		

def case(param):
	def val(f):
		Switch.add(f, param)
		return f
	return val
