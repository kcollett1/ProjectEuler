#!/usr/bin/env python

import itertools

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

maxsumtracker = 0
for a in list(itertools.product([0,1],repeat=14)):
	col = 0
	row = 0
	sumtracker = 75
	for step in a:
		col = col + step
		row = row + 1
		sumtracker = sumtracker + triangle[row][col]
	if sumtracker > maxsumtracker:
		maxsumtracker = sumtracker

print maxsumtracker

exit

'''
maxsum = [0]

def onestep(row, col, paths, increasepaths):
	if row > 3:
		print 'end of path'
		if increasepaths:
			maxsum.append(maxsum[paths[0]])
			paths[0] = paths[0] + 1
		return

	print 'now at ',row,' ',col,' ',paths[0],' ... triangle num= ',triangle[row][col]

	maxsum[paths[0]] = maxsum[paths[0]] + triangle[row][col]
	print 'maxsum here ',maxsum[paths[0]]

	onestep(row + 1, col, paths, False)

	onestep(row + 1, col + 1, paths, True)

row = 0; col = 0; paths = [0]
print 'we should start at 75'
onestep(row, col, paths, False)
'''

