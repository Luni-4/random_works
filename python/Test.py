import unittest
import string

# Inverte la stringa
def anagram(sample):		
		if sample == sample[::-1]:
			return sample[::-1]


class NotPresentError(ValueError): pass

	
def validate(string):

	win = ([0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6])
	
	l = list(string)
	x = l.count("X")
	o = l.count("O")
	sp = l.count(" ")
	
	if sp == 9:
		raise NotPresentError("Stringa vuota non valida") 
	
	if (x + o + sp) != 9:
		raise NotPresentError("Ci sono simboli non corretti")
	
	if not ((x == o) or (o == x - 1) or (x == o-1)):
		raise NotPresentError("Combinazione errata")					  
	
	c = 0	
	for index in win:
		if (string[index[0]] == string[index[1]]) and (string[index[1]] == string[index[2]]):
			winner = string[index[0]]
			c += 1
	
	if c > 1:
		raise NotPresentError("Più combinazioni vincenti contemporaneamente")
	
	if c == 1:	
		return "Ha vinto il giocatore " + winner
	
	if sp == 0:
		return "La partita è finita in parità"			
	
	return "Si possono ancora fare mosse"	
		

class Test(unittest.TestCase):

	palindrome = {"Do geese see God?", "Rise to vote, sir.", "Anna"}
	punteggiatura = {"<":None, ">":None, ",":None, ";":None, ".":None, ":":None, '"':None, "!":None, "?":None, "(":None, ")":None, " ":None} 						
	def test_palindrome(self):	
		for s in self.palindrome:
			s = s.translate(self.punteggiatura).lower()
			self.assertEqual(anagram(anagram(s)), s) 

class Test_tris(unittest.TestCase):
	
	def test_tris_bad_input(self):
		"""validate fallisce con configurazioni scritte male"""
		for s in ("         ", "gXXXXOXO X", "XXXOOOXXX", "XXXXXXXXX"):
			self.assertRaises(NotPresentError, validate, s)
	
	def test_tris_win_parity(self):
		for s in ("OXXXOOXOO", "OXXXOOXOX", "OXXXOOXO ", "XOOOXXOXX"):
			self.assertIn(validate(s), ["La partita è finita in parità", "Ha vinto il giocatore O", "Ha vinto il giocatore X", "Si possono ancora fare mosse"])
			
		
	
if __name__ == "__main__":
	unittest.main()
