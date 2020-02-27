#!/bin/usr/env python

from itertools import combinations as com

def isprime(n): # will never be even, always greater than 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

concat = lambda a,b: int(str(a) + str(b))

def find_primepair_set(set_len):
# 2 and 5 can not be part of any pairs
# any number > 10 ending in 2 or 5 are never prime
    pair_sets = {3:0, 7:[set([3]),set()]}
    min_sum   = 10**9
    min_group = []
    i         = 11

    def valid_pair(val1, val2):
        if val1 in pair_sets[val2][0]: return True
        elif val1 in pair_sets[val2][1]: return False
        else:
            v12   = concat(val1, val2)
            v21   = concat(val2, val1)
            v12_p = isprime(v12)
            v21_p = isprime(v21)
            if v12 < min_sum and v12_p: pair_sets[v12] = 0
            if v21 < min_sum and v21_p: pair_sets[v21] = 0
            if not v12_p or not v21_p:
                pair_sets[val2][1].add(val1)
                return False
            else:
                pair_sets[val2][0].add(val1)
                return True

    def valid_group(n, remaining, ind, choices, currgroup):
        if remaining == 0: return [True, currgroup + [n]]

        valid  = [False, []]
        maxind = len(choices) - remaining
        while not valid[0] and ind <= maxind:
            # check if choices[ind] is valid addition to currgroup
            checkval = choices[ind]
            can_add = True
            for val in currgroup:
                if not valid_pair(val, checkval):
                    can_add = False
                    break
            # if not, do nothing, just keep checking rest of potential values to add
            if not can_add:
                ind += 1
                continue
            # if so: add val to currgroup, add check if rest of group can be made recursively
            valid = valid_group(n, remaining - 1, ind + 1, choices, currgroup + [checkval])
            ind += 1
        return valid

    while len(min_group) == 0 or min_sum > i:

        if str(i)[-1] == '5' or (i not in pair_sets and not isprime(i)):
            i += 2
            continue

        newpairs = {}
        newpairs[i] = [set(),set()]

        for j in pair_sets:
            if j >= i: continue
            ij   = concat(i,j)
            ji   = concat(j,i)
            ij_p = isprime(ij)
            ji_p = isprime(ji)
            if ij < min_sum and ij_p: newpairs[ij] = 0
            if ji < min_sum and ji_p: newpairs[ji] = 0
            if ij_p and ji_p: newpairs[i][0].add(j)
            else: newpairs[i][1].add(j)


        for p in newpairs: pair_sets[p] = newpairs[p]
        # if p already in pair_sets, should only be there as 0

        l = len(pair_sets[i][0])
        if l < set_len - 1:
            i += 2
            continue

        valid_check = valid_group(i, set_len - 1, 0, sorted(pair_sets[i][0]), [])

        if valid_check[0]:
            gsum = sum(valid_check[1])
            if gsum < min_sum:
                min_sum = gsum
                min_group = valid_check[1]

        i += 2

    print(min_sum, min_group)

find_primepair_set(5)
