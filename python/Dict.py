class OrderedDict(dict):
		
	def items(self):
		#return sorted(super(OrderedDict,self).items())
		return sorted(dict.items(self))
	
	def __iter__(self):
		#return iter(sorted(super(OrderedDict,self).keys()))
		return iter(sorted(dict.keys(self)))
	
	def keys(self):
		#return sorted(super(OrderedDict,self).keys())
		return sorted(dict.keys(self))
		
	def __repr__(self):
		self._str = "{"
		return self._str + "".join(["'" + str(x) + "'" + ": " + str(self[x]) + ", " for x in sorted(super(OrderedDict,self).keys())])[:-2] \
		+ "}"		
	 
	 	
if __name__ == "__main__":     
	alkaline_earth_metals1 = [('barium', 56), ('beryllium', 4), ('calcium', 20),('magnesium', 12), ('radium', 88), ('strontium', 38)]    
	alkaline_earth_metals1 = sorted(alkaline_earth_metals1, key = lambda x: x[1]) 
	alkaline_earth_metals1 = dict(alkaline_earth_metals1)
	print(alkaline_earth_metals1)
	a = OrderedDict(alkaline_earth_metals1)
	a['z'] = 3
	a['a'] = 2
	print(a.items())
	print(a.keys())
	del a['z']
	print(a.items())
	print(a.keys())
	for key in a:
		print (key, 'corresponds to', a[key])
