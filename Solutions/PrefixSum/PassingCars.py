def solution(array):
    if len(array) < 1:
        return None

    count_cars = 0
    for i in range(len(array)):
        if array[i] == 0:
            for j in range(i, len(array)):
                if array[j] == 1:
                    count_cars += 1
    return count_cars

print(solution([0, 1, 0, 1, 1]))
