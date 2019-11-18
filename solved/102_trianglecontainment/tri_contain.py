with open('tri.txt') as f: lines = f.readlines()

origin = 0

for tri in lines:
    tri = tri.strip().split(',')
    for i,c in enumerate(tri): tri[i] = int(c)
    x, y = tri[::2], tri[1::2]
    b, a = [], []

    for i in range(3):
        if x[i] == 0:
            if y[i] == 0: origin += 1; continue
            for j in range(i + 1, 3):
                if x[j] == 0: origin += 1; continue
            continue
        elif x[i] < 0: b.append([x[i], y[i]])
        else: a.append([x[i], y[i]])

    if len(a) == 3 or len(a) == 0: continue
    if len(a) == 2: a,b = b,a

    x1, y1 = a[0][0], a[0][1]
    b1 = y1 - (x1 * (b[0][1] - y1) / (b[0][0] - x1))
    b2 = y1 - (x1 * (b[1][1] - y1) / (b[1][0] - x1))
    if b1 * b2 <= 0: origin += 1 # one is below axis, one is above (or on the origin)

print('answer:', origin)
