gray = lambda n: n and [x+y for x in '01' for y in gray(n-1)[::1-2*int(x)]] or ['']

printer = lambda x,func: print("{0} ~> {1}".format(x, func(*x)))

converter = lambda s:[int(x) for x in list(s)]

pretty = lambda n,func: list(map(lambda x: printer(converter(x),func), gray(n)))

if __name__ == '__main__':
	f0 = lambda x: 1-x
	f1 = lambda x,y: x&y
	f2 = lambda x,y,z: x&y|z
	pretty(1,f0)
	pretty(2,f1) 
	pretty(3,f2)
