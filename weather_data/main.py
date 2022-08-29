import csv

with open("weather_data.csv") as weather_data:
  data = list(csv.reader(weather_data))
  temperatures = []
  for row in data[1:]:
    temperatures.append(int(row[1]))

  print(temperatures)