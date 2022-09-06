# with arguments

# def decorator(func):
#   def wrapper(wrapper_parameter):
#     print('dec begins')
#     func(wrapper_parameter)
#     print('dec ends')
#   return wrapper

# you see this often - unpacking operators *args - for list, **kwargs - dictionary
def decorator(func):
  def wrapper(*args, **kwarg):
    print('dec begins')
    func(*args, **kwarg)
    print('dec ends')
  return wrapper

@decorator
def my_func(func_parameter):
  print(func_parameter)

my_func('Hello')