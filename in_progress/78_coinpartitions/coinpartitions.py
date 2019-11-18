import sys

n    = int(sys.argv[1])
poss = 0
nums = [i for i in range(1, n + 1)]

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

countsums(n, n - 1, [0] * n)


print(poss)

#print(poss % 7) # test - result is n=5
#print(poss % 1000000)
