import sys
from string import *

dict_line = {}	

def readfile(filename):
	c = 1
	with open(filename, encoding = "UTF-8") as pattern:
		for line in pattern:
			dict_line[str(c)] = line.split()
			c += 1

check = lambda x: x.lower() != "the" and x.lower() != "and" and len(x) > 2
			
def output():
	word = sorted([(key,l) for key in dict_line.keys() for l in dict_line[key] if check(l)], key = lambda x: x[1])
	for key, words in word:
		left = " ".join(dict_line[key][:dict_line[key].index(words)])
		right = " ".join(dict_line[key][dict_line[key].index(words) + 1:])
		print("{:>5} {:>33} {:<40}".format(key, left[-33:], (words + " " + right)[:40]))
		
		# Altro tipo di formattazione
		#print(key.rjust(5), left.rjust(33)[-33:], (words + " " + right).ljust(40)[:40])
	
		
	
if __name__ == "__main__":
	readfile(sys.argv[1])
	output()
