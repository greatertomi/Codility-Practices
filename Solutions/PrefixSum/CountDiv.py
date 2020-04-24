def solution(start, end, mod):
    if start > end or mod == 0:
        return None

    countDiv = 0
    for num in range(start, end):
        if (num > mod) and (num % mod == 0):
            countDiv += 1

    return countDiv

print(solution(10, 10, 7))
