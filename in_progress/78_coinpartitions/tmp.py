def translate_piglatin(in_str):
    piglatin = []

    for wd in in_str.split(' '):
        if wd[0].isdigit():
            piglatin.append(wd)
        else:
            piglatin.append(wd[1:] + wd[0] + 'ay')

    return ' '.join(piglatin)

teststr = 'the 2 quick brown foxes'
print(translate_piglatin(teststr))

def maxdiff(arr):
    diff = 0
    arr = list(set(arr))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            currdiff = abs(arr[i] - arr[j])
            if currdiff > diff:
                diff = currdiff
    return diff

testarr = [1,9,2,-7,10,4,3]
print(maxdiff(testarr))
