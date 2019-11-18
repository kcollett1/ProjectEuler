
def isprime(num):
	if num <= 1 or num == 4: return False
	div = 2
	maxn = int(num / div)
	while div < maxn:
		maxn = num / div
		if num%div == 0:
			return False
		div += 1
	return True

for odd in range(9,10000,2):
	if not isprime(odd):
		flag = True
		for prime in range(odd-2,2,-2):
			if isprime(prime):
				num = 1
				while prime+2*num**2 < odd: num += 1
				if prime+2*num**2 == odd:
					flag = False; break
		if flag: print odd; break
