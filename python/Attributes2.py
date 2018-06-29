from datetime import *

class Person(object):
	def __init__(self, name, lastname, birthday):
		self.setname(name)
		self.setlastname(lastname)
		divide = birthday.split("/")
		self.setbirthday(date(int(divide[2]), int(divide[1]), int(divide[0])))
	
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
		

		
class grade_average_descriptor(object):
	def __get__(self, instance, owner):
		assert len(instance._lectures) > 0, "Non puoi dividere per 0"
		return sum(instance._lectures.values()) / len(instance._lectures)	

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
		
	grade_average = grade_average_descriptor() 
	
	


class day_salary_descriptor(object):
	def __get__(self, instance, owner):
		return instance._pay_per_hour * 8
	def __set__(self, instance, amount):
		assert amount > 0, "Il salario per ora non può essere negativo"
		instance._pay_per_hour = amount / 8

class week_salary_descriptor(object):
	def __get__(self, instance, owner):
		return instance.day_salary * 5
	def __set__(self, instance, amount):
		assert amount > 0, "Il salario settimanale non può essere negativo"
		instance.day_salary = amount / 5

class month_salary_descriptor(object):
	def __get__(self, instance, owner):
		return instance.week_salary * 4
	def __set__(self, instance, amount):
		assert amount > 0, "Il salario mensile non può essere negativo"
		instance.week_salary = amount / 4
		
class year_salary_descriptor(object):
	def __get__(self, instance, owner):
		return instance.month_salary * 12
	def __set__(self, instance, amount):
		assert amount > 0, "Il salario annuale non può essere negativo"
		instance.month_salary = amount / 12
		


class Worker(Person):
	def __init__(self, *args):
		super(Worker, self).__init__(*args[:3])
		self._pay_per_hour = args[3]
		
	day_salary = day_salary_descriptor()
	week_salary = week_salary_descriptor()
	month_salary = month_salary_descriptor()
	year_salary = year_salary_descriptor()
	
	
class age_salary_descriptor(object):
	def __get__(self, instance, owner):
		return (date.today() - instance.getbirthday()).days
		
	def __set__(self, instance, birthday):
		divide = birthday.split("/")
		instance.setbirthday(date(int(divide[2]), int(divide[1]), int(divide[0])))
	
class Wizard(Person):
		
	age = age_salary_descriptor()	
		

if __name__ == "__main__":
	a = Student("Michele", "Valsesia", "25/10/2016")
	a.setdict("Matematica", 3)
	a.setdict("Geografia", 8)
	a.setdict("Italiano", 5)
	print(a.getbirthday().year)
	print(a.grade_average)
	b = Worker("Michele", "Valsesia", "25/11/2016", 5)
	print(b.day_salary)
	b.year_salary = 15000
	print(b._pay_per_hour)
	c = Wizard("Michele", "Valsesia", "25/12/2016")
	c.age = "25/10/2016"
	print(c.age)
	

