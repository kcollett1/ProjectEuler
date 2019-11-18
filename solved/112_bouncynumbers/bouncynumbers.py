# this code is brute force, not optimized, but gives correct answer in a few seconds

b = 0
r = 0
i = 1

def bouncy(n):
    n = str(n)
    if len(n) == 1: return 0

    inc, dec = 1,1
    prev = n[0]
    for i in n[1:]:
        if not inc and not dec: return 1
        if int(i) < int(prev): inc = 0
        elif int(i) > int(prev): dec = 0
        prev = i

    if not inc and not dec: return 1
    return 0

while r != 0.99:
    if bouncy(i): b += 1
    r = b / i
    i += 1

print('answer:', i - 1)
