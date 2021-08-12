# 배열 문법 공부하자

# 1) 1차원 배열
arr1 = [0, 0, 0, 0, 0]
print(arr1)

arr2 = [0] * 5
print(arr2)

arr2[0] = 1
print(arr2)

# 2) 2차원 배열
arr3 = [[0]*5 for _ in range(5)]
print(arr3)
arr3[0][1] = 1
print(arr3)
