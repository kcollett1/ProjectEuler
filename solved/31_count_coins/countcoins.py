coins = [1,2,5,10,20,50,100,200]
poss  = 0

def calccoins(tot, i, a):
    global poss

    if i < 0: return

    for numcoins in range(tot // coins[i], -1, -1):
        a2      = a
        a2[i] = numcoins
        tot2    = tot - (numcoins * coins[i])

        if tot2 > 0: calccoins(tot2, i - 1, a2)
        elif tot2 == 0: poss += 1

    return

calccoins(200, 7, [0,0,0,0,0,0,0,0])
print('answer:',poss)
