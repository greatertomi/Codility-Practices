def solution(arr):
    new_arr = set([abs(x) for x in arr])
    return len(new_arr)

print(solution([-5, -3, 1, 0, 3, 6]))
