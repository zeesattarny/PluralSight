def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

# In the example shown above, make_pretty() is a decorator. In the assignment step.

# @make_pretty
# def ordinary():
#     print("I am ordinary")
# is equivalent to

# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

##########################################################################


def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@percent
def printer(msg):
    print(msg)
printer("Hello") 