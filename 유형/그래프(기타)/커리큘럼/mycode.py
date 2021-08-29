## 틀림

from collections import deque

n = int(input())

# 진입차수
graph = [0] * (n + 1)
indegree = [0] * (n + 1)
cost = [0] * (n + 1)
for i in range(1, n + 1):
  a = list(map(int, input().split()))
  graph[i] = a
  cost[i] = a[0]
  # 그래프 안에 뭐뭐 들었는지 확인하기
  # 그 안에 목록의 진입차수를 +1 해줘야한다.
  for j in range(1, len(a) - 1):
    if graph[i][j] == -1:
      break
    else:
      indegree[graph[i][j]] += 1

q = deque()

for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  # cost[now] = graph[now][0]

  for j in range(1, len(graph[now])-1):
    indegree[graph[now][j]] -= 1
    cost[graph[now][j]] += cost[now]

    if indegree[graph[now][j]] == 0:
      q.append(graph[now][j])

for i in range(1, n + 1):
  if indegree[i] == 0:
    print(cost[i])