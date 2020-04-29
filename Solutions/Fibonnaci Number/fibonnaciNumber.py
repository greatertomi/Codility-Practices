# Fibonacci number dynamic programming style
def fib(num):
    store = [None] * (num+1)
    return fib_engine(num, store)

def fib_engine(num, store):
    if store[num] is not None:
        return store[num]
    if num < 0:
        return 0
    if num == 1 or num == 2:
        return 1

    total = fib_engine(num-1, store) + fib_engine(num-2, store)
    store[num] = total
    return total