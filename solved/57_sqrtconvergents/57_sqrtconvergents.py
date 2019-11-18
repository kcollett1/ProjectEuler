n = 1
d = 2
r = 0

for i in range(2, 1001):
    t = n
    n = d
    d = 2 * d + t
    if len(str(n+d)) > len(str(d)): r += 1

print('answer:', r)
