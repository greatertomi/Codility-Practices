def solution(array):
    index = 0
    if len(array) % 2 != 1:
        return None

    while len(array) > 1:
        num = array[index]
        if num in array:
            array.remove(num)
            array.remove(num)
        else:
            index += 1
    return array[0]

arr = [9, 3, 9, 3, 9, 7, 9]
print(solution(arr))
