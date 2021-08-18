# 파이썬 장점을 살린 퀵 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0] # 첫 번째 원소
  tail = arr[1:] # 나머지 원소

  left_side = [x for x in tail if x <= pivot] # 분할 왼쪽
  right_side = [x for x in tail if x > pivot] # 분할 오른쪽

# 분할 왼쪽 + 피벗 + 분할 오른쪽
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))