# 반복문을 이용한 이진 탐색

target = int(input())

array = list(map(int, input().split()))

start = 0
end = len(array)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1 
  return None

print("target은 {}번째에 있다.".format(binary_search(array, target, start, end)+1))