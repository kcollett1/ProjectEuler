def isprime(i):
    if i == 2 or i == 3: return True
    if i%2 == 0 or i < 2: return False
    for j in range(3,int(i**0.5)+1,2):
        if i%j == 0: return False
    return True

c = 3
n = 10**6
primes = [2]

while c < n:
    if c + primes[-1] >= n: break
    if isprime(c): primes.append(c)
    c += 1

l = len(primes) - 1
j = 0
s = [sum(primes)]

while l > 0:
    #if l % 1000 == 0: print l # just to track progress
    for a,b in enumerate(s):
# check s for any sums are less than n AND prime
        if b < n and isprime(b):
            print b; exit(1)
# if not construct next sum list appending last element in special way
    s.append(s[-1] - primes[j])
    for a in range(len(s) - 1):
        s[a] -= primes[l + a]
    l -= 1
    j += 1
