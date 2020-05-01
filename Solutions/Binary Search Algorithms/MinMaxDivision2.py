def check(a, k, max_block_sum):
    block_sum = 0
    count = 0

    for elem in a:
        if block_sum + elem > max_block_sum:
            block_sum = elem
            count += 1
        else:
            block_sum += elem

        if count >= k:
            return False

    return True

def solution(k, m, a):
    lower_bound = max(a)
    upper_bound = sum(a)

    if k == 1:
        return upper_bound

    if k >= len(a):
        return lower_bound

    while lower_bound <= upper_bound:
        possible_candidate = (lower_bound + upper_bound) // 2
        if check(a, k, possible_candidate):
            upper_bound = possible_candidate - 1
        else:
            lower_bound = possible_candidate + 1
    return lower_bound

# testcase 1
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
print(solution(K, M, A))

# # testcase 2
# K = 2
# M = 5
# A = [5, 3]
# print(solution(K, M, A))
#
# # testcase 3
# K = 3
# M = 5
# A = [5, 3]
# print(solution(K, M, A))
#
# # testcase 4
# K = 2
# M = 7
# A = [4, 1, 2, 7]
# print(solution(K, M, A))
