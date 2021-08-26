def multiple(num):
  return_value = 1
  for index in range(1, num + 1):
    return_value = return_value * index


def multiple2(num):
  if num <= 1:
    return num
  return num * multiple2(num-1)


def sum_list(data):
  if len(data) == 1:
    return data[0]
  return data[0] + sum_list(data[1:])

def palindrome(string):
  if len(string) <= 1:
    return True  
  if string[0] == string[-1]:
    return palindrome(string[1:-1])
  else:
    return False

def sol1(n):
  print(n)
  if n == 1:
    return n

  if n%2 == 0:
    return sol1(n/2)
  else:
    return sol1(n*3 + 1)
sol1(3)

def func(data):
  if data == 1:
    return 1
  elif data == 2:
    return 2
  elif data == 3:
    return 4
  
  return func(data-1) + func(data-2) + func(data-3)
   