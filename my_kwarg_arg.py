#*ARG  Topics


def sum_func(a, b):
  return a + b


add = sum_func(1, 2)
#print(add)


def sum_list(*args):
  return sum(args)


add_list = sum_list(1, 2, 3, 4, 5, 6)
#print(add_list)


def sum_method(*args):
  #print(args)
  return sum(args)


#add_value = sum_method(2,4,6,8,10[])
#print(add_value)

set_ = (1, 2, 3)
#print(set_, type(set_))
#print(*set_)
_set_ = ((1, 2, 3), 3, 5)
#print('NESTED: ', *_set_)


def sum_val(args):
  return sum(args)


list_variable = [1, 2, 4, 56]

plus_val = sum_val(list_variable)
#print(plus_val)

#array = [A1:A10]
#sum(array)


def display_name(*args):
  for arg in args:
    print(arg, end=" ")


display_name("Dr.", "|Spongebob", "Squarepants")


def add(*args):
  total = 0
  for arg in args:
    total = total + arg
  return total


print(add(2, 4, 6, 8))


def my_func(**kargs):
  for i, j in kargs.items():
    print(i, j)


my_func(name='gold', want='money', year=2023)

#Example of **kwargs with normal parameter


def func(*args, **kwargs):
  print(sum(args))
  print(kwargs)
  print(type(args))
  print(type(kwargs))


y = (2, 3, 4, 5)
z = {'a': 5, 'b': 6, 'c': 7, 'd': 8}

func(*y, **z)
