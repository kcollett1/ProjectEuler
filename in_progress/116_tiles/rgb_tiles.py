r_len   = 2
g_len   = 3
b_len   = 4
tot_len = 50
ans     = 0
sums    = [1]

for i in range(2, 51): sums.append(sums[i - 2] + i)

# counting red
for i in range(1, tot_len // b_len + 1):
    # calulcate tot_len - (r_len * i) + 1 ###FIXME here
    ans += tot_len - r_len + 1

# counting green
for i in range(1, tot_len // b_len + 1):
    ans += tot_len - g_len + 1

# counting blue

for i in range(1, tot_len // b_len + 1):
    ans += tot_len - b_len + 1

print('answer:', ans)
