weather_c = {
  'Monday': 12,
  'Tuesday': 14,
  'Wednesday': 15,
  'Thursday': 14,
  'Friday': 21,
  'Saturday': 22,
  'Sunday': 24
}

const process_obj = (obj, func) => {
  new_obj = {}
  for (const property in obj) {
    new_obj = {...new_obj, [property]: func(obj[property])}
  }
  return new_obj
}

const weather_f = process_obj(weather_c, (degrees) => degrees * 1.8 + 32)

console.log(weather_f)
console.log(weather_c)

// console.log(weather_f)

