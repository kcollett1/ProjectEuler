#!/bin/usr/env python

def run():
	stop = 2500
	pentnums = [int(0.5*i*(3*i-1)) for i in range(1,stop)]
	diff = []

	for j in range(stop-1):
		for k in range(j+1,stop-1):
			if pentnums[j]+pentnums[k] in pentnums[k+1:] and pentnums[k]-pentnums[j] in pentnums[:k]:
				return pentnums[k]-pentnums[j]
print run()
