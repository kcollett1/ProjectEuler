u = 1000
r = 2 * u - 3

for d in range(2, u + 1):
    for n in range(2, d - 1):
        hcf = 1
        for i in range(2, n + 1):
            if d % i == 0 and n % i == 0:
                hcf = i
                break
        if hcf == 1:
            #print(n,'/',d)
            r += 1

print('for u = ', u, '... r = ', r)
