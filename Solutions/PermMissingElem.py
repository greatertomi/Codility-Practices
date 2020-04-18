def solution(array):
    array.sort()
    missing_num = 0
    for i in range(len(array)):
        if i + 1 != array[i]:
            missing_num = i + 1
            break
    return missing_num

arr = [4]
print(solution(arr))
