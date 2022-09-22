def add(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

print(add(1,5,6,8,4,3,6,7,5,4,3,4,5,66,5,4))

# get will return none if the key doesnt exist
class Car:
  def __init__(self, **kw):
    self.make = kw.get('make')
    self.model = kw.get('model')

my_car = Car(make = 'Honda')
print(my_car.model)