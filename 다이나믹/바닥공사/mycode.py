import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range (3, n + 1):
  if i % 2 == 1: # 홀수
    d[i] = (2 * d[i-1] - 1) % 796796
  else: # 짝수
    d[i] = (2 * d[i-1] + 1) % 796796

print(d[n])