def perm(n, f, l=[]):
	if n == 0:
		print("{}: ---> {}".format(l, f(*l)))
	else:
		perm(n-1, f, l+[0])
		perm(n-1, f, l+[1])

def perm2(n, f):		
	conv = lambda x: list("".join(['0'] * (n-len(bin(x)[2:]))) + bin(x)[2:]) 
	
	for x in range(2**n):
		intver = [int(m) for m in conv(x)]
		print("{} ---> {}".format(intver, f(*intver)))
		
if __name__ == '__main__':
	f0 = lambda x: 1-x
	f1 = lambda x,y: x&y
	f2 = lambda x,y,z: x&y|z
	
	print("Versione con ricorsione\n")
	perm(1,f0)
	perm(2,f1)
	perm(3,f2)
	
	print("\n\nVersione che sfrutta il binario\n")
	perm2(1,f0)
	perm2(2,f1)
	perm2(3,f2)
