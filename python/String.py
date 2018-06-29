import itertools

class String(str):

	def palindrome(self):
		self.temp = self.translate({"<":None, ">":None, ",":None, ";":None, ".":None, ":":None, '"':None, "!":None, \
					"?":None, "(":None, ")":None, " ":None}).lower()
		return self.temp == self.temp[::-1]
		
	def subtract(self, b, string):
		return "".join([b.__getitem__(p) for p in range(len(b)) if b.__getitem__(p) not in list(string)])
		
	def anagram(self, d):
		s = {"".join(p) for p in itertools.permutations(self) if ("".join(p) in d.keys() or "".join(p) in d.values())}
		return "{0} elementi trovati".format(len(s)) + ("" if len(s) == 0 else ": {0}".format(s))		
	
	
	
if __name__ == "__main__":
	a = String("Rise to vote, sir.")
	print(a.palindrome())
	
	b = String("Walter Cazzola")	
	print(a.subtract(b, "abcwxyz"))
	
	c = String("lenovo")	
	print(c.anagram({"prima":"enolov", "seconda":"enolvo"}))
