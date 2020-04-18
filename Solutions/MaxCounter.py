# def solution(operations, counter_num):
#     counters = [0 for _ in range(5)]
#     for i in operations:
#         if i == counter_num + 1:
#             max_num = max(counters)
#             counters = [max_num for _ in counters]
#         elif i <= counter_num:
#             counters[i-1] += 1
#         else:
#             pass
#     return counters

def solution(counter_num, operations):
    counters = [0 for _ in range(counter_num)]
    for i in operations:
        if i == counter_num + 1:
            max_num = max(counters)
            counters = [max_num for _ in counters]
        elif i <= counter_num:
            counters[i-1] += 1
        else:
            pass
    return counters

print(solution(1, [3, 4, 4, 6, 1, 4, 4]))

