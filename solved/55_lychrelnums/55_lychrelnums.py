def ispalindrome(n):
    n = str(n)
    l = len(n)
    for i in range(l // 2):
        if n[i] != n[l - i - 1]: return 0
    return 1

def islychrel(n):
    i = 0
    while i < 50:
        n += int(str(n)[::-1])
        if ispalindrome(n): return 0
        i += 1
    return 1

r = 0
for i in range(12,10**4):
    if islychrel(i): r += 1

print r
