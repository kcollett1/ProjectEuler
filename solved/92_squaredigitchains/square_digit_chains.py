ans = 0

for i in range(10000000):
    chain = []
    n = i
    while n not in chain:
        if n == 89: ans += 1; break
        chain.append(n)
        r = 0
        for j in str(n): r += int(j) ** 2
        n = r

print('answer:', ans)
