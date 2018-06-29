import sys
import inspect

class TailRecurseException(Exception):
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs
    

def tail_recursion(g):
  def func(*args, **kwargs):
     f = sys._getframe()
     if  f.f_back.f_back != None:
       print("2", f.f_back.f_back.f_locals)
     else:
       print("2 None")	
     print("1", f.f_back.f_locals)
     print("0", f.f_locals)
     print()
     if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:     
        f.f_back.f_back.f_locals["put"] = f.f_locals["args"]              
     else:
       while 1:
         '''if "put" in f.f_locals:
            print("dentro")  
            return g(*(f.f_locals["put"]))
         else:'''
         return g(*args, **kwargs) 
  return func
  
'''def tail_recursion(g):
  def func(*args, **kwargs):
    f = sys._getframe()   
    if  f.f_back.f_back != None:
       print("2", f.f_back.f_back.f_locals)
     else:
       print("2 None")	
     print("1", f.f_back.f_locals)
     print("0", f.f_locals)
     if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code: 
      print("if")     
      raise TailRecurseException(args, kwargs)
     else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException as e:
          args = e.args
          kwargs = e.kwargs
  return func'''
  
  


@tail_recursion
def tfact(n, acc=1):
  if n == 0: return acc
  return tfact(n-1, n*acc)

#@tail_recursion
#def tfib(i, current = 0, next = 1):
  #if i == 0: return current
  #else: return tfib(i - 1, next, current + next)

if __name__ == "__main__":
  print("10000! :-", tfact(5))
  #print("fib(10000) :-", tfib(10000))


