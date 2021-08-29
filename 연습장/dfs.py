# dfs
n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
  a = list(map(int, input().split()))
  graph[i] = a

visited = [False] * (n + 1)

def dfs(graph, v, visited):
  if visited[v] == False:
    print(v, end = ' ')
    visited[v] = True
    for i in graph[v]:
      dfs(graph, i, visited)
      
dfs(graph, 1, visited)