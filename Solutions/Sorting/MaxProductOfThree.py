def solution(array):
    new_array = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                new_array.append(array[i] * array[j] * array[k])

    return max(new_array)

print(solution([-3, 1, 2, -2, 5, 6]))
