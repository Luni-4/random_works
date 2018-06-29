from datetime import *
from types import FunctionType 

class Counter(type):
	c = 0		
	def __call__(Class, *args, **kwargs):
		if Class.__name__ == "Person":
			Counter.c += 1
			print("Numero di istanze di Person:", Counter.c)
		return super().__call__(*args, **kwargs)

class Spell(type):
	
	def __call__(Class, *args, **kwargs):
		if Class.__name__ == "Person":
			l = [cls for cls in Class.__subclasses__() if cls.__name__ == "Worker"]
			return l[0].__call__(*args, 5, **kwargs) 
		return super().__call__(*args, **kwargs)
		
def count(f):
	c = 0
	def add(*args, **kwargs):
		nonlocal c
		c += 1
		if c > 1:
			return f(*args, **kwargs)
		return "Prima volta che istanza invoca il metodo"
	return add
			

class MultiTriggeredMethod(type):
	def __new__(meta, classname, supers, classdict):
		for attr, attrvalue in classdict.items():
			if attr != "__init__" and type(attrvalue) is FunctionType:
				classdict[attr] = count(attrvalue)
		return type.__new__(meta, classname, supers, classdict)			
	
		

class Person(metaclass=Counter):

	def __init__(self, name, lastname, birthday):
		self._name = name
		self._lastname = lastname
		divide = birthday.split("/")
		self._birthday = date(int(divide[2]), int(divide[1]), int(divide[0]))
	
	def getname(self):
		return self._name
	
	def getlastname(self):
		return self._lastname
	
	def getbirthday(self):
		return self._birthday
		
	def setname(self,name):
		self._name = name
	
	def setlastname(self, lastname):
		self._lastname = lastname
	
	def setbirthday(self, birthday):
		self._birthday = birthday
	
	def __repr__(self):
		return "Mi chiamo {0} {1} e sono nato il {2}/{3}/{4}".format(self._name, self._lastname, self._birthday.day, self._birthday.month, self._birthday.year)

class Student(Person):
	def __init__(self, *args):
		super(Student, self).__init__(*args)
		self._lectures = dict()
		
	def getdict(self):
		return self._lectures
	
	def setdict(self, lectur, mark):
		self._lectures[lectur] = mark
	
	def deldict(self, lectur):
		self._lectures.pop(lectur)
		
	def getaverage(self):
		assert len(self._lectures) > 0, "Non puoi dividere per 0"
		return sum(self._lectures.values()) / len(self._lectures)		
		
	grade_average = property(getaverage, None, None, "Calcolo della media di uno studente")

class Worker(Person):
	def __init__(self, *args):
		super(Worker, self).__init__(*args[:3])
		self._pay_per_hour = args[3]
	
	def get_day_salary(self):
		return self._pay_per_hour * 8
		
	def set_day_salary(self, amount):
		self._pay_per_hour = amount / 8
	
	def get_week_salary(self):
		return self.get_day_salary() * 5
		
	def set_week_salary(self, amount):
		self.set_day_salary(amount/5)
		
	def get_month_salary(self):
		return self.get_week_salary() * 4
		
	def set_month_salary(self, amount):
		self.set_week_salary(amount/4)
		
	def get_year_salary(self):
		return self.get_month_salary() * 12
		
	def set_year_salary(self, amount):
		self.set_month_salary(amount/12)
	
	day_salary = property(get_day_salary, set_day_salary, None)
	week_salary = property(get_week_salary, set_week_salary, None)
	month_salary = property(get_month_salary, set_month_salary, None)
	year_salary = property(get_year_salary, set_year_salary, None)
	
class Wizard(Person):
	def get_age(self):
		return (date.today() - self.getbirthday()).days
	
	def set_age(self, birthday):
		divide = birthday.split("/")
		self.setbirthday(date(int(divide[2]), int(divide[1]), int(divide[0])))
		
	age = property(get_age, set_age, None)


if __name__ == "__main__":
	print(type(Person))
	a = Person("Michele", "Ip", "25/10/2016")
	b = Student("Michele", "Ip", "25/10/2016")
	print(a.getname())
	print(a.getname())
	print(a.getlastname())
	print(a.getlastname())			
	c = Worker("Michele", "Ip", "25/10/2016", 5)
	c.set_month_salary(50)
	d = Person("Michele", "Ip", "25/10/2016")
	
