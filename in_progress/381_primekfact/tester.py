#!/usr/bin/env python

with open("listofprimes_lt10_8.txt", "r") as f: primes = f.readlines()

primes = [int(p) for p in primes[:100]]
# temporary, testing smaller set of primes first, remove for final version

mod_arr = [[]] * len(primes)
ctr_mapper = {}
for i,j in enumerate(primes): ctr_mapper[j] = i

for i in range(7, primes[-1] + 1, 2):
    iip1 = i * (i + 1)
    for j in primes[::-1]:
        if j <= i: break
        mod_arr[ctr_mapper[j]].append(iip1 % j)

for i,j in enumerate(mod_arr):
    print(i,j, primes[i], len(j))
    print(' ')

'''
ans = 8

#for p in primes[4:25]: # should give ans = 480
for p in primes[4:]:
    p = int(p)
    m = 270
    for i in range(7, p - 1): m = (-m * i) % p
    ans += m


print('answer:', ans)
'''
