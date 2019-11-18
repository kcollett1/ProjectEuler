#!/usr/bin/env python

import itertools

runsum = 0

for a in list(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)):
	if a[3]%2==0 and (a[2]*100+a[3]*10+a[4])%3==0 and a[5]==5 and (a[4]*100+a[5]*10+a[6])%7==0 and (a[5]*100+a[6]*10+a[7])%11==0 and (a[6]*100+a[7]*10+a[8])%13==0 and (a[7]*100+a[8]*10+a[9])%17==0:
		runsum += a[0]*1000000000+a[1]*100000000+a[2]*10000000+a[3]*1000000+a[4]*100000+a[5]*10000+a[6]*1000+a[7]*100+a[8]*10+a[9]
print 'ans=',runsum
