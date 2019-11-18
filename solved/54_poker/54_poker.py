#!usr/bin/env python

p1 = 0
a  = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def straight(hand): # return yes or no, and if A is low or not
    b = sorted([a[j[0]] for j in hand])
    if b == [2,3,4,5,14]: return True,True
    c = b[0]
    for i in b[1:]:
        if i != c + 1: return False,False
        c = i
    return True,False

def fours(hand): # return yes or no, and number of card
    b = [a[j[0]] for j in hand]
    c = list(set(b))
    if len(c) == 2:
        for i in c:
            if b.count(i) == 4: return True,i
    return False,1

def threes(hand): # return yes or no, and number of card
    b = [a[j[0]] for j in hand]
    c = list(set(b))
    if len(c) == 3:
        for i in c:
            if b.count(i) == 3: return True,i
    return False,1

def pairs(hand): # return yes or no, array of card values of any pairs, and card value array excluding pairs
    p = False
    n = []
    hi = []
    b = [a[j[0]] for j in hand]
    c = list(set(b))
    if len(c) < 5:
        for i in c:
            if b.count(i) == 2:
                p = True
                n.append(i)
            else: hi.append(i)
    return p, sorted(n), sorted(hi)

def higher(hi1, hi2):
    for i in range(len(hi1) - 1, -1, -1):
        if hi1[i] > hi2[i]: return 1
        if hi1[i] < hi2[i]: return 2
    return 0

with open('poker.txt') as f: hands = f.readlines()

for c in hands:
    c  = c.strip().split(' ')
    h1 = c[:5]
    h2 = c[5:]

    fl1 = len(list(set([j[1] for j in h1]))) == 1
    st1,al1 = straight(h1)
    hi1 = [a[b[0]] for b in h1]
    if al1:
        for x,y in enumerate(hi1):
            if y == 14: hi1[x] = 1
    hi1 = sorted(hi1)
    sf1 = st1 and fl1
    if sf1 and hi1[-1] == 14: p1 += 1; continue

    fl2 = len(list(set([j[1] for j in h2]))) == 1
    st2,al2 = straight(h2)
    hi2 = [a[b[0]] for b in h2]
    if al2:
        for x,y in enumerate(hi2):
            if y == 14: hi2[x] = 1
    hi2 = sorted(hi2)
    sf2 = st2 and fl2
    if sf2 and hi2[-1] == 14: continue

    h = higher(hi1, hi2)

    if sf1 and not sf2: p1 += 1; continue
    if sf2 and not sf1: continue
    if sf1 and sf2:
        if h == 1: p1 += 1
        continue

    four1,c1 = fours(h1)
    four2,c2 = fours(h2)
    if four1 and not four2: p1 += 1; continue
    if four2 and not four1: continue
    if four1 and four2:
        if c1 > c2: p1 += 1
        continue

    three1,t1     = threes(h1)
    three2,t2     = threes(h2)
    pair1,pa1,hp1 = pairs(h1)
    pair2,pa2,hp2 = pairs(h2)
    full1         = False
    if three1 and pair1:
        full1     = True
    full2         = False
    if three2 and pair2:
        full2     = True
    if full1 and not full2: p1 += 1; continue
    if full2 and not full1: continue
    if full1 and full2:
        if t1 > t2: p1 += 1
        continue

    if fl1 and not fl2: p1 += 1; continue
    if fl2 and not fl1: continue
    if fl1 and fl2:
        if h == 1: p1 += 1
        continue

    if st1 and not st2: p1 += 1; continue
    if st2 and not st1: continue
    if st1 and st2:
        if h == 1:  p1 += 1
        continue

    if three1 and not three2: p1 += 1; continue
    if three2 and not three1: continue
    if three1 and three2:
        if t1 > t2: p1 += 1
        continue

    tp1 = pair1 and len(pa1) > 1
    tp2 = pair2 and len(pa2) > 1
    if tp1 and not tp2: p1 += 1; continue
    if tp2 and not tp1: continue
    if tp1 and tp2:
        if pa1[-1] > pa2[-1] or (pa1[-1] == pa2[-1] and pa1[0] > pa2[0]): p1 += 1
        elif pa1[-1] == pa2[-1] and pa1[0] == pa2[0] and hp1[0] > hp2[0]: p1 += 1
        continue

    if pair1 and not pair2: p1 += 1; continue
    if pair2 and not pair1: continue
    if pair1 and pair2:
        if pa1[-1] > pa2[-1] or (pa1[-1] == pa2[-1] and higher(hp1,hp2) == 1):
            p1 += 1
        continue

    if h == 1: p1 += 1

print('answer:', p1)
