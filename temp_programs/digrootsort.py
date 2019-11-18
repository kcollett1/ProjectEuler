def digitRootSort(a):
    ans = []; digroots = []

    for el in a: digroots.append([sum([int(i) for i in str(el)]),el])

    # are we supposed to implement a sorting algo ourselves?
    digroots = sorted(digroots)

    for (r,n) in digroots: ans.append(n)

    return ans
