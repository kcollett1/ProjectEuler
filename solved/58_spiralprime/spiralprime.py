ratio  = 1.
i      = 1
primes = 0
total  = 1

def isprime(n):
    if n == 2 or n == 3: return 1
    if n % 2 == 0 or n < 2: return 0
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0: return 0
    return 1

while ratio >= 0.1:
    i     += 2
    total += 4
    j      = (i - 2) ** 2

    for k in range(3):
        j += (i - 1)
        if isprime(j): primes += 1

    ratio = primes / total

print('answer:', i)
