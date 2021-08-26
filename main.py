from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1 # 필요한 것들 (가는거 X) 
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + cost[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


    for i in range(1, n + 1):
        print(result[i])

topology_sort()