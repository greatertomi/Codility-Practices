def solution(array):
    divisor_list = []
    for i in array:
        divisor_count = 0
        for j in array:
            if i % j != 0:
                divisor_count += 1
        divisor_list.append(divisor_count)

    return divisor_list

print(solution([3, 1, 2, 3, 6]))
