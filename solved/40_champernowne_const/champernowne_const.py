#!/bin/usr/env python

dig,pow10,ans,i = 25,100,1,18

while pow10 < 1000001:
	num = i
	while num > 0:
		num /= 10
		dig += 1
	if dig >= pow10:
		num = i; digcheck = dig
		while digcheck != pow10:
			digcheck -= 1
			num /= 10
		ans *= num%10
		pow10 *= 10
	i += 1

print ans
