from importlib.resources import contents

numbers = [1, 2, 3]
new_list = []
for n in numbers:
  add_1 = n + 1
  new_list.append(add_1)

print(new_list)

# can be rewritten as
new_list2 = [n + 1 for n in numbers]
print(new_list2)

name = 'Jacob'

new_list3 = [letter for letter in name]
print(new_list3)

double_num = [num *2 for num in range(1,5)]

print(double_num)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) <= 4]

print(short_names)

upper_names = [name.upper() for name in names if len(name) >=5]

print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num **2 for num in numbers]

print(squared_numbers)

even_numbers = [num for num in numbers if num%2==0]

print(even_numbers)

with open('file1.txt', mode='r') as file:
  file1 = [int(line) for line in file.readlines()]



with open('file2.txt', mode='r') as file2:
  file2 = [int(line) for line in file2.readlines()]

common_lines = [line for line in file1 if line in file2]

print(common_lines)


  