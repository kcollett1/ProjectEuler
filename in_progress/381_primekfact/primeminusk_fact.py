#!/usr/bin/env python

lim = 10
fac = [1, 1, 2, 6, 24]
ans = 0

def isprime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return 0
    return 1

for p in range(5, lim, 2):
    if (p - 1) % 10 ** 7 == 0: print(p, ans)
    if isprime(p):
        a   = [i % p for i in fac]
        ctr = 0
        for i in a: ctr = (ctr + i) % p
        ans += ctr
        print(ans,ctr)

    a   = fac[-1] * p
    b   = a * (p + 1)
    fac = fac[2:] + [a, b]

print('answer:', ans)
