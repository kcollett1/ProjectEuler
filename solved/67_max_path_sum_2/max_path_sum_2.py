#!/usr/bin/env python

with open("p067_triangle.txt","r") as data:
	triangledata = data.readlines()
data.close()

triangle = [[] for i in range(len(triangledata))]

for row in range(0,len(triangledata)):
	for col in triangledata[row].split():
		triangle[row].append(int(col))

for row in range(len(triangle) - 2,-1,-1):
	for col in range(0,len(triangle[row])):
		if triangle[row + 1][col] > triangle[row + 1][col + 1]:
			triangle[row][col] = triangle[row][col] + triangle[row + 1][col]
		else:
			triangle[row][col] = triangle[row][col] + triangle[row + 1][col + 1]

print triangle[0][0]

exit
