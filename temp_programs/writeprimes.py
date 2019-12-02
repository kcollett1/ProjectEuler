
prm = [3]

for p in range(5, 10**8, 2):
    sqrtp = p ** 0.5
    prime = 1
    for i in prm:
        if i > sqrtp: break
        if p % i == 0: prime = 0; break
    if prime: prm.append(p)

f = open("listofprimes_lt10_8.txt", "w")
for p in [2] + prm: f.write(str(p) + '\n')
f.close()
