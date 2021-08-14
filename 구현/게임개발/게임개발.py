n, m = map(int, input().split()) # n x m 맵
x, y, direction = map(int, input().split()) # 현재 위치 (x, y) 좌표와 향하고 있는 방향 direction

map = [[0] * m for _ in range(n)] # n x m 맵 초기화

arr = []
for i in range(n): # 맵 정보 n행 받아오기
  arr.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  

# 방향 (왼쪽) 회전
def turn_left():
  global direction
  if direction == -1:
    direction = 3
  direction -= 1


# 회전 후 이동
turn_left()
nx = x + dx[direction]
ny = y + dy[direction]
# 회전 한 이후 좌표 확인
if