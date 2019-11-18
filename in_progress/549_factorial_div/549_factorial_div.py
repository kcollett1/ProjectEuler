
import numpy as np

factarr = [0,1]
for i in range(2,10000):
	factarr.append(factarr[i-1]*i)

#print factarr[np.searchsorted(factarr,10**6,side="left")]

def sfunc(num):
	i = np.searchsorted(factarr,10**6,side="left")
	while factarr[i]%num != 0: i +=1
	return i

def Sfunc(num):
	return sum([sfunc(i) for i in range(2,num+1)])

print Sfunc(10**3)
#print Sfunc(10**8)
#print sfunc(10),sfunc(25)

