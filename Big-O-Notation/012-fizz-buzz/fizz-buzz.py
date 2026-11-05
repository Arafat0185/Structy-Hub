def fizz_buzz(n):
  list = []
  for num in range(1, n):
    if (num % 3 == 0 and num % 5 ==0):
      list.append("fizzbuzz")
    elif num % 3 == 0:
      list.append("fizz")
    elif num % 5 == 0:
      list.append("buzz")
    else:
      list.append(num)
  return list
      