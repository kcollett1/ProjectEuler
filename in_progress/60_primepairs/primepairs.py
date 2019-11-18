#!/bin/usr/env python

import itertools as itt
from itertools import combinations as comb

fo = open("primes.txt","w")
fo.write('2\n')
fo.write('3\n')

for i in range(5, 9999999, 2):
    prime = 1
    for j in range(3, int(i ** 0.5), 2):
        if not i % j: prime = 0; break
    if prime: fo.write(str(i)+'\n')

fo.close()
#321 primes from 1-2000

'''
for c in comb(primes, 5):
    for i in comb(c, 2):
        chprimefor = "".join(map(str, i))
        chprimebac = "".join(map(str, i[::-1]))

        if chprimefor not in notprimes and chprimefor not in primes:isprime(chprimefor)
        print(chprimefor, chprimebac)
'''
