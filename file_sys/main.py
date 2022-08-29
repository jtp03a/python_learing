# file = open("file.txt")

# contents = file.read()

# print(contents)

# file.close()

from importlib.resources import contents


with open("file.txt", mode="a+") as file:
  contents = file.read()
  print(contents)
  file.write("New text")