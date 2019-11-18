def constructSubmatrix(m, rToDel, cToDel):
    if len(rToDel) == len(m) or len(cToDel) == len(m[0]): return []

    ans = []; ritr = 0

    for i,r in enumerate(m):
        if i in rToDel: continue # no error if empty
        ans.append([])

        for j,c in enumerate(r):
            if j in cToDel: continue
            ans[ritr].append(c)
            ritr += 1

return ans
