import time

# I want to add functionality without changing the orginal function
def decorator(func):
  def wrapper():
    print('New Functionality A')
    func()
    print('New Functionality B')
  return wrapper

def duration_decorator(my_func):
  def wrapper():
    start_time = time.time()
    my_func()
    duration = time.time() - start_time
    print('The duration decorator')
    print(f'duration: {duration}')
  return wrapper

def double_exec_decorator(my_func):
  def wrapper():
    my_func()
    my_func()
  return wrapper


# new_func_w_extra = decorator(my_func)

# new_func_w_extra()

# Shorthand

@decorator
@double_exec_decorator
@duration_decorator
def my_func():
  print('my original function')
  time.sleep(1)

my_func()

