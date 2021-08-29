n, m = map(int, input().split())
ball = list(map(int, input().split()))

count = 0
for i in range(n):
  for j in range(n - 1, i - 1, -1):
      if ball[i] != ball[j]:
        count += 1
print(count)