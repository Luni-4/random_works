import sys,os
from stat import *

exclude = [".zip"]
			
def print_file(i):
	for x in readfile(i):
		print(x)
			
'''def cat(dire):
	for files in os.listdir(dire):
		if os.path.isfile(files) and os.path.splitext(files)[1] not in exclude:
			print_file(files)'''

def do_print(lst):
	[print(r) for r in lst]


def cat(fn):
	print(open(fn).read()[-2::-1])


if __name__ == "__main__":
	print(["Ciao", "Ok", "basta"][::-1])
	#do_print(["Ciao", "Ok", "basta"])
	cat(sys.argv[1])
	
