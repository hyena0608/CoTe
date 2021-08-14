n, m = map(int, input().split()) # n x m 맵
x, y, direction = map(int, input().split()) # 현재 위치 (x, y) 좌표와 향하고 있는 방향 direction

# 내가 지나간 정보를 위한 n x m 맵
my_map = [[0] * m for _ in range(n)]
# 현재 내 위치
my_map[x][y] = 1

# 바다 육지 정보
arr = []
for i in range(n): # 맵 정보 n행 받아오기
  arr.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  

# 방향 (왼쪽) 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3
  

# 시작
count = 1
turn_time = 0
while True:
  # 회전 후 이동
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 한 이후 좌표 확인 / 정면 칸에 안가봤으면 이동
  # 내가 방문한 맵 / 바다와 육지 맵
  if my_map[nx][ny] == 0 and arr[nx][ny] == 0:
    my_map[nx][ny] = 1
    x = nx # 현재 내 위치 바꾸기
    y = ny 
    count += 1 # 한번 이동 추가
    turn_time = 0 # 회전 안함
    continue
  else: # 만약 정면이 바다거나 가봤던 칸이면
    turn_time += 1 # 한번 회전해본다.
  # 네 방향 다 가지 못하면
  if turn_time == 4:
    nx = x - dx[direction] # 원래 왔던 곳으로 되돌아가기 위한 좌표 만들기
    ny = y - dx[direction]
    # 뒤로 갈 수 있다면 다시 뒤로가기
    if arr[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤로 못간다면 (바다)
    else:
      break # 시뮬레이션 끝.
    turn_time = 0 # 회전 횟수 0 초기화

# 출력
print(count)
