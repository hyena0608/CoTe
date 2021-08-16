n, m = map(int, input().split())

arr = []
for i in range(n):
  arr.append(list(map(int,input())))


def ice(x, y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False 
  if arr[x][y] == 0:
    arr[x][y] = 1
    ice(x+1, y)
    ice(x-1, y)
    ice(x, y+1)
    ice(x, y-1)
    return True
  return False


count = 0
for i in range(n):
  for j in range(m):
    if ice(i, j) == True:
      count += 1

print(count)
