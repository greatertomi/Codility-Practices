def solution(num, arrayA, arrayB):
    ranges = list(zip(arrayA, arrayB))
    semis_list = []
    for i in range(len(ranges)):
        count = len(findSemiPrimes(ranges[i][0], ranges[i][1]))
        semis_list.append(count)

    return semis_list

def findSemiPrimes(num1, num2):
    prime_nums = []
    semi_primes = []
    for i in range(1, (num2//2) + 1):
        if isPrime(i):
            prime_nums.append(i)

    for m in prime_nums:
        for n in prime_nums:
            prod = m*n
            if prod not in semi_primes and (num1 <= prod <= num2):
                semi_primes.append(prod)

    semi_primes.sort()
    return semi_primes

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    primeStatus = True
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            primeStatus = False
            break
    return primeStatus

print(solution(26, [1, 4, 16], [26, 10, 20]))
# print(findSemiPrimes(4, 10))
