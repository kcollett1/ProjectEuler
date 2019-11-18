import math

max_x = 0
max_D = 0

for D in range(1001):
    if math.sqrt(D) % 1 == 0: continue
    x = 2
    #x = 100000
    while 1:
        if math.sqrt((x**2 - 1) / D) % 1 == 0:
            if x > max_x:
                max_x = x
                max_D = D
            break
        x += 1
        if x == 200000: print('x reached 200000 for d = ',D); break
    #print('D = ', D, ' ... x = ', x)

print('max x found: ',max_x,' ... max D found: ', max_D)
