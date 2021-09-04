# BFS
from collections import deque
n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i] = list(map(int, input().split()))

visited = [False] * (n + 1)

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    print(now)
    for i in graph[now]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

bfs(graph, 1, visited)