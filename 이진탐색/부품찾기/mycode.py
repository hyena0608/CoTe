# 이진

n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))

arrN.sort()
arrM.sort()

def binary_search(array, target, start, end):
  if start > end:
    return 'no'

  mid = (start + end) // 2

  if array[mid] == target:
    return 'yes'
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

result = []

for i in range(m):
  start = 0
  end = n-1
  result.append(binary_search(arrN, arrM[i], start, end))

for i in range(m):
  print(result[i], end=' ')