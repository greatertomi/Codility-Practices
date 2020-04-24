def solution(array):
    new_array = []
    check = False

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                new_array.append([array[i], array[j], array[k]])

    for triple in new_array:
        if (triple[0] + triple[1] > triple[2]) and (triple[0] + triple[2] > triple[1]) and (triple[1] + triple[2] > triple[0]):
            check = True
            break

    if check:
        return 1
    else:
        return 0

print(solution([10, 2, 5, 1, 8, 20]))
