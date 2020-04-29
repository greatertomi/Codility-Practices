# Didn't fully under the question, so I decided to solve this.

# There are n stairs, a person standing at the bottom wants to reach the top.
# The person can climb either 1 stair or 2 stairs at a time.
# Count the number of ways, the person can reach the top.

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

def count_stairs(n):
    return fib(n + 1)
