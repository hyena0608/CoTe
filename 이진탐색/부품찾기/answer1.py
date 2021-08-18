# 이진 탐색 소스코드 구현(반복문)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n = int(input())
arrN = list(map(int, input().split()))
arrN.sort()
m = int(input())
arrM = list(map(int, input().split()))

for i in arrM:
  result = binary_search(arrN, i, 0, n-1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')