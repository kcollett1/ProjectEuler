
def countdig(num):
	dig = 0
	while num > 0: dig += 1; num = int(num/10)
	return dig

power = 2; ans = 9

while True:
	if countdig(9**power) != power: break
	itr = 8; ans += 1
	while countdig(itr**power) == power: itr -= 1; ans += 1
	power += 1
print ans
