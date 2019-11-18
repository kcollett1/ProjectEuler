#!/usr/bin/env python

import math

distinct = []
sqfree   = [1]
primesq  = [4, 9]
pascal   = [[1]]

for i in range(50):
    a = [pascal[i][j] + pascal[i][j + 1] for j in range(i)]
    pascal.append([1] + a + [1])
    for j in a:
        if j not in distinct: distinct.append(j)

def isprime(n):
    for j in range(3, int(math.sqrt(n) // 1) + 1, 2):
        if n % j == 0: return 0
    return 1

for i in range(5, int(math.sqrt(distinct[-1] // 1)) + 1, 2):
    if isprime(i): primesq.append(i * i)

for n in distinct:
    i = 0
    sqf_check = 1
    while i < len(primesq) and primesq[i] <= n:
        if n % primesq[i] == 0: sqf_check = 0; break
        i += 1
    if sqf_check: sqfree.append(n)

print('ans:', sum(sqfree))
