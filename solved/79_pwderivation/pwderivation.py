#!/usr/bin/env python

p_vals = []

with open('p079_keylog.txt') as f: pwds = f.readlines()

for v in pwds:
    for i in v.strip():
        if i not in p_vals: p_vals.append(i)

print(p_vals)

# i solved this one by pen and paper ...  is there a way to code it?
