def solution(arrayA, arrayB):
    stack, alive = [], len(arrayA)
    for fish in zip(arrayA, arrayB):
        size, up = fish
        if not up:
            while stack and stack[-1] < size:
                alive -= 1
                stack.pop()

            if stack:
                alive -= 1
        else:
            stack.append(size)
    return alive

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))
