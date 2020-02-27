def p(L, n):
    len_L = len(L)
    i     = 0
    x     = 1
    found = 0
    while found < n:
        if str(x)[:len_L] == L: found += 1
        x *= 2
        i += 1
    return i - 1

print('ans should be 7:', p('12', 1))
print('ans should be 80', p('12', 2))
#print('ans should be 12710:', p('123', 45))
print('ans:', p('123', 678910))
