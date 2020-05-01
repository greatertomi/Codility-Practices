def solution(array):
    array_perm = []
    count_triangles = 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                array_perm.append((array[i], array[j], array[k]))

    for val in array_perm:
        if (val[0] + val[1] > val[2]) and (val[1] + val[2] > val[0]) and (val[0] + val[2] > val[1]):
            count_triangles += 1

    return count_triangles

print(solution([10, 2, 5, 1, 8, 12]))
