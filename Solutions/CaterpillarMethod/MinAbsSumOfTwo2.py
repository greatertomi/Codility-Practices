def solution(array):
    diff = int(20E8)
    beg = 0
    end = len(array) - 1
    array.sort()

    while beg <= end:
        diff = min(diff, abs(array[beg] + array[end]))
        if abs(array[beg]) > abs(array[end]):
            beg += 1
        else:
            end -= 1

    return diff

# testcase 1
A = [1, 4, -3]
print(solution(A))

# # testcase 2
# A = [-8, 4, 5, -10, 3]
# print(solution(A))
#
# # testcase ３
# A = [0]
# print(solution(A))
