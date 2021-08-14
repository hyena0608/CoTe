# 00시 00분 00초
#  N시 59분 59초

# 시간을 정한다.
# 그다지 의미가 없다? 24시에는?
n = int(input())

#분
# 03 13 23 33 43 53             // 6가지
# 30 31 32    34 35 36 37 38 39 // 9가지
# 초
# 6가지
# 9가지
# [a][b]시 [c][d]분 [e][f]초
# cdef 1씩 증가.. 4자리수
count = 0
d=1
f=1
for i in range(n + 1):
  for c in range(7):
    for d in range(10):
      for e in range(7):
        for f in range(10):
          if i == 3 or c == 3 or d == 3 or e == 3 or f == 3:
            count += 1

print(count)
