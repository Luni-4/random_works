import sys
import inspect

class TailRecurseException(Exception):
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_recursion(g):
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException as e:         
          args = e.args
          kwargs = e.kwargs
  return func
  
  


@tail_recursion
def tfact(n, acc=1):
  if n == 0: return acc
  return tfact(n-1, n*acc)

@tail_recursion
def tfib(i, current = 0, next = 1):
  if i == 0: return current
  else: return tfib(i - 1, next, current + next)

if __name__ == "__main__":
  print("10000! :-", tfact(1))
  print("fib(10000) :-", tfib(10000))


