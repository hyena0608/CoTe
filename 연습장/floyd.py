# Floyd
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

for _ in range(m):  
  a, b, cost = map(int, input().split())
  graph[a][b] = cost

for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, n + 1):
  print()
  for j in range(1, n + 1):
    if graph[i][j] == INF :
      print('INF', end=' ')
    else:
      print(graph[i][j], end=' ')