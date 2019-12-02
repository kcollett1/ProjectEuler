
maxratio = 0
maxn     = 0
n_max    = 10000


def gcd(a,b):
    #if b > a: a,b = b,a #will always pass a > b in this code, so not necessary to check
    if b == 0: return a
    return gcd(b, a % b)


for n in range(2, n_max + 1):
    relprime = 1

    for i in range(2, n):
        if gcd(n, i) == 1:
            relprime += 1

    ratio = n / relprime

    if ratio > maxratio:
        maxratio = ratio
        maxn     = n


print('the value of n < ', n_max, ' which has max totient ratio is ', maxn)
