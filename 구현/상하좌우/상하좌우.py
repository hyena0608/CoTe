n = int(input())
plans = input().split()
x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
  for i in range(len(move_types)):
    if move_types[i] == plan:
      x += dx[i]
      y += dy[i]
    if x < 1 or y < 1 or x > n or y >n:
      x -= dx[i]
      y -= dy[i]
print(x, y)    