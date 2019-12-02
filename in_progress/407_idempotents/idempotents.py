#!/usr/bin/env python

a2 = [i ** 2 for i in range(10 ** 7)]
a2modn = {}

for a,asq in enumerate(a2):
    for j in range(a):
        asq % j
