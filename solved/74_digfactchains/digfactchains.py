import math

f = [math.factorial(i) for i in range(10)]
numchains = 0

for num in range(1000000):
    chain = []
    while num not in chain:
        chain.append(num)
        r = 0
        for i in str(num): r += f[int(i)]
        num = r
    if len(chain) == 60: numchains += 1

print('answer:', numchains)
