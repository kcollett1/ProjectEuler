#!/bin/usr/env python

import math

per = [0 for i in range(1000)]

for l1 in range(1,500):
	for l2 in range(l1,500):
		if l1+l2+math.sqrt(l1*l1+l2*l2) > 1000: break
		if math.sqrt(l1*l1+l2*l2)%1. == 0:
			per[int(l1+l2+math.sqrt(l1*l1+l2*l2))-1] += 1

print 'ans =',per.index(max(per))+1
