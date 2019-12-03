
with open("listofprimes_lt10_8.txt", "r") as f: primes = f.readlines()

primes     = primes[4:1000001] + [0]
facts      = [720] # (prime - 5)!
m          = 720
p          = int(primes[1]) - 5
prime_itr  = 2
last_prime = int(primes[-2]) - 4

for i in range(7, last_prime):
    m *= i
    if p == i:
        facts.append(m)
        p = int(primes[prime_itr]) - 5
        prime_itr += 1

'''
for i in range(len(facts)):
    print(int(primes[i]), facts[i])
'''

print('done calculating, writing to file')

'''
f = open("listofprimeminus5facts.txt", "w")
for i in facts:
    f.write(str(i) + '\n')
f.close()
'''
