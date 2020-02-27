p_n   = [1, 1]
max_n = 5

for n in range(2, max_n + 1):
    pn     = 1
    groups = 1
    while groups <= n - groups:
        pn     += p_n[groups] * p_n[n - groups] # FIXME this overcounts some non-distinct possibilities
        groups += 1
    p_n.append(pn)

print(p_n)
