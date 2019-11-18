#!/usr/bin/env python

maxnum 	= 1000
palsum 	= 0

def palindrome(num):
	digits = []
	while(num > 0):
		digits.append(num%10)
		num = num / 10
	numdig = len(digits)
	if numdig == 1:
		return False
	for itr in range(0,numdig/2):
		if digits[itr] != digits[numdig - itr - 1]:
			return False
	return True

for itr in range(11,maxnum):
	if palindrome(itr) and : #FIXME stopped here , need to check if it can be written as a sum of consecutive square numbers
		palsum = palsum + itr

