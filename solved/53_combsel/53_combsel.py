def nCr(n,r):
    c = 1
    for i in range(n,max(r,n-r),-1):
        c *= i
    for i in range(2,min(r,n-r) + 1):
        c /= i
    return c

ans = 0

for i in range(100,0,-1):
    for j in range(i,0,-1):
        if nCr(i,j) > 10**6: ans += 1
print ans
