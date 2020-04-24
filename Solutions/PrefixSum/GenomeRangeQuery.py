def solution(string, p, q):
    string_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    return_arr = []

    for i in range(len(p)):
        new_string = str(string[p[i]:q[i]+1]).upper()
        string_val = [string_dict[x] for x in new_string]
        return_arr.append(min(string_val))

    return return_arr

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
