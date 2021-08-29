s = list(map(int, input()))
changed = 0 
for i in range(len(s) -1):
  if s[i] != s[i + 1]:
    changed += 1

if changed % 2 == 0:
  print(int(changed / 2))
else:
  print(int(changed // 2 + 1))