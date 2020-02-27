#!/bin/usr/env python

fo = open("primes.txt","w")
fo.write('2\n')
fo.write('3\n')

for i in range(5, 9999999, 2):
    prime = 1
    for j in range(3, int(i ** 0.5) + 1, 2):
        if not i % j: prime = 0; break
    if prime: fo.write(str(i)+'\n')

fo.close()
#322 primes from 1-2000
