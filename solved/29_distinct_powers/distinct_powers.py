#!/usr/bin/env python

def foo():
	min_a = 2
	min_b = 2
	max_a = 100
	max_b = 100
	powers = []

	itr_a = min_a

	while itr_a <= max_a:
		tracker = itr_a
		itr_b = min_b

		while itr_b <= max_b:
			tracker = tracker * itr_a
			powers.append(tracker)
			itr_b = itr_b + 1

		itr_a = itr_a + 1
		
	print "answer: ",len(set(powers))
