import time

n, m = map(int, input().split())
ball = list(map(int ,input().split()))

start = time.time()
count = 0
for i in range(n):
  for j in range(n - 1, i - 1, -1):
      if ball[i] != ball[j]:
        count += 1
print(count)
print("time :", time.time() - start)

# 1.3589859008789062e-05
# 6.532669067382812e-05