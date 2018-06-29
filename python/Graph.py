from datetime import date

class Graph(object):
	
	struct = []
	
	@classmethod
	def addStruct(cls, y):
		cls.struct.append(y)
	
	@classmethod
	def visit(cls):
		i = 0
		while i < len(cls.struct):		
			if cls.struct[i].friends == []:
				yield (cls.struct[i], "L'utente non ha amici")
			else:
				yield (cls.struct[i], "\n".join([str(x) for x in cls.struct[i].friends]))				
			i += 1
	
	def __str__(self):
		tratt = "".join(["-" for x in range(70)])		
		s = ["{}\n\nAmici\n\n{}\n{}\n".format(x[0], x[1], tratt) for x in Graph.visit()]		
		return "".join(s)
		
		

class Node(object):
	def __init__(self, name, lastname, birthday):
		self.name = name
		self.lastname = lastname
		divide = birthday.split("/")
		self.birthday = date(int(divide[2]), int(divide[1]), int(divide[0]))
		
		self.enroll = date.today()
		
		self.friends = []
		
		Graph.addStruct(self)

	def getFriends(self):
		return self.friends	
		
	def addFriend(self, y):
		if type(y).__name__ == "Node" and y not in self.friends and y != self:
			self.friends.append(y)
			y.friends.append(self)
	
	def __repr__(self):
		return "Sono {} {}, Nascita: {}, Iscrizione: {}".format(self.name, self.lastname, self.birthday, self.enroll)
	
	
if __name__ == "__main__":
	a1 = Node("Michele", "Ip", "25/01/2016")
	a2 = Node("Michele", "Ip", "25/01/2016")
	a3 = Node("Marco", "Noce", "25/01/2016")
	
	# Aggiunge un Amico
	a1.addFriend(a2)
	a2.addFriend(a1)
	a1.addFriend(a3)
	
	# Graph
	h = Graph()
	print(h)
	
	print(a1.getFriends())
	print(a2.getFriends())
	
	
	
	
	
	 
