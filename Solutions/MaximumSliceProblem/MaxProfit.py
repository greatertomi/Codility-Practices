def solution(array):
    profits = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            profits.append(-(array[i] - array[j]))

    return max(profits)

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
