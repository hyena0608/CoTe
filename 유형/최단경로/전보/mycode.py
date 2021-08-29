import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

distance = [INF] * (n + 1)

def dijkstra(c):
  q = []
  heapq.heappush(q, (0, c))
  distance[c] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

total_distance = 0
count = 0

dijkstra(c)

for _ in graph[c]:
  count += 1

for i in range(1, n + 1):
  if distance[i] == INF:
    continue
  if total_distance < distance[i]:
    total_distance = distance[i]
print(count, end = ' ')
print(total_distance)