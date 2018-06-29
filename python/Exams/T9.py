import sys

key = {	       'a': '2', \
			   'b': '2', \
			   'c': '2', \
			   'd': '3', \
			   'e': '3', \
			   'f': '3', \
			   'g': '4', \
			   'h': '4', \
			   'i': '4', \
			   'j': '5', \
			   'k': '5', \
			   'l': '5', \
			   'm': '6', \
			   'n': '6', \
			   'o': '6', \
			   'p': '7', \
			   'q': '7', \
			   'r': '7', \
			   's': '7', \
			   't': '8', \
			   'u': '8', \
			   'v': '8', \
			   'w': '9', \
			   'x': '9', \
			   'y': '9', \
			   'z': '9'
		}

myDict = dict()
res = []

def WordToNum(word):	
	return "".join([key[char] for char in word])
	
def readDict(filename):
	with open(filename, encoding="UTF-8") as pattern:
		for word in pattern:
			word = word.rstrip()
			num = WordToNum(word)
			myDict[num] = myDict.get(num,[]) + [word]

def unroll(myList, string = ""):

	if len(myList) == 0:
		return string
		
	for i in range(len(myDict[myList[0]])):
	
		if i == len(myDict[myList[0]]) - 1: 
			return unroll(myList[1:], string + myDict[myList[0]][i] + " ") 
		else:
			res.append(unroll(myList[1:], string + myDict[myList[0]][i] + " "))

def readFile(filename):

	with open(filename, encoding="UTF-8") as pattern:
		for line in pattern:
			res.append(unroll(line.split()))
	print(res)

if __name__ == "__main__":
	readDict(sys.argv[1])
	readFile(sys.argv[2])
