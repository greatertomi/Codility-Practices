def solution(number):
    seen_values = []
    min_perimeter = 0

    for i in range(1, (number//2) + 1):
        if number % i == 0 and i not in seen_values:
            second = number // i
            perimeter = 2 * (i + second)

            if min_perimeter == 0:
                min_perimeter = perimeter
            else:
                if perimeter < min_perimeter:
                    min_perimeter = perimeter

            seen_values.extend([i, second])

    return min_perimeter

print(solution(30))
