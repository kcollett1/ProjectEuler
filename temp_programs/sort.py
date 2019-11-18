def insertion(arr):
    newarr = [arr[0]]
    for i in arr[1:]:
        itr = 0
        while itr < len(newarr) and i > newarr[itr]: itr += 1
        newarr.insert(itr,i)
    return newarr

#####################################################################

def selection(arr):
    for itr in range(len(arr)):
        minval = arr[itr]; minind = itr;
        ctr = itr
        for i in arr[itr + 1:]:
            ctr += 1
            if i < minval: minval = i; minind = ctr
        if itr != minind: arr[itr], arr[minind] = arr[minind], arr[itr]

######################################################################

def merge(arr):
    if len(arr) < 2: return arr
    def combine(arr1, arr2):
        i = 0; j = 0; res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]: res.append(arr1[i]); i += 1
            else: res.append(arr2[j]); j += 1
        if i != len(arr1):
            for x in arr1[i:]: res.append(x)
        elif j != len(arr2):
            for x in arr2[j:]: res.append(x)
        return res
    return combine(merge(arr[:len(arr)//2]), merge(arr[len(arr)//2:]))

######################################################################

def quick_Xmem(arr):
    return quicksort_Xmem([x for x in arr if x < arr[-1]]) + [arr[-1]] * arr.count(arr[-1]) + quicksort_Xmem([x for x in arr if x > arr[-1]])

######################################################################

def quick_inplace(arr, first, last):
    if first < last:
        pivot = arr[first]
        i, j = first, last
        while i < j:
            while i < len(a) and a[i] < pivot: i += 1
            while j > -1 and a[j] > pivot: j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1; j -= 1
        quick_inplace(arr, first, j)
        quick_inplace(arr, j + 1, last)
        return
    else: return

#################################################################################

a = [1,2,3,4,236,6,4,3,5,6,6,7,7,4,5,6,7,3,2,2,1,42,5,1]
print 'orig arr: ', a
a = insertion(a)
print 'after arr, insertion: ', a

print ''
print '--------------------------------------------------------------'
print ''

a = [1,2,3,4,236,6,4,3,5,6,6,7,7,4,5,6,7,3,2,2,1,42,5,1]
print 'orig arr: ', a
selection(a)
print 'after arr, selection: ', a

print ''
print '--------------------------------------------------------------'
print ''

a = [1,2,3,4,236,6,4,3,5,6,6,7,7,4,5,6,7,3,2,2,1,42,5,1]
print 'orig arr: ', a
a = merge(a)
print 'after arr, merge: ', a

print ''
print '--------------------------------------------------------------'
print ''

a = [1,2,3,4,236,6,4,3,5,6,6,7,7,4,5,6,7,3,2,2,1,42,5,1]
print 'orig arr: ', a
quick_inplace(a, 0, len(a) - 1)
print 'after arr, quick: ', a
