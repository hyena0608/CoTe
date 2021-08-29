INF = int(1e9) # 무한 의미

# 노드, 간선 개수 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)만들고, 모든 값을 INF로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 자기 자신으로 가는 비용 0 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 9

# 각 간선에 대해 정보를 입력받고, 그 값으로 초기화
for _ in range(m):
  # a와 b가 서로에게 가는 비용은 1이라 설정
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력받기
x, k = map(int(), input().split())

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1 출력
if distance >= INF:
  print("-1")
else:
  print(distance)