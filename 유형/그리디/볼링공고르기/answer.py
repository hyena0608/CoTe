n, m = map(int, input().split())
data = list(map(int ,input().split()))

start = time.time()
# 1부터 10까지의 무게를 담을 수 있는 리스트 ( 1 <= m <= 10)
array = [0] * 11

for x in data:
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
  n -= array[i] # 무게가 i인 볼링공의 개수를 제외 (무게가 i끼리의 중복을 제외하기 위해서)
  # result = 무게 i * n(무게 i를 제거한 나머지 무게)
  result += array[i] * n # B가 선택하는 경우의 수와 곱하기