import sys

input = sys.stdin.readline

food_times = list(map(int, input().split()))
k = int(input())
loc = 0
count = 0
def solution(food_times, k):

    global loc
    global count

    x = fun(food_times, k, loc, count) + 1

    if sum(food_times) != 0:
        if x == len(food_times):
            x = 0
        while food_times[x] != 0:
            if food_times[x] != 0:
                break
            else:
                x += 1

        answer = x + 1
    return answer


def fun(food_times, k, loc, count):
    while count != k:
        if sum(food_times) == 0:
            print(-1)
            break
        if food_times[loc] == 0:
            loc += 1
        elif loc >= len(food_times) - 1:
            loc = 0        
        else:
            food_times[loc] -= 1
            count += 1
            return fun(food_times, k, loc + 1, count)
    return loc

print(solution(food_times, k))