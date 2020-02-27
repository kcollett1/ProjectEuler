#!/Users/kcolletti1/opt/anaconda3/bin/python3

# load data into variables to work with ###

import sys

with open('matrix.txt','r') as f: rows = f.readlines()

for i,row in enumerate(rows):
    rows[i] = [int(i) for i in row.strip().split(',')]

# done loading data #######################

# start algorithm #########################

x_len  = len(rows)
y_len  = len(rows[0])
minsum = 10 ** 10

for start in range(0, x_len):
    for end in range(0, x_len):
        # calculate here the DP problem for the matrix
        # using the rows[start][0] and rows[end][y_len - 1]
        # locations as source and sink
        sum_trckr       = [[0 for i in range(y_len)] for j in range(x_len)]
        sum_trckr[0][0] = rows[0][0]
        for x in range(1, x_len):
            sum_trckr[x][0] = sum_trckr[x - 1][0] + rows[x][0]
        for y in range(1, y_len):
            sum_trckr[0][y] = sum_trckr[0][y - 1] + rows[0][y]
 
        for x in range(1, x_len):
            for y in range(1, y_len):
                sum_trckr[x][y] = rows[x][y]
                if sum_trckr[x - 1][y] <= sum_trckr[x][y - 1]:
                    sum_trckr[x][y] += sum_trckr[x - 1][y]
                else:
                    sum_trckr[x][y] += sum_trckr[x][y - 1]

        if sum_trckr[end][y_len - 1] < minsum: minsum = sum_trckr[end][y_len - 1]


print('answer:', minsum)

# done with algorithm #####################
