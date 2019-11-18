
with open('roman.txt') as f: nums = f.readlines()

rom_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def pref_num(num):
    num_m = num // 1000
    r     = 'M' * num_m
    num  -= num_m * 1000

    if num > 899: r += 'CM'; num -= 900
    elif num > 499: r += 'D'; num -= 500
    elif num > 399: r += 'CD'; num -= 400

    num_c = num // 100
    r    += 'C' * num_c
    num  -= num_c * 100

    if num > 89: r += 'XC'; num -= 90
    elif num > 49: r += 'L'; num -= 50
    elif num > 39: r += 'XL'; num -= 40

    num_x = num // 10
    r    += 'X' * num_x
    num  -= num_x * 10

    if num > 8: r += 'IX'; num -= 9 # should now equal 0
    elif num > 4: r += 'V'; num -= 5
    elif num > 3: r += 'IV'; num -= 4 # should now equal 0

    return r + 'I' * num

ans = 0

for n in nums:
    n = n.strip()
    p = rom_num[n[0]]
    t = p

    for i in n[1:]:
        t += rom_num[i]
        if rom_num[i] > p: t -= 2 * p
        p = rom_num[i]

    ans += len(n) - len(pref_num(t))

print('answer:', ans)
