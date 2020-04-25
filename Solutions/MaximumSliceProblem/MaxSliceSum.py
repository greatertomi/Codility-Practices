def solution(array):
    once_total = float("-inf")
    until_now = 0
    for i in array:
        until_now = max(i, until_now + i)
        once_total = max(once_total, until_now)

    return once_total

solution([0, 2, -6, 4, 0])
