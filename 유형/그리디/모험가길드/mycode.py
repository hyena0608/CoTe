import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
group_num = n // arr[0] + 1
print(group_num)