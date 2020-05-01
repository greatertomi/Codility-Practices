def solution(array):
    N = len(array)
    count = 0

    array.sort()
    for x in range(N):
        z = x + 2
        for y in range(x + 1, N):
            while z < N and array[x] + array[y] > array[z]:
                z += 1
            count += z - y - 1

    return count

A = [10, 2, 5, 1, 8, 12]
print(solution(A))
