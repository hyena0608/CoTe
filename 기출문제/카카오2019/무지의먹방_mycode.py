food_times = list(map(int, input().split()))
k = int(input())
loc = 0
count = 0

while count != k:

    if food_times[loc] == 0:
        if loc == len(food_times):
            for i in range(len(food_times)):
                if food_times[i] != 0:
                    loc = i
                    continue
        for j in range(loc, len(food_times)):
            if food_times[j] != 0:
                food_times[j] -= 1
                loc = j + 1
                count += 1
                continue
    else:
        food_times[loc] -= 1
        count += 1
        if loc + 1 == len(food_times):
            loc = 0
        else:
            loc += 1

    if sum(food_times) == 0:
        print(-1)
        break

if sum(food_times) != 0:
    if loc == len(food_times):
        loc = 0
    while food_times[loc] != 0:
        if food_times[loc] != 0:
            break
        else:
            loc += 1
    print(loc + 1)
