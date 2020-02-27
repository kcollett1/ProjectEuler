digsums = [i for i in range(10)]
sn      = [0]
fib     = [0, 1]
ans     = 0

def sumdigits(n):
    ans = 0
    for dig in str(n): ans += int(dig)
    return ans

def s(n):
    for i,sums in enumerate(digsums):
        if sums == n: return i

    i = len(digsums)
    digsums.append(sumdigits(i))

    while digsums[-1] != n:
        i += 1
        digsums.append(sumdigits(i))

    return i

def S(k):
    ans = 0
    for i in range(1, min(len(sn), k + 1)): ans += sn[i]

    for i in range(len(sn), k + 1):
        si = s(i)
        sn.append(si)
        ans += si

    return ans

for i in range(2, 91):
    fib.append((fib[i - 2] + fib[i - 1]) % 1000000007)
    ans = (ans + S(fib[-1])) % 1000000007

print('ans:', ans)
