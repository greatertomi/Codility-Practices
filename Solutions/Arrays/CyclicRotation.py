def solution(array, num):
    array_length = len(array)
    temp_array = None
    for m in range(num):
        temp_array = []
        for n in range(array_length):
            if n == array_length - 1:
                temp_array.insert(0, array[n])
            else:
                temp_array.insert(n + 1, array[n])
        array = temp_array
    return temp_array

print(solution([3, 8, 9, 7, 6], 3))
