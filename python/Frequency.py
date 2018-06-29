def reader(filename):
	elem = {"<":None, ">":None, ",":None, ";":None, ".":None, ":":None, '"':None, "!":None, "?":None, "(":None, ")":None}
	
	with open(filename, encoding = "utf-8") as pattern:
		for line in pattern:
			words = ((line.translate(elem).lower())).split()
			yield words

def funcs(filename, number):
	d = dict()
	for x in reader(filename):
		k = [(elem,(x.count(elem) + d.get(elem))) if d.get(elem) != None else (elem,x.count(elem)) for elem in x]		
		d.update(dict(k))
	return sorted([elem for elem in d.items() if elem[1] > number], key = lambda x: x[1], reverse = True) 
					
if __name__ == "__main__":
	print(funcs(filename="open.txt", number = 1))
