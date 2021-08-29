n = int(input())

student = []

for i in range(n):
  student.append((input().split()))

def jumsu(data):
    return data[1]

result = sorted(student, key=jumsu)

for i in range(n):
  print(result[i][0], end=' ')