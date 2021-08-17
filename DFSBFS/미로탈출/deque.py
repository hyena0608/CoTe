from collections import deque
queue = deque()

queue.append((1,2))
queue.append((2,3))
queue.append((1,2))

print(queue)