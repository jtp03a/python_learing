import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name:random.randint(1, 100) for name in names}
print(student_scores)
passing_score = {name:score for name, score in student_scores.items() if score > 70 }
print(passing_score)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)

weather_c = {
  'Monday': 12,
  'Tuesday': 14,
  'Wednesday': 15,
  'Thursday': 14,
  'Friday': 21,
  'Saturday': 22,
  'Sunday': 24
}

weather_f = {day:temp * 1.8 + 32 for day, temp in weather_c.items()}

print(weather_f)

