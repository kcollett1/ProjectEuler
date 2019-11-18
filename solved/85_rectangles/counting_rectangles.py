
min_diff = 2000000
min_area = 0

# range up to 1000 is overkill, but still gives correct answer pretty quickly
for i in range(2, 1000):
    possl = 0
    measl = [i, 0]
    for j in range(2, 1000): # quicker to go from 2..1000 (and double count some rectangles possibly, because it is quicker to calculate these smaller dimensions and break the loop earlier on
# this is an i x j rectangle to check posibilities for now, with these two loops
        poss  = 0
        for m in range(i):
            extra_m = i - m
            for n in range(j):
                poss += extra_m * (j - n)

        if poss < 2000000:
            possl = poss
            measl[1] = j
        else:
            diffg = poss - 2000000
            diffl = 2000000 - possl

            if diffg < diffl:
                diff  = diffg
                li,lj = i,j
            else:
                diff  = diffl
                li,lj = measl

            if diff < min_diff:
                min_diff = diff
                min_area = li * lj

            break

print('answer:', min_area)
