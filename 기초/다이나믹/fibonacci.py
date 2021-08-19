# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 피보나치 수열 : 탑다운
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo_topdown(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
  return d[x]

print(fibo(99))

# 피보나치 수열 : 보텀업
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d2 = [0] * 100

d2[1] = 1
d2[2] = 1
n = 99

for i in range(n+1):
  d2[i] = d2[i-1] + d2[i-2]

print(d[n])
