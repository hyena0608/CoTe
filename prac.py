graph = [[0] for _ in range(5)]
print(graph)
print(graph[0])
graph[0].append((1, 2))
print(graph)
print(graph[0])
for i in graph[0]:
  print(i[1])
print(type(graph))

print("+=============")
graph2 = [0] * (5)
print(graph2)
print(type(graph2))
print(graph2[0]) 