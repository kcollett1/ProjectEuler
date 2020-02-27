n  = 5
pn = 7

while str(pn)[-6:] != '000000':
    n  += 1
    pn += n // 2
    #if str(n)[-2:] == '00': print(n, pn)

print('answer:', n)
