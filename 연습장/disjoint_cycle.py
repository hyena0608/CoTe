n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(1, n + 1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

cycle = False
for _ in range(1, n + 1):
  a, b = map(int, input().split())
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
  else:
    cycle = True

if cycle:
  print("사이클O")
else:
  print("사이클X")