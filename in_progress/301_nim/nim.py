#!/usr/bin/env python

upper_limit = 100 # doesn't work for large numbers
ans         = 0

for n in range(1, upper_limit + 1):
    if n ^ (2 * n) ^ (3 * n) == 0: ans += 1

print('answer:', ans)
