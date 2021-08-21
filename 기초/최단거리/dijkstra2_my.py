import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

# 노드, 간선
n, m = map(int, input().split())

# 시작 노드 받기
start = int(input())

# 사용할 자료구조 : 큐(거리, 노드), 그래프(노드 a, [노드 b, 거리]) -> 초기화 시켜야함
# 사용할 데이터 : discount .. 거리.. 

# 노드 0번 빼고 1번부터 시작하게 설정 -> n노드까지 만들어야함 -> range(n + 1)
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 모두 무한으로 초기화 -> 위에 노드 인덱스를 맞춰주자 -> `
distance = [INF] * (n + 1) 

# 간선 정보 입력 받자
for i in range(m):
  # 노드 a, 노드 b, 사이 거리 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  
# 다익스트라 알고리즘
# 최단 거리를 가진 노드들을 PQ로 받아 최적의 거리들을 계산한다.
# 1. 최단 거리를 얻게 되면 distance를 갱신 시켜줘야한다.
# 2. 최단 거리로 도착한 노드를 큐에 넣어준다.
# 3. 힙 구조로 이루어진 우선순위 큐가 비어있지 않으면 하나를 빼서 연결된 노드들과의 최단 거리를 다시 비교하고 계산한다.

def dijkstra(start):
  # 큐 자료구조 생성
  q = []
  # 시작 노드 start로 가기 위한 최단 경로는 0 
  heapq.heappush(q, (0, start)) # 1. 큐 설정
  distance[start] = 0 # 2. 최단 거리 테이블 설정
  while(q): # 큐가 비어있지 않으면
    # 가장 최단 거리 짧은 노드 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드의 최단 거리가 이미 최적(최단)으로 처리되었으면 무시하는 함수 (굳이 안해도 된다. 최적화1)
    if distance[now] < dist:
      continue # while문으로 돌아가기
    # 처리 되지 않은 최단 거리의 노드의 인접한 노드들 확인하기
    for i in graph[now]:
      # cost = 원래 노드까지 거리 + 원래 노드에서 인접 노드까지 거리
      cost = dist + i[1]
      # 만약 cost가 원래 인접 노드까지 가는데 거리보다 짧으면 (최단거리 탄생)
      if cost < distance[i[0]]:
        # 최단 거리 테이블 재설정 해주기
        distance[i[0]] = cost
        # 갱신된 최단 거리 큐에 넣어주기
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])