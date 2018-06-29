import re

if __name__ == "__main__":
	lista =  ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
	
	#matching
	match = "Cavallo che scorre"
	
	dematch = re.match(r"(.*) che (.*)", match) 
	
	print(dematch.group())
	print(dematch.group(1))
	print(dematch.group(2))
	
	# findall
	print(re.findall(r"(?=c)\w+",match))
	
	#Sub	
	print([re.sub(" \(\.[a-z]+\)","",x) for x in lista])
