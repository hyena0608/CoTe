# append() 리스트 맨 뒤쪽에 삽입
# pop() 리스트 맨 뒤쪽 데이터 꺼내오기


stack = []


stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)


# 최하단 부터
print(stack)
# 최상단 부터
print(stack[::-1])