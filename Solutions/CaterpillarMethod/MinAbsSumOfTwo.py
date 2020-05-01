def solution(array):
    array_perm = []
    solved = []
    for i in range(len(array)):
        for j in range(len(array)):
            array_perm.append((array[i], array[j]))

    for val in array_perm:
        solved.append(abs(val[0] + val[1]))
    return min(solved)

nums = [1, 4, -3]
nums2 = [-8, 4, 5, -10, 3]
print(solution(nums2))
