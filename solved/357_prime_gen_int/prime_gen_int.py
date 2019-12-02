
def isprime(i):
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0: return 0
    return 1


ans    = 1
primes = [0,0,1,1,0,1,0]
max_n  = 100000000

for p in range(7, max_n + 1, 2):
    primes.append(isprime(p))
    primes.append(0)

for n in range(2, max_n + 1, 2):
    if not primes[n + 1]: continue
    t_or_f = 1
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0 and not primes[div + int(n / div)]:
            t_or_f = 0
            break
    if t_or_f: ans += n

print('answer:', ans)
