def solution(array):
    array.sort()
    new_array = list(set(array))
    start = new_array[0]
    missing_num = None
    m = 0

    for i in range(start, start + len(new_array)):
        if i != new_array[m]:
            if i > 0:
                missing_num = i
                break
        m += 1

    if missing_num is None:
        max_num = max(new_array)
        max_num += 1
        while max_num <= 0:
            max_num += 1
        missing_num = max_num
    return missing_num

print(solution([-6, 8, 4006]))
