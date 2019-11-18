i = 1

while 1:
    r = 2 * i
    s = sorted([int(k) for k in str(i)])
    for j in range(5):
        # if r has same digits as i then continue, if not then break
        if s != sorted([int(k) for k in str(r)]): break
        if j == 4: print i; exit(1)
        r += i
    i += 1
