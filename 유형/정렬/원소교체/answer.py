n, k = map(int, input().split()) # n, k 입력받기
a = list(map(int, input().split())) # a 배열 입력받기
b = list(map(int, input().split())) # b 배열 입력받기

a.sort() # 배열 a 오름차순
a.sort(reverse=True) # 배열 b 내림차순

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
  # a < b
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else: # a >= b
    break

print(sum(a)) # 배열 a의 모든 원소의 합 출력
