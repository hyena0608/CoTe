# 퀵 정렬 1

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(arr, start, end):
  pivot = start
  left = pivot + 1
  right = end
  if left >= right:
    return
  while left <= right:
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    while right > start and arr[right] >= arr[pivot]:
      right -= 1
    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else:
      arr[right], arr[left] = arr[left], arr[right]
  quicksort(arr, start, right-1)
  quicksort(arr, right+1, end)


quicksort(arr, 0, len(arr)-1)
print(arr)
