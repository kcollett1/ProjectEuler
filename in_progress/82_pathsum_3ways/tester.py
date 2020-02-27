#!/Users/kcolletti1/opt/anaconda3/bin/python3

# load data into variables to work with ###

import sys

with open('matrix.txt','r') as f: rows = f.readlines()

for i,row in enumerate(rows):
    rows[i] = [int(i) for i in row.strip().split(',')]

# done loading data #######################

# start algorithm #########################

row_len  = len(rows)
col_len  = len(rows[0])
minsum = 10 ** 10

for start in range(x_len):
    sum_tracker = [[0 for _ in range(col_len)] for _ in range(row_len)]
    prev_direct = [1 for _ in range(start)] + [0] + [-1 for _ in range(start + 1, row_len)]
    curr_direct = [i for i in prev_direct]

    sum_tracker[start][0] = rows[start][0]
    for row in range(start + 1, row_len):
       sum_tracker[row][0] = sum_tracker[row - 1][0] + rows[row][0]
    for row in range(start - 1, -1, -1):
        sum_tracker[row][0] = sum_tracker[row + 1][0] + rows[row][0]

    #for col in range(1, col_len): # FIXME: when algo working correctly for each row in a col
                               #            extend to evaluating each col until last col
    col = 1 # TEMP while figuring out algo. when extended to loop, delete this line
    dirs_poss = [[] for _ in range(row_len)]
    for row in range(start, row_len):
        # stuff
        # curr_direct[][] = blah blah blah
        if row > 0 and curr_direct[row - 1][col] < 1:
            dirs_poss[row].append(1)
        if row + 1 < row_len:
            if curr_direct[row + 1][col] #FIXME wrong
    for row in range(start - 1, -1, -1):
        # stuff
        # curr_direct[][] = blah blah blah
    # done with stuff, save curr_dir in prev_dir var for next iteration of columns
    prev_direct = [i for i in curr_direct]
    


print('answer:', minsum)

# done with algorithm #####################
