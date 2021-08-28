arr = list(map(int, input()))
result = 0
for i in arr:
  if i == 0 or i == 1:
    result += i
  else:
    if result == 0:
      result = 1 * i
    else:
      result *= i

print(result)
