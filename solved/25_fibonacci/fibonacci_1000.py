#!/usr/bin/env python

digits = 1000
fibprev = 1
fib = 1
i = 2

while fib < 10 ** (digits - 1):
    fibtemp = fib
    fib += fibprev
    fibprev = fibtemp
    i += 1
    # at this point in loop the i-th index fib term is: fib

print("answer: ",i)
