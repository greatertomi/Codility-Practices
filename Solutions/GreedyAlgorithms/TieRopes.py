def solution(k, array):
    count = 0
    total = 0
    for i in range(len(array)):
        total += array[i]
        if total >= k:
            total = 0
            count += 1

    return count

print(solution(4, [1, 2, 3, 4, 1, 1, 3]))
