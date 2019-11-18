import itertools
from itertools import product as pr

pete_poss  = pr('1234', repeat=9)
colin_poss = pr('123456', repeat=6)

pete_sums  = [0] * 28
colin_sums = [0] * 31
for i in pete_poss: pete_sums[sum([int(j) for j in list(i)]) - 9] += 1
for i in colin_poss: colin_sums[sum([int(j) for j in list(i)]) - 6] += 1

P_pete = 0
runsum = sum(colin_sums[:3])
for n in range(9, 37):
    P_pete += (pete_sums[n - 9] * runsum)
    runsum += colin_sums[n - 6]

'''
P_tie = 0
for n in range(9,37):
    P_tie += (pete_sums[n - 9] * colin_sums[n - 6])

P_colin = 0
runsum  = colin_sums[30]
for n in range(35, 8, -1):
    P_colin += (pete_sums[n - 9] * runsum)
    runsum  += colin_sums[n - 6]
'''

denom = 262144 * 46656
print('answer:', round(P_pete / denom, 7)) # prob of pete winning
'''
print('prob of tie:', round(P_tie / denom, 7))
print('prob of colin winning:', round(P_colin / denom, 7))
print('total prob (should be 1.0):', (P_colin + P_tie + P_pete) / denom)
'''
