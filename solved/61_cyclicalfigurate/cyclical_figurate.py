def getnums(n):
    dig4 = 0
    arr  = []
    num  = 1
    i    = 1

    while num < 10000:
        if num > 999:
            dig4 += 1
            arr.append(str(num))

        if n == 3: num = i * (i + 1) // 2
        elif n == 4: num = i ** 2
        elif n == 5: num = i * ((3 * i) - 1) // 2
        elif n == 6: num = i * ((2 * i) - 1)
        elif n == 7: num = i * ((5 * i) - 3) // 2
        elif n == 8: num = i * ((3*i) - 2)
        i += 1

    return arr

fig_nums = [getnums(8), getnums(7), getnums(6), getnums(5), getnums(4), getnums(3)]

def recursion(ordered_set, used):
    global fig_nums

    if len(ordered_set) == 6:
        if ordered_set[0][:2] == ordered_set[-1][-2:]:
            r = 0
            for i in ordered_set: r += int(i)
            print('set:', ordered_set, '... answer:', r)
            return 1
# this is the answer ... did not figure out how to get it to only find the answer once

    for i,u in enumerate(used):
        if u: continue
        for j in fig_nums[i]:
            if ordered_set == [] or ordered_set[-1][-2:] == j[:2]:
                u_tmp = used[:]
                u_tmp[i] = 1
                recursion(ordered_set + [j], u_tmp)

recursion([], [0,0,0,0,0,0])
