with open('matrix.txt','r') as fo: rows = fo.readlines()

for i,row in enumerate(rows):
    rows[i] = list(map(int, row.strip().split(',')))

minsum = 10000000

def pathsum(mat, lenmat, i, j, runsum):
# assuming square matrix, but could just add extra parameter for rectangle matrix
    global minsum

    if i == lenmat - 1 and j == lenmat - 1:
        if runsum + mat[i][j] < minsum: minsum = runsum + mat[i][j]
        return 1

    if i < lenmat - 1: pathsum(mat, lenmat, i + 1, j, runsum + mat[i][j])

    if j < lenmat - 1: pathsum(mat, lenmat, i, j + 1, runsum + mat[i][j])

pathsum(rows, len(rows), 0, 0, 0)

print('minsum:', minsum)
