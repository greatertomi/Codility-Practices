def convertToBinary(number: int):
    binary = ''
    while number > 0:
        binary += str(number % 2)
        number = number // 2
    binary = binary[::-1]
    return binary


def solution(num):
    if num <= 0:
        return 0
    binary = convertToBinary(num)
    print(binary)
    max_zero_count = 0
    temp_zero_count = 0
    for i in binary:
        if int(i) == 0:
            temp_zero_count += 1
        else:
            if temp_zero_count > max_zero_count:
                max_zero_count = temp_zero_count
            temp_zero_count = 0
    return max_zero_count


print(solution(1041))
