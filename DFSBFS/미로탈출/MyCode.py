from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
  arr.append(list(map(int, input())))

#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def miro(x, y):
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어날 때
      if nx>=n or nx<0 or ny>=m or ny<0:
        continue
      # 괴물을 만났을 때
      if arr[nx][ny] == 0:
        continue
      # 정상적인 길일 때
      if arr[nx][ny] == 1:
        arr[nx][ny] = arr[x][y] + 1
        queue.append((nx, ny))
  return arr[n-1][m-1]

print(miro(0, 0))