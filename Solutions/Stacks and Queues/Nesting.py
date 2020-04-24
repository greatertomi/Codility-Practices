def solution(string):
    if len(string) == 0:
        return 1

    paren = 0
    for char in string:
        print(paren)
        if char == '(':
            paren += 1
        else:
            paren -= 1
            if paren < 0:
                return 0

    print('end', paren)
    if paren == 0:
        return 1
    else:
        return 0

print(solution(')))((('))
