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
    # letter_dict = {}
    # array_length = len(array)
    # dominatorCheck = False
    # dominatorIndex = []
    # dominatorValue = 0
    #
    # for i in array:
    #     if i in letter_dict:
    #         letter_dict[i] += 1
    #     else:
    #         letter_dict[i] = 1
    #
    # for key in letter_dict:
    #     if letter_dict[key] > array_length//2:
    #         dominatorCheck = True
    #         dominatorValue = key
    #         break
    #
    # if dominatorCheck is True:
    #     for i in range(len(array)):
    #         if array[i] == dominatorValue:
    #             return i
    # else:
    #     return -1


# print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))
