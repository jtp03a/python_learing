import csv
import stat
import pandas
import statistics

with open("weather_data.csv") as weather_data:
  data = list(csv.reader(weather_data))
  temperatures = []
  for row in data[1:]:
    temperatures.append(int(row[1]))

  print(temperatures)

data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

data_dict = data.to_dict()

print (data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

avg = statistics.mean(temp_list)
print(avg)

def get_avg(num_list):
  return sum(num_list) / len(num_list)

print(get_avg(temp_list))

print(data['temp'].mean())

print(data['temp'].max())

print(data.temp.max())

print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.temp)

def c_temp_convert(temp):
  return (temp * 1.8) + 32

print(c_temp_convert(monday.temp))

# create a dataframe from scratch
data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [ 76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

new_data.to_csv('newdata.csv')

