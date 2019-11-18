def isprime(i):
    if i == 2 or i == 3: return True
    if i%2 == 0 or i < 2: return False
    for j in range(3,int(i**0.5)+1,2):
        if i%j==0: return False    
    return True

def primefactor(n):
    factors[(n-1)%4] = []
    if isprime(n): factors[(n-1)%4].append(n); return
    def recur(i1,i2):
        if isprime(i1): factors[(n-1)%4].append(i1)
        else:
            j = 2
            while i1%j != 0: j += 1
            recur(j,i1/j)
        if isprime(i2): factors[(n-1)%4].append(i2)
        else:
            j = 2
            while i2%j != 0: j += 1
            recur(j,i2/j)
    i = 2
    while n%i != 0: i += 1
    recur(i,n/i)
    factors[(n-1)%4] = list(set(factors[(n-1)%4]))

n = 646
factors = [[],[],[],[]]

while len(factors[0]) != 4 or len(factors[1]) != 4 or len(factors[2]) != 4 or len(factors[3]) != 4:
    n += 1
    primefactor(n)

print n-3
