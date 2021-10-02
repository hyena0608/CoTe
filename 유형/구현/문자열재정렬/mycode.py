# 08 문자열 재정렬

s = list(map(str, input()))

num = 0
context = []
for c in s:
    if c.isdigit():
        num += int(c)
    else:
        context.append(c)

print(''.join(sorted(context)), end='')
if num != 0:    
    print(num)