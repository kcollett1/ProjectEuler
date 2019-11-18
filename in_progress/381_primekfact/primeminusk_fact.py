#!/usr/bin/env python

upper_limit  = 10 ** 2
fact_tracker = 1
sum_S_p      = 4
primes       = [2, 3, 5]

def isprime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return 0
    return 1

for p in range(7, upper_limit, 2):
    fact_tracker *= (p - 6) * (p - 5)
    if (p - 1) % 10**6 == 0: print(p)
    if isprime(p):
        primes.append(p)
        #sum_S_p += (fact_tracker * (p**4 - 9*p**3 + 27*p**2 - 30*p + 9)) % p

print('answer:', sum_S_p)
