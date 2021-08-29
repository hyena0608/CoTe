x = int(input())

count = 0

def make_x_one(x):
  global count
  if x == 1:
    return count
  count += 1
  if x % 5 == 0:
    x /= 5
    return make_x_one(x)
  elif x % 3 == 0:
    x /= 3
    return make_x_one(x)
  elif x % 2 == 0:
    x /= 2
    return make_x_one(x)
  else:
    x -= 1
    return make_x_one(x)

print(make_x_one(x))