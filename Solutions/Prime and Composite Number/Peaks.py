def solution(array: list):
    array_len = len(array)

    if array_len < 3:
        return 0

    peaks = []

    for index in range(1, array_len - 1):
        if array[index - 1] < array[index] > array[index + 1]:
            peaks.append(index)

    check = None
    print('peaks', peaks)
    for size in range(len(peaks), 0, -1):
        if array_len % size == 0:
            block_len = array_len // size
            check = [0]*size
            for elem in peaks:
                ptr = elem // block_len
                if check[ptr] == 0:
                    check[ptr] = 1

        if check.count(1) == size:
            return size

    return 0

solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
