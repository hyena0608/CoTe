# 계수 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

sort_arr = [0] * (max(arr) + 1)

for i in range(len(arr)):
  sort_arr[arr[i]] += 1

for i in range(len(sort_arr)):
  for j in range(sort_arr[i]):
    print(i, end=' ')