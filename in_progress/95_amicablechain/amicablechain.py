def sum_divisors(n):
    if n < 2: return 0
    div = [1]
    i   = 2
    ndi = n // i
    while ndi >= i:
        if n % i == 0:
            div.append(i)
            if ndi != i: div.append(ndi)
        i  += 1
        ndi = n // i
    return sum(div)

chains = {}
for j in range(11):
    k = j
    chain = []
    while k not in chain:
        if k in chains:
            chain += chains[k]
            break
        chain.append(k)
        k = sum_divisors(k)
    chains[j] = chain
    print(j, chain)

found_div  = {}
max_chain  = []
len_maxch  = 0

'''
for i in range(2, 1000000):
    if i not in found_div:
        curr_chain = [i]
        sumdivis = sum_divisors(i)
'''     
