def solution(number):
    factors = 0
    for i in range(1, (number//2) + 1):
        if number % i == 0:
            factors += 1

    factors += 1
    return factors

print(solution(24))
