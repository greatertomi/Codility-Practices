def solution(array1, array2):
    if len(array1) < 1:
        return 0

    count = 1
    prev_end = array2[0]

    for index in range(1, len(array1)):
        if array1[index] > prev_end:
            count += 1
            prev_end = array2[index]

    return count

A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
solution(A, B)
