
#http://code.activestate.com/recipes/578053-metaclass-and-deepcopy/

import inspect
import re

def deepcopy(l):
	return [deepcopy(elem) if type(elem).__name__ == "list" else elem for elem in l]

def delete(self):
	if self == []:
		current = inspect.currentframe()
		outer_frame = inspect.getouterframes(current)[1][4]
		code = re.findall(r"\w+", outer_frame[0])
		delete.__globals__[code[0]] = deepcopy(delete.__globals__[code[1]])

class DeepCopyList(type):
	def __new__(meta, classname, supers, classdict):
		classdict['__del__'] = delete
		return type.__new__(meta, classname, supers, classdict)
	def __init__(clazz, classname, supers, classdict):
		return supers.__init__(clazz, classname, supers, classdict)
		
original_list = list

list = DeepCopyList('list', (original_list,), dict(list.__dict__))

if __name__ == "__main__":
  mylist=list()
  seclist = list()
  mylist.append(0)
  mylist.append(1)
  mylist.append(2)
  mylist.append([7,8,9])
  seclist=mylist
  seclist[2] = "X"
  mylist[0] = 8
  seclist[1] = "tre"
  seclist[3][0] = "t"
  print(mylist)
  print(seclist)

