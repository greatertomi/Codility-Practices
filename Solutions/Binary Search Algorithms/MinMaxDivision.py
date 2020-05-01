import itertools

def solution(k, m, a):
    buckets = refresh_bucket(k)
    array_sum = []

    for x in itertools.permutations(a):
        new_array = list(x)
        count = 0
        for i in new_array:
            buckets[count].append(i)
            if count + 1 == k:
                count = 0
            else:
                count += 1
        summer = sum(max(buckets, key=sum))
        array_sum.append(summer)
        buckets = refresh_bucket(k)

    return min(array_sum)


def refresh_bucket(k):
    buckets = []
    for i in range(k):
        buckets.append([])
    return buckets

# print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))
# testcase 1
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
print(solution(K, M, A))

# testcase 2
K = 2
M = 5
A = [5, 3]
print(solution(K, M, A))

# testcase 3
K = 3
M = 5
A = [5, 3]
print(solution(K, M, A))

# testcase 4
K = 2
M = 7
A = [4, 1, 2, 7]
print(solution(K, M, A))

