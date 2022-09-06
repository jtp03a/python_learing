def repetition_decorator(repetitions):
  def decorator(func):
    def wrapper():
      for r in range(repetitions):
        func()
    return wrapper
  return decorator

@repetition_decorator(5)
def my_func():
  print('Function')

my_func()





