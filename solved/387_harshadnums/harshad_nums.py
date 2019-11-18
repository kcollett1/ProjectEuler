#!/usr/bin/env python

rt_harsh  = [[i for i in range(1, 10)]]
srt_harsh = []
dig_limit = 14 # find the number of strong, right-truncatable harshad primes less than 10^(dig_limit)
srt_hp    = []

def isprime(n):
    if n == 2: return 1
    if n < 2 or n % 2 == 0: return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return 0
    return 1

for digits in range(dig_limit - 2):
    rt_harsh.append([])
    for i in rt_harsh[digits]:
        sumdigits = sum([int(j) for j in str(i)])
        for j in range(10):
            testnum = int(str(i) + str(j))
            if testnum % sumdigits == 0:
                rt_harsh[digits + 1].append(testnum)
                if isprime(testnum / sumdigits): srt_harsh.append(testnum)
            sumdigits += 1

for n in srt_harsh:
    for j in range(1, 10, 2):
        testnum = int(str(n) + str(j))
        if isprime(testnum): srt_hp.append(testnum)

print('answer:', sum(srt_hp))
