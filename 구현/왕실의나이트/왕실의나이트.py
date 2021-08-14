# [0,0,0,0]

# UU = [-2, 0, 0, 0]
# DD = [0, 2, 0, 0]
# LL = [0, 0, -2, 0]
# RR = [0, 0, 0, 2]

# U = [-1, 0, 0, 0]
# D = [0, 1, 0, 0]
# L = [0, 0, -1, 0]
# R = [0, 0, 0, 1]


# UU + L or R // x, y >= 1, 1
# DD + L or R // x, y >= 1, 1
# LL + U or D // x, y >= 1, 1
# RR + U or D // x, y >= 1, 1
# a - 96 =

road_list = [(2,1), (2,-1), (-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

loc = input()
x_num = ord(loc[0]) - 96
y_num = int(loc[1])

count = 0

for road in road_list:
  x = road[0]
  y = road[1]
  if 1 <= x + x_num <= 8 and 1 <= y + y_num <= 8: 
    count += 1

print(count)
