import itertools as it

def isprime(i):
    if i == 2 or i == 3: return True
    if i%2 == 0 or i < 2: return False
    for j in range(3,int(i**0.5)+1,2):
        if i%j==0: return False    
    return True

for c in it.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9],4):
    if len([j for j in c if j==0]) > 1 or max(c) - min(c) < 7: continue
    if (1,4,7,8) == c: continue

    primes = []
    for n in it.permutations(c,4):
        if n[0] == 0 or int(''.join(map(str,n))) in primes: continue
        if isprime(int(''.join(map(str,n)))): primes.append(int(''.join(map(str,n))))
    if len(primes) < 3: continue
    primes = sorted(primes)

    for i in range(len(primes)-2):
        for j in range(i+1,len(primes)-1):
            diff = primes[j] - primes[i]
            for k in range(j+1,len(primes)):
                if primes[k] - primes[j] == diff:
                    print ''.join([str(primes[i]),str(primes[j]),str(primes[k])])
                    exit(1)
