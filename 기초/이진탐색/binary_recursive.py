# 재귀 호출을 이용한 이진 탐색

target = int(input())

array = list(map(int, input().split()))

start = 0
end = len(array)

def binary_search(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] == target:
    print("target은 {}번째에 있다.".format(mid+1))
    # return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

binary_search(array, target, start, end)
