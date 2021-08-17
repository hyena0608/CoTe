from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
  arr.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def miro(x, y):
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    print("(x, y) = ({}, {})".format(x, y))

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 넘었을 때
      if nx>=n or ny>=m or nx<0 or ny<0:
        print("범위(nx, ny) = ({}, {})".format(nx, ny))
        continue
      # 괴물을 만났을 때
      if arr[nx][ny] == 0:
        print("괴물(nx, ny) = ({}, {})".format(nx, ny))
        continue
      # 갈 수 있을 때
      if arr[nx][ny] == 1:
        queue.append((nx, ny)) # 내가 간 현재 위치 등록
        print("(nx, ny) = ({}, {})".format(nx, ny))
        arr[nx][ny] = arr[x][y] + 1 # 현재 몇 번째 노드인지 숫자 매기기
        print("arr[{}][{}] = {}".format(nx,ny,arr[nx][ny]))
      else:
        print("이미 지나침 (nx, ny) = ({}, {})".format(nx, ny))

  return arr[n-1][m-2]

print(miro(0, 5))

# 05 15