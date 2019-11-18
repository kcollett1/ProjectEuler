#!/usr/bin/env python

max_r = 0
max_n = 0
upper = 1000001
facts = {}

##FIXME here, if i is a factor of n, than all of i's factors are also factors of n, should utilize this fact to make it more efficient

for i in range(2, upper):
    facts[i] = [i]
    j = 2
    while j <= i / j:
        if i % j == 0:
            facts[i] += [j, int(i / j)]
        j += 1
    facts[i] = list(set(facts[i]))

for n in range(2, upper):
    if n % 100000 == 0: print(n)
    relprimes = [1]

    for i in range(2, n):
        a = facts[n] + facts[i]
        if len(a) == len(set(a)):
            relprimes.append(i)

    p = len(relprimes)
    r = n / p

    if r > max_r:
        max_r = r
        max_n = n

print('answer:', max_n)
print('(n / phi(n) =', max_r, ')')

''' # takes too long
def totient(n):
    if n < 2: return 0 # not a valid n
    ctr = 1
    for i in range(2, n):
        if math.gcd(n,i) == 1: ctr += 1
    return ctr

for i in range(2,100001):
    if i % 10000 == 0: print(i)
    ratio = i / totient(i)
    if ratio > max_ratio: max_ratio, max_n = ratio, i
'''
