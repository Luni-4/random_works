evaluate = lambda f,l: print("{0}\t:~> {1}".format(l, f(*l)))

def perm(n, f, l=[]):
	if n == 0:
		evaluate(f,l)
	else:
		perm(n-1, f, l+[0])
		perm(n-1, f, l+[1])	
		
if __name__ == '__main__':
	f0 = lambda x: 1-x
	f1 = lambda x,y: x&y
	f2 = lambda x,y,z: x&y|z
	perm(1,f0)
	perm(2,f1)
	perm(3,f2)
