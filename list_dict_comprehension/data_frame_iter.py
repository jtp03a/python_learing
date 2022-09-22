import pandas

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)

for key, value in student_dataframe.items():
  print(key)
  print(value)

for (index, row) in student_dataframe.iterrows():
  print(index)
  print(row.student)