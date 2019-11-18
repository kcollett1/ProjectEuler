#!/usr/bin/env python

upper = 1000001
ans_n = 2
ans_d = 5
facts = {1:[]}

for n in range(2, 9):
    facts[n] = [n]
    i = 2
    while i <= n / i:
        if n % i == 0:
            facts[n] += [i, int(n / i)]
        i += 1
    facts[n] = list(set(facts[n]))

for n in range(9, upper):
## FIXME here, if i is a factor of n,
## than all of i's factors are also factors of n,
## can we utilize this fact to make it more efficient
    facts[n] = [n]
    i = 2
    while i <= n / i:
        if n % i == 0:
            facts[n] += [i, int(n / i)]
        i += 1
    facts[n] = list(set(facts[n]))

    i = n * 3 // 7
    j = (n * ans_n // ans_d) + 1
    while i >= j:
        a = facts[n] + facts[i]
        if len(a) == len(set(a)):
            ans_n = i
            ans_d = n
        i -= 1

print('answer:', ans_n)
