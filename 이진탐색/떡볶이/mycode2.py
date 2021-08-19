# 떡의 개수   1,000,000
# 떡의 길이   2,000,000,000
# 절단기 높이 1,000,000,000

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
  mid = (start + end) // 2
  sum = 0
  for i in arr:
    # 잘랐을 때 떡의 양 계산
    if i > mid:
      sum += i - mid

  # 잘린 떡의 양이 충분한 경우 덜 남게 자르기 (절단기 높이 높이기)
  if sum >= m:
    result = mid # 최대한 덜 잘랐을 때 정답
    start = mid + 1
  # 잘린 떡의 양이 부족한 경우 더 많이 남게 자르기 (절단기 높이 줄이기)
  else:
    end = mid - 1

print(result)