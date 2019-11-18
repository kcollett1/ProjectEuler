def numberOfSolutions(n):
    res = 0
    for a in range(n + 1, 10000):
        if (float(n*a) / float(a - n)) % 1 == 0: res += 1
    return res
