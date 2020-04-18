def solution(array):
    if len(array) < 2:
        return None
    diff_list = []
    for i in range(len(array) - 1):
        sum1 = sum(array[:i+1])
        sum2 = sum(array[i+1:])
        diff_list.append(abs(sum1 - sum2))
    return min(diff_list)

arr = [3, 1, 5, 6]
print(solution(arr))

