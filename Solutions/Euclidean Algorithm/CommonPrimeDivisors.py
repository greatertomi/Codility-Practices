def solution(array1, array2):
    arrays = list(zip(array1, array2))
    countSame = 0
    for i in range(len(arrays)):
        primes1 = primeDivisorLister(arrays[i][0])
        primes2 = primeDivisorLister(arrays[i][1])
        if primes1 == primes2:
            countSame += 1

    return countSame

def primeDivisorLister(num):
    divisors = []
    for i in range(2, num+1):
        if num % i == 0:
            if isPrime(i):
                divisors.append(i)
    return divisors

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

print(solution([15, 10, 3], [75, 30, 5]))
