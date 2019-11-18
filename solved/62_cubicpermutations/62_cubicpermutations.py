cubed_nums = {}
# dict = str of digits in cube sorted : [first # to get this, total # that have given permutations of this cube]

for i in range(1,10000):
    i3 = ''.join(sorted(list(str(i ** 3))))

    if len(i3) < 8: continue

    if i3 not in cubed_nums: cubed_nums[i3] = [i, 1]
    else:
        if cubed_nums[i3][1] == 4:
            print('answer: (', cubed_nums[i3][0], ') ^3 =', cubed_nums[i3][0] ** 3)
            break
        else: cubed_nums[i3][1] += 1
