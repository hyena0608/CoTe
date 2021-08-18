# 집합 자료형

n = int(input())
arrN = set(map(int, input().split()))

m = int(input())
arrM = list(map(int, input().split()))

for i in arrM:
  if i in arrN:
    print('yes', end=' ')
  else:
    print('no', end=' ')