def solution(array: list):
    array.append(1)
    N = len(array)

    fib_table = [0]*27
    fib_table[1] = 1
    index = None

    for index in range(2, 27):
        fib_table[index] = fib_table[index-1] + fib_table[index-2]
        if fib_table[index] > N:
            break

    fib_table = fib_table[2:index]

    next_try = [-1]*N
    for index in range(len(fib_table)):
        next_try[fib_table[index] - 1] = 1

    for index, leaf in enumerate(array):
        if next_try[index] > 0 and leaf == 1:
            for fib in fib_table:
                if index + fib >= N:
                    break
                if next_try[index+fib] < 0 or next_try[index+fib] > next_try[index] + 1:
                    next_try[index+fib] = next_try[index]+1
    return next_try[-1]

A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))
