#!/bin/usr/env python

file_o = open('primes.txt','r')
primes = file_o.readlines()
s,c,f  = [],[],[]
t,fo   = 0,0

for p in primes:
    p  = int(p.strip())
    p2 = p * p
    if p2 > 50000000: break
    s.append(p2)
    if t: continue
    p3 = p2 * p
    if p3 > 50000000:
        t = 1
        continue
    c.append(p3)
    if fo: continue
    p4 = p3 * p
    if p4 > 50000000:
        fo = 1
        continue
    f.append(p4)

file_o.close()

nums = []

for i in f:
    for j in c:
        a = i + j
        if a > 50000000: break
        for k in s:
            n = a + k
            if n > 50000000: break
            nums.append(n)

print('answer:', len(set(nums)))
