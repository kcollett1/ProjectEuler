
max_itr  = 20000
pascal   = [[1]]
S        = [0, 1]

def B(n):
    pas_arr = pascal[n][1:-((len(pascal[n]) + 1)//2)]

    prod = 1
    for i in pas_arr: prod *= i ** 2
    if n % 2 == 0: prod *= pascal[n][n // 2]

    return prod

def D(n):
    b       = B(n)
    #print('d(',n,'): B(',n,')=',b)
    run_sum = (b + 1) % 1000000007

    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            run_sum = (run_sum + i) % 1000000007
            if i != b / i: run_sum += b / i

    return int(run_sum)


for i in range(max_itr + 1):
    a = [pascal[i][j] + pascal[i][j + 1] for j in range(i)]
    pascal.append([1] + a + [1])

#for i in range(2, max_itr + 1):
#    S.append((S[i - 1] + D(i)) % 1000000007)

#print(S)

