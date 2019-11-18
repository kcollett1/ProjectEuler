def isprime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 2: return False
    for i in range(3,int(n**0.5),2):
        if n%i == 0: return False
    return True

i = 56009

while i < 10**6: #i < 10**8:
    a = [0,0,0]
    for j in str(i):
        if j in '012': a[int(j)] += 1
    if sum(a) > 0 and isprime(i):
# has to be a number with digits either 0 1 or 2 (so that there are at least 8 primes in the family to check), then can check all possible HIGHER primes
# first replace all 0's (2 can be not prime), then all 1's (1 can be not prime), then all 2's (none can not be prime)
        for j in [0,1,2]:
            if a[j] > 0:
                np = j
                m = str(i).replace(str(j),'*')
                for q in range(j + 1, 10):
                    # replace all *'s in m with q, check if prime, if not prime increase np
                    if not isprime(int(m.replace('*',str(q)))): np += 1
                    if np > 2: break
                if np < 3:print i; exit(1)
    i += 1
