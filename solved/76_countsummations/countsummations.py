# brute force; takes a long time

total = 100
nums  = [i for i in range(1, total)]
poss  = 0

def countsums(tot, i, a):
    global poss

    if i < 0: return

    for numdigs in range(tot // nums[i], -1, -1):
        a2    = a
        a2[i] = numdigs
        tot2  = tot - (numdigs * nums[i])

        if tot2 > 0: countsums(tot2, i - 1, a2)
        elif tot2 == 0: poss += 1

    return

countsums(total, total - 2, [0 for i in range(total - 1)])

print('answer:', poss)
