import numpy

ps_nums = []

for k in range(2,13):
#for k in range(2,12001):
    foundset = 0
    checkset = [1] * (k - 2) + [2, 2]
    #print(checkset, sum(checkset), numpy.prod(checkset))
    #while not foundset:
        #
    N = sum(checkset)
    if N not in ps_nums: ps_nums.append(N)

print('ans:', sum(ps_nums))
