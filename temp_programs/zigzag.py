def zigzag(a):
        ans = 2; tmpans = 2; start = 1; equal = False

            while start < len(a) and a[start - 1] == a[start]: start += 1
                if start == len(a): return 1

                    bigger = (a[start - 1] > a[start])

                        for i,val in enumerate(a[:len(a)-1]):
                                    if i < start: continue

                                            if equal:
                                                            equal = (val == a[i + 1])
                                                                        if not equal: bigger = (val > a[i + 1])
                                                                                    continue

                                                                                        if val == a[i + 1]:
                                                                                                        if tmpans > ans: ans = tmpans
                                                                                                                    tmpans = 2
                                                                                                                                equal = True

                                                                                                                                        elif bigger:
                                                                                                                                                        if val < a[i + 1]:
                                                                                                                                                                            bigger = False
                                                                                                                                                                                            tmpans += 1
                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if tmpans > ans: ans = tmpans
                                                                                                                                                                                                                                            tmpans = 2

                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                    if val > a[i + 1]:
                                                                                                                                                                                                                                                                                        bigger = True
                                                                                                                                                                                                                                                                                                        tmpans += 1
                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                        if tmpans > ans: ans = tmpans
                                                                                                                                                                                                                                                                                                                                                        tmpans = 2

                                                                                                                                                                                                                                                                                                                                                            return ans


