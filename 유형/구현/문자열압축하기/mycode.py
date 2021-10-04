def solution(s):
    if len(s) == 1:
        return 1
    index = 0
    result = []
    repeated_count = 1
    arr = []
    for count in range(1, len(s)//2 + 1):
        for i in range(count, len(s) + count, count):
            if s[index:i] == s[i:i + count]:
                repeated_count += 1
                index = i
            else:
                if repeated_count != 1:
                    arr += (str(repeated_count))
                    arr += (s[index:i])
                else:
                    arr+=(s[index:i])
                index = i
                repeated_count = 1
        result.append(len(arr))
        arr = []
        index = 0
        repeated_count = 1

    return min(result)