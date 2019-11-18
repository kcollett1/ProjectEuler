#!/usr/bin/env python

def isprime(n): # for n > 3
    for i in range(3, int(n ** 0.5 // 1) + 1, 2):
        if n % i == 0: return 0
    return 1

primes = [2,3]
for i in range(5, 100001, 2):
    if isprime(i): primes.append(i)
primes = primes[::-1]

'''
def smoothcheck(n, sqrtn):
    i = 0
    global primes
    while n > 1:
        if primes[i] >= sqrtn: return 0
        if n % i == 0: n /= i
        else: i += 1
    return 1
'''

sqrt_smooth = 1
for i in range(4, 10000000001):
    if i in primes: continue
    sqrti = i ** 0.5
    for j in primes:
        if j >= i: continue
        if j < sqrti:
            sqrt_smooth += 1; break
        if i % j == 0: break

print('answer:', sqrt_smooth)
