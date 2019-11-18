def sum_digs(i):
    r = 0
    for j in str(i): r += int(j)
    return r

ans = 0
for a in range(1,100):
    for b in range(1,100):
        ans = max(ans, sum_digs(a ** b))

print ans
