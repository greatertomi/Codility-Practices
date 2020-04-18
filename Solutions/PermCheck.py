def solution(array):
    if (len(array) != len(set(array))) or (len(array) < 1):
        return 0

    isPerm = None
    for i in range(len(array)):
        if i+1 != array[i]:
            isPerm = False
            break

    if isPerm is False:
        return 0
    else:
        return 1

print(solution([1, 2, 3, 4]))
