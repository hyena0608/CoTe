n, m = map(int, input().split())

arr = (list(map(int, input().split())))

arr.sort()

max_height = 0

for i in range(arr[0], arr[n-1]):
  sum_now = 0
  for j in range(n):
    if arr[j] > i:
      sum_now += arr[j] - i

  if sum_now == m:
    if max_height < i:
      max_height = i

print(max_height) 


  