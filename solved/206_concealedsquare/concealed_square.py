import re

i    = 1000000001
i2   = i ** 2
pat  = '^1\d2\d3\d4\d5\d6\d7\d8\d9\d0$'
mobj = re.match(pat,str(i**2))

while mobj == None and len(str(i2)) == 19:
    i   += 1
    i2   = i ** 2
    mobj = re.match(pat,str(i2))

print('answer:', i)
