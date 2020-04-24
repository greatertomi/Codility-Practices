def solution(string):
    if len(string) == 0:
        return 1
    elif string is None:
        return 0

    matches, stack = dict(['()', '[]', '{}']), []
    print(matches)
    for char in string:
        if char in matches.values():
            if stack and matches[stack[-1]] == char:
                stack.pop()
            else:
                return 0
        else:
            stack.append(char)
        print(stack)

    return int(not stack)


S = "[()()]"
print(solution(S))
