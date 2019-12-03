
maxnum = 10 ** 6

n_dict = {}
for i in range(2, maxnum + 1):
    n_dict[i] = [1]

#stuff here to fill arrays with relative prime numbers
for i in range(2, maxnum):
    for j in n_dict[i]:
        for k in range(i + j, maxnum + 1, i):
            n_dict[k].append(i)

maxn     = 2
maxratio = 2

for n in n_dict:
    ratio = n / len(n_dict[n])
    if ratio > maxratio:
        maxratio = ratio
        maxn = n

print('answer:', maxn, '( maxratio = ', maxratio,')')

