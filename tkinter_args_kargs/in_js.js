const add = (...numbers) => {
  let sum = 0
  for (const num of numbers) {
    sum += num
  }
  return sum
}

const add_reduce = (...numbers) => {
  return numbers.reduce((accumlator, num) => {
    return accumlator += num
  })
}

const add_reduce_succinct = (...numbers) => {
  return numbers.reduce((a, b) => a+b)
}

const calculate = (n, obj) => {
  console.log(n += obj['add'])
  console.log(n *= obj['multiply'])
}

calculate(3, {'add': 3, 'multiply': 3})

console.log(add(4,4,3,3,5,6,7,5,43))
console.log(add_reduce(4,4,3,3,5,6,7,5,43))
console.log(add_reduce_succinct(4,4,3,3,5,6,7,5,43))