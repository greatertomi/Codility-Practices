def solution(x, y, d):
    if y < x or d < 1:
        return 0

    count = 0
    while x <= y:
        x += d
        count += 1
        print(x)
    return count

print(solution(10, 85, 30))
