import inspect
import re

# TODO usare un decoratore

def inits(*args):
		val = re.findall("\w+",str(getattr(inits,args[0].__class__.__name__)))
		for x in range(len(args) - 1):
			args[0].__setattr__(val[x+1], args[x+1])

class AutoInit(type):
	def __new__(meta, classname, supers, classdict):
		inits.__setattr__(classname,inspect.signature(classdict["__init__"]))
		classdict["__init__"] = inits
		return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=AutoInit):
	def __init__(self, name, age): pass
	

class Car(metaclass=AutoInit):
	def __init__(self, model, code, color): pass
	
if __name__ == "__main__":
	a = Person("John", 15)
	b = Car("Lancia", "1234", "Bianco")
	
	print(a.name, a.age)
	print(b.model, b.code, b.color)
	
	
