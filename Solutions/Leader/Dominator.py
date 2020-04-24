from collections import Counter

def solution(array):
    if len(array) == 0:
        return -1

    dominator, dominator_count = Counter(array).most_common()[0]
    dominatorIndex = []

    if dominator_count <= len(array) // 2:
        return -1

    for idx, value in enumerate(array):
        if value == dominator:
            dominatorIndex.append(idx)
    return dominatorIndex


A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))
